print("Власов Дмитрий; 14124ПИ; Данный код находит числа армстронга")

lower=int("1")
upper=int("10000")
for num in range(lower,upper + 1):
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(sum)