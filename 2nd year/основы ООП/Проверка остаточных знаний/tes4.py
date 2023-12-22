n = int(input("Введите число от 0 до 250: "))

if n >= 0 and n <= 250:
    c = [0,1]
    for i in range (12):
        f = c[0]+c[1]
        c[0] = c[1]
        c[1] = f

        if n == f:
            print("Число", n, "является числом Фибоначчи")
            break
            
else:
    print("Недопустимое число")
    exit

