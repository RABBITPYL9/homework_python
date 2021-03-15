
import numpy

account1 = {'login':'ivan', 'password':'q1'}
account2 = {'login':'petr', 'password':'q2'}
account3 = {'login':'olga', 'password':'qq5'}
account4 = {'login':'anna', 'password':'qqq4'}

user1 = {'name':'Иван', 'age':20, 'account':account1}
user2 = {'name':'Петр', 'age':25, 'account':account2}
user3 = {'name':'Ольга', 'age':18, 'account':account3}
user4 = {'name':'Анна', 'age':27, 'account':account4}

user_list = [user1,user2,user3,user4]

en = input("Введите ключ (name или account): ")
if en.lower() == 'name':
    print(f"значение ключа name для юзера 1 = {user1['name']}")
    print(f"значение ключа name для юзера 1 = {user2['name']}")
    print(f"значение ключа name для юзера 1 = {user3['name']}")
    print(f"значение ключа name для юзера 1 = {user4['name']}")
elif en.lower() == 'account':
    print(f"значение ключа account для юзера 1 = Иван {account1}")
    print(f"значение ключа account для юзера 2 = Петр {account2}")
    print(f"значение ключа account для юзера 3 = Ольга {account3}")
    print(f"значение ключа account для юзера 4 = Анна {account4}")
else:
    print("Введенный ключ не найден")

ent = int(input("Введите порядковый номер: "))
if ent == 1:
    print(f'Данные по user{ent}:')
    print(f'имя: {user_list[(int(ent)-1)]["name"]}')
    print(f'возраст: {user_list[(int(ent)-1)]["age"]}')
    print(f"логин: {user_list[(int(ent)-1)]['account']['login']}")
    print(f"пароль: {user_list[(int(ent)-1)]['account']['password']}")  
elif ent == 2:
    print(f'Данные по user{ent}:')
    print(f'имя: {user_list[(int(ent)-1)]["name"]}')
    print(f'возраст: {user_list[(int(ent)-1)]["age"]}')
    print(f"логин: {user_list[(int(ent)-1)]['account']['login']}")
    print(f"пароль: {user_list[(int(ent)-1)]['account']['password']}")
elif ent == 3:
    print(f'Данные по user{ent}:')
    print(f'имя: {user_list[(int(ent)-1)]["name"]}')
    print(f'возраст: {user_list[(int(ent)-1)]["age"]}')
    print(f"логин: {user_list[(int(ent)-1)]['account']['login']}")
    print(f"пароль: {user_list[(int(ent)-1)]['account']['password']}")
elif ent == 4:
    print(f'Данные по user{ent}:')
    print(f'имя: {user_list[(int(ent)-1)]["name"]}')
    print(f'возраст: {user_list[(int(ent)-1)]["age"]}')
    print(f"логин: {user_list[(int(ent)-1)]['account']['login']}")
    print(f"пароль: {user_list[(int(ent)-1)]['account']['password']}")
else:
    print("Пользователь с указанным номером не найден")


ente = int(input("Какого пользователя перенести в конец?"))
if ente == 1:
    print(f"Список до перемещения {user_list[0:5]}")
    element1 = user_list.pop(0)
    print(element1)
    asik = user_list.append(element1)
    print(f"Пользователь с именем {user_list[(int(ente)-1)]['name']} перемещен в конец списка")
    print(f"Список после перемещения {user_list[0:5]}")

elif ente == 2:
    print(f"Список до перемещения {user_list[0:5]}")
    element1 = user_list.pop(1)
    print(element1)
    asik = user_list.append(element1)
    print(f"Пользователь с именем {user_list[(int(ente)-1)]['name']} перемещен в конец списка")
    print(f"Список после перемещения {user_list[0:5]}")

elif ente == 3:
    print(f"Список до перемещения {user_list[0:5]}")
    element1 = user_list.pop(2)
    print(element1)
    asik = user_list.append(element1)
    print(f"Пользователь с именем {user_list[(int(ente)-1)]['name']} перемещен в конец списка")
    print(f"Список после перемещения {user_list[0:5]}")
 
elif ente == 4:
    print(f"Список до перемещения {user_list[0:5]}")
    element1 = user_list.pop(3)
    print(element1)
    asik = user_list.append(element1)
    print(f"Пользователь с именем {user_list[(int(ente)-1)]['name']} перемещен в конец списка")
    print(f"Список после перемещения {user_list[0:5]}")
else:
    print ("Пользователь не найден")   

#расчет среднего возраста
numbers = [3,5,2]
median = numpy.median(numbers)


for x in user_list[0:5]:
    print(x.get('age'))
    ane = x.get('age')
    #print("1111")
    

age1 = [user1['age']]
age2 = [user2['age']]
age3 = [user3['age']]
age4 = [user4['age']]
user_age = [age1, age2, age3, age4]

median = numpy.median(user_age)
print("Средний возраст:", median)