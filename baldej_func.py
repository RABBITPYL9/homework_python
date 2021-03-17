a = int(input("Введите число: "))
baza_studenta = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44]
baza_studentov = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
baza_student = [1]
spisok = ['Студент', 'Студента', 'Студентов']

#result = 0

def plural_form(digit, rgraz, argdvag, argtri):
    result = 0
    if a in baza_studenta:
        #print("OK naydeno")
        print(f"На курс поступило: {a} {spisok[1]}")
        result +=a
        return result
    #else: 
        #print("Не найдено в первом списке,ищем в следующем")

    if a in baza_studentov:
        print(f"На курс поступили: {a} {spisok[2]}")
        result +=a
        return result
    else:
        #print("Не найдено в двух спиках, ищем в третьем")
        
        if a in baza_student:
            print(f"На курс поступил: {a} {spisok[0]}")
            result +=a
            return result
        else:
            print("Не найдено во всех списках")
    return result


plural_form(3, 'raz', 'dva', 'tri')
