spisok = []
finish_spisok = []
#генерим числа от 1000 до 20000 включительно
diapa = 0
for i in range(1000, 20001):
    diapa+=i
    #print(i, end=',')
    spisok.append(i) #добавляем в наш список


#spisok.append(diapa)

print(spisok)
#вторая часть программы, которая проходит по всему списку spisok и по условию находит числа, которые делятся на 3 и 5
#кладя их в переменную result
for it in spisok:
    if it%5 == 0 and it%3 ==0:
        #print(it)
        finish_spisok.append(it)


sum = 0
for ih in finish_spisok:
    sum += i
print(sum)
        


