import array

inp = int(input("Введите размер маски подсети от 0 до 32: "))
if inp < 0 or inp > 32:
    print("Неверный ввод")
    exit()

a = 0
b = float(128)
j = 0
mask =[0,0,0,0]

print("Маска подсети:")
for i in range (inp):
    if b == 0.5:
        mask[j]= a
        j = j+1
        a = 0
        b = 128
    else:
        pass

    a = a + b
    b = b / 2

mask[j] = a
print(mask)