import base64


def simle(a):
    simple = True
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return simple
    else:
        simple = False
        print('Р§РёСЃР»Р° РЅРµ РїСЂРѕСЃС‚С‹Рµ')


def return_d(e, f):
    d = 1
    while ((e % f) * (d % f)) % f != 1:
        d += 1
    return d


p, q = 8, 12
while not (simle(p) and simle(q)):
    flag = True
    while flag:
        p, q = input("Р’РІРµРґРёС‚Рµ РґРІР° Р·РЅР°С‡РµРЅРёСЏ p Рё q: ").split()
        try:
            p = int(p)
            q = int(q)
        except ValueError:
            print('РљР°Р¶РµС‚СЃСЏ Р·Р°РјРµС‡РµРЅР° РѕС€РёР±РєР°...')
        else:
            flag = False

n = p * q
f = (p - 1) * (q - 1)
e = 7
d = return_d(e, f)

public_key = (e, n)
private_key = (d, n)
print(f"public_key = {public_key}, private_key = {private_key}")

print("\n\nTask1")
m = int(input(f"РџСЂРѕРІРµСЂРєР° С€РёС„СЂРѕРІР°РЅРёСЏ РЅР° m - С†РёС„СЂРµ РјРµРЅРµРµ n (РїРѕРґСЃРєР°Р·РєР°: n = {n}\n Р’РІРµРґРёС‚Рµ m:\n  "))
num1 = (m ** public_key[0]) % public_key[1]
num2 = (num1 ** private_key[0]) % private_key[1]
print(m, num1, num2)

print("\n\nTask2")
txt = b"Checking encryption"
print(f"РќР°С‡Р°Р»СЊРЅРѕРµ:   {txt}")
txt = base64.b64encode(txt)
print(f"РЁРёС„СЂРѕРІР°РЅРёРµ:  {txt}")
txt = base64.b64decode(txt)
print(f"Р Р°СЃС€РёС„СЂРѕРІРєР°: {txt}")