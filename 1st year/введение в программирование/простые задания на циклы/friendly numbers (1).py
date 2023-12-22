print("Власов Дмитрий; 14124ПИ; Данный код находит дружественные числа с помощью циклов")

def divisors(n):
    yield 1
    i = 2
    while i * i <= n:
        d, r = divmod(n, i)
        if r == 0:
            yield i
            if d == i:
                break
            yield d
        i += 1

sums = [sum(divisors(i)) for i in range(1, 10000)]

for i in range(1, 10000):
    for j in range(i + 1, 10000):
        if sums[i - 1] == j and sums[j - 1] == i:
            print(i, j)