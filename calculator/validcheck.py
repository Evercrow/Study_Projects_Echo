import colorama as cs # pip install colorama
def userTerminal():
    while True:
        print(cs.Fore.GREEN)
        user_req = input('Введите ОДНОЙ СТРОКОЙ выражение, значение которого нужно найти, и нажмите клавишу "ввод":\n')
        if bool(user_req) == False: return False
        checked_str = InputValidityTelebot(user_req)
        if checked_str == 0: break
        else : print(cs.Fore.RED,checked_str[1])

    if user_req[0] == '+': user_req = user_req[1:]
    print(cs.Fore.GREEN, "Принято, вычисляю...")
    print(cs.Fore.RESET  ,end='')

    return user_req

def InputValidityTelebot(user_req :str):
    validset = {'0','1','2','3','4','5','6','7','8','9','*',':','+','-','i','/','_','^'}
    check_str =''
    user_req = user_req.replace(' ','')
    user_req = user_req.replace('--','+')
    user_req = user_req.replace('+-','-')
    user_req = user_req.replace('-+','-')
    user_req = user_req.replace('++','+')
    user_req = user_req.replace('ii','i*i')
#code 0 : "Выражение валидно"
#code 1 : "невалидный символ"
#code 2 : "двойной символ матоперации"
#code 3 : "неправильно записана смешанная дробь"
#code 4 : "пустая матоперация в конце строки"
    if user_req[0] not in {'0','1','2','3','4','5','6','7','8','9','+','-','i'}:
        return 1,f"Первый символ невалидный - ' {user_req[0]} ' , исправьте ввод"

    for i in range(1,len(user_req)-1):
        if user_req[i]  not in validset:
            return 1,f"Вы ввели невалидный символ ' {user_req[i]} ' на {i+1}-м месте, исправьте ввод" 
        if user_req[i-1] in {'*',':','/','^','+'} and user_req[i] in {'*',':','/','^','+'}:
            return 2,f"У вас двойной символ матоперации -  на {i+1}-м месте  , уточните ввод"
        # if user_req[i] == 'i' and (user_req[i-1].isdigit()): #для варианта когда везде *i
            # user_req[i-1:i].replace('i','*i')
        if user_req[i] == '_': #проверка валидности в смешанных дробях
                if not(user_req[i-1].isdigit()): #проверяем слева
                    return 3, f"Не указана целая часть полной дроби на {i+1}-м месте  , уточните ввод"
                for let in user_req[i+1:]: #проверяем справа
                    if let in {'*',':','+','/','_','^','-'}: 
                        if check_str =='': #если сразу без цифр
                            return 3,f"Не указан числитель полной дроби на {i+1}-м месте  , уточните ввод"
                        elif let == '/': #цифры нашли, теперь смотрим знак дроби
                            check_str = let
                        elif check_str.count("/") == 0:
                            return 3,f"Не указаны части дроби на {i+1}-м месте  , уточните ввод"
                        elif len(check_str) < 2:  #знак дроби нашли, а цифры после нет
                            return 3,f"Не указан знаменатель полной дроби на {i+1}-м месте  , уточните ввод"
                        else:
                            check_str = ''
                            break  #Все нормально, выходим из проверки дроби
                    elif let == '-': #Отдельная проверка , если запретить писать минус в частях дроби.
                        if check_str == '':
                            return 4,f"Минус в числителе дроби на {i+1}-м месте запрещен, вынесите знак перед полной частью"
                        elif check_str[-1] == '/':
                            return 4,f"Минус в знаменателе дроби на {i+1}-м месте запрещен, вынесите знак перед полной частью"
                        elif len(check_str) > 0 and check_str.find('/') == -1:
                            return 3,f"Не указан числитель полной дроби на {i+1}-м месте  , уточните ввод"
                        else:
                            check_str = ''
                            break
                    else:
                        check_str +=let
    if user_req[-1] not in validset:
        return 1,f"Последний символ невалидный - ' {user_req[-1]} ' , исправьте ввод"
    if user_req[-1] in {'*',':','+','-','/','_','^'}:
        return 4,f"Матоперация ' {user_req[-1]} ' на конце пустая  , уточните ввод"
    if user_req[-2] == '_':
        return 3, f"Не указаны части дроби в конце выражения  , уточните ввод"
    return 0
