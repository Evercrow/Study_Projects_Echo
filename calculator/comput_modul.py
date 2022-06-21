def negative_value(string_arg):             #Модуль обработки отрицательных значений
    string_arg += ' '
    set = {'+', '-', '*', ':', '^',  ' '}
    list_string = list(string_arg)
    if list_string[0] == '-':
        list_string[1] = '-' + list_string[1]
        list_string = list_string[1:]
    long = len(list_string)
    i = 1
    while i < long:
        if list_string[i] == '-' and list_string[i-1] in set:
            list_string[i+1] = '-' + list_string[i+1]
            list_string.pop(i)
            long -=1
        i +=1    
    return list_string

def format_in_fract_list(string_arg):       #функция конвертация строки в сипсок
    from fractions import Fraction          #из чисел в формате Fraction и знаков в формате строки
    list_arg = []                           
    result = ''
    list_string = negative_value(string_arg)
    set = {'+', '-', '*', ':', '^',  ' '}
    for i in list_string:
        if i not in set:
            result += i
        else:
            list_arg.append(Fraction(result))
            list_arg.append(i)
            result = ''
    list_arg.pop()
    return list_arg
    
def calc_mod(string_arg): 
    from fractions import Fraction
    if string_arg == '':
        return ''
    list_arg = format_in_fract_list(string_arg)
    set = {'+', '-'}
    prom_result_list = []
    i = 1
    while i < len(list_arg)-1:
        if list_arg[i] == '^':
            prom_result_list.append(Fraction(list_arg[i-1]**list_arg[i+1]))
            list_arg = prom_result_list + list_arg[i+2:]
            prom_result_list = []
            i= 1
        else:
            prom_result_list.append(list_arg[i-1])
            i+=1
    prom_result_list = []
    i = 1
    while i < len(list_arg)-1:
        if list_arg[i] == '*':
            prom_result_list.append(list_arg[i-1]*list_arg[i+1])
            list_arg = prom_result_list + list_arg[i+2:]
            prom_result_list = []
            i= 1
        elif list_arg[i] == ':':
            prom_result_list.append(list_arg[i-1]/list_arg[i+1])
            list_arg = prom_result_list + list_arg[i+2:]
            prom_result_list = []
            i = 1
        else:
            prom_result_list.append(list_arg[i-1])
            i+=1
    if len(list_arg) == 1:
        result = list_arg[0]
        return result
    result = list_arg[0]
    for i in range(1, len(list_arg)-1):
        if list_arg[i] == '+':
            result += list_arg[i+1]
        elif list_arg[i] == '-':
            result -= list_arg[i+1]
    return result

