
def separator(input_string):
    if input_string == '':
        return ''
    temp = ''
    result=[]
    set_before_minus = {':','*','^',''}
    clean = []
    clean2 = []

    for i,symb in enumerate(input_string[:-1]):
        if symb == "+" or (symb == "-" and input_string[i-1] not in set_before_minus) :
            result.append(temp)
            temp =''
        temp += symb
    temp += input_string[-1]
    result.append(temp)

    for x in result:
        if any("i" in filt for filt in x) == True:
            clean.append(x)
        else:
            clean2.append(x)

    clean = ''.join(clean)
    if clean != '':
        if clean[0] == '+':
            clean = ''.join([clean[i] for i in range(len(clean)) if i != 0])      
    clean2 = ''.join(clean2)
    if clean2 != '':
        if clean2[0] == '+':
            clean2 = ''.join([clean2[i] for i in range(len(clean2)) if i != 0]) 

    return clean2, clean

# def separator(input_string):
#     temp = ''
#     result=[]
#     set_before_minus = {':','*','^',''}

#     for i,symb in enumerate(input_string[:-1]):
#         if symb == "+" or (symb == "-" and input_string[i-1] not in set_before_minus) :
#             result.append(temp)
#             temp =''
#         temp += symb
#     temp += input_string[-1]
#     result.append(temp)
#     # result = list(map(str,result))
#     print(result)
#     real = ''
#     img = ''
#     for x in result:
#         if x.find('i') == -1:
#             real+=x
#         else:
#             img+=x
#     if real !="":
#         if real[0]=='+': real = real[1:]
#     if img !="":
#         if img[0]=='+': img = img[1:]
#     return real,img

