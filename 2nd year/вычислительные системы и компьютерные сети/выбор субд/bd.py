def choose_res(v):
    a, b = input(f'{v}\n\t1. Yes\n\t0. No\n\t\t'), d.get(v)
    if a == '1':
        result = b[0]
    elif a == '0':
        result = b[1]
    else:
        print('Ошибка')
        quit()
    return result

d = {}
with open('bd.txt', 'r', encoding="utf-8") as file:
    for line in file:
        a = {line.split(':')[0]: line.split(':')[1].strip().split(',')}
        d |= a

print('Какую базу данных выбрать?')
c = list(d.keys())
res = choose_res(c[0])

while len(d.get(res.strip())) != 1:
    res = choose_res(res.strip())

print(res)