wrong = False

while wrong == False:
    try:
        a = int(input("Число 1: "))
        b = int(input("Число 2: "))
        break
    except:
        print("Неверный ввод. Введите еще раз")
        wrong = True
        break

print(a,b)