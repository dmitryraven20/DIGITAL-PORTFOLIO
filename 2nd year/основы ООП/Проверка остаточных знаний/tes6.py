n = list(input("Введите массив чисел: ").split())

a = n
c1 = 0 #счетчик нечетных чисел
c2 = 0 #счетчик четных чисел

for i in range(len(n)):
    n[i] = n[i] / 2
    
    if a[i] == 0:
        c2=c2+1
    else:
        c1=c1+1

    i=i+1

print("Четных чисел:",c2)
print("Нечетных чисел:",c1)