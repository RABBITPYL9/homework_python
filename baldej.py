baza_studenta = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44]
baza_studentov = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
baza_student = [1]

spisok = ['Студент', 'Студента', 'Студентов']

a = int(input("Введите число"))

if a in baza_studenta:
    print("OK naydeno")
    print(f"{spisok[1]}")
else: 
    print("Не найдено в первом списке,ищем в следующем")
    if a in baza_studentov:
        print("Найдено во втором списке(база студентов)")
    else:
        print("Не найдено в двух спиках, ищем в третьем")
        if a in baza_student:
            print("Найдено в третем списке(студент)")
        else:
            print("Не найдено во всех списках")