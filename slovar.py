
account1 = {'login':'ivan', 'password':'q1'}
account2 = {'login':'petr', 'password':'q2'}
account3 = {'login':'olga', 'password':'qq5'}
account4 = {'login':'anna', 'password':'qqq4'}

user1 = {'name':'Иван', 'age':20, 'account':account1}
user2 = {'name':'Петр', 'age':25, 'account':account2}
user3 = {'name':'Ольга', 'age':18, 'account':account3}
user4 = {'name':'Анна', 'age':27, 'account':account4}

user_list = ['user1','user2','user3','user4']

en = input("Введите ключ (name или account): ")
if en.lower() == 'name':
    print("значение ключа name для юзера 1 = Иван")
    print("значение ключа name для юзера 2 = Петр")
    print("значение ключа name для юзера 3 = Ольга")
    print("значение ключа name для юзера 4 = Анна")
elif en.lower() == 'account':
    print(f"значение ключа account для юзера 1 = Иван {account1}")
    print(f"значение ключа account для юзера 2 = Петр {account2}")
    print(f"значение ключа account для юзера 3 = Ольга {account3}")
    print(f"значение ключа account для юзера 4 = Анна {account4}")