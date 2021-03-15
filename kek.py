import numpy


user1 = {'name':'Иван', 'age':20, 'account':1}
user2 = {'name':'Петр', 'age':25, 'account':2}
user3 = {'name':'Ольга', 'age':18, 'account':3}
user4 = {'name':'Анна', 'age':27, 'account':4}

user_list = [user1, user2, user3, user4]

for x in user_list[0:5]:
    print(x.get('age'))
    ane = x.get('age')
    #print("1111")
    

age1 = [user1['age']]
age2 = [user2['age']]
age3 = [user3['age']]
age4 = [user4['age']]
user_age = [age1, age2, age3, age4]

print("middle")
median = numpy.median(user_age)
print(median)
