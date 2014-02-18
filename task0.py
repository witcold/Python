even = 0 
odd = 0
flag = True
x = ''
while flag or x != '':
    x = raw_input(':> ')
    if x != '':
        flag = False
        if int(x) % 2 == 0:
            even += 1
        else:
            odd += 1
print('even = ' + str(even))
print('odd = ' + str(odd))
