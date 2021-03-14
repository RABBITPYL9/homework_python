
try:
    a = input("PAROL: ")
    b = 5
    check_len = len(a)
    check_len1 = b / check_len
#    a = str(a)
except ZeroDivisionError:
    print('Нельзя делить на 0')
    
except ValueError:
    print('Пароль состоит только из буков')
#t    a = int(a)
except TypeError:
    print('Пароль состоит только из буковdffdfd')

#print('результат деления = ')
