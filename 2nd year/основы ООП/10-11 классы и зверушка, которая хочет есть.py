1import time
from random import randint

c = randint(2,4)

class hunger():
    """Состояние голода"""
    
    more_than_good = 4
    norm = 3
    med = 2
    hungry = 1

    def improv_h(state):
        if state == hunger.hungry:
            return state + c
        elif state == hunger.med:
            return state + c
        elif state == hunger.norm:
            return state + c
        elif state <= 0:
            return state + c

    def decrease_h(state):
        if state == hunger.norm:
            return state - 1
        elif state == hunger.med:
            return state - 1
        elif state == hunger.hungry:
            return state - 1

class behavior():
    """Состояние поведения"""
    
    very_well = 4
    good = 3
    normal = 2
    bad = 1

    def improv_s(stat):
        if stat == behavior.bad:
            return stat + c
        elif stat == behavior.normal:
            return stat + c
        elif stat == behavior.good:
            return stat + c
        elif stat <= 0:
            return stat + c

    def decrease_s(stat):
        if stat == behavior.good:
            return stat - 1
        elif stat == behavior.normal:
            return stat - 1
        elif stat == behavior.bad:
            return stat - 1

class Animal(object):
    """Зверюшка, которая хочет есть"""

    def __init__(self,hunger_stat = hunger,behav_stat = behavior):
        self.hs = hunger_stat
        pass

    def Get_Hungry(self):
        self.hs = hunger.decrease_h(self.hs)

    def Get_Bored(self):
        self.hs = behavior.decrease_s(self.hs)

    def Get_Fed(self):
        self.hs = hunger.improv_h(self.hs)

    def Get_Well(self):
        self.hs = behavior.improv_s(self.hs)

cow = Animal(hunger.med, behavior.good)

def status_h():
    if cow.hs == hunger.more_than_good:
        print("Все супер")
    elif cow.hs == hunger.norm:
        print("Я сыт")
    elif cow.hs == hunger.med:
        print("Терпимо")
    elif cow.hs == hunger.hungry:
        print("Я хочу есть")
    else:
        print("Покормите меня уже!")

def status_s():
    if cow.hs == behavior.very_well:
        print("Все супер")
    elif cow.hs == behavior.good:
        print("Все хорошо")
    elif cow.hs == behavior.normal:
        print("Еще ничего")
    elif cow.hs == behavior.bad:
        print("Так себе")
    else:
        print("Мне не по себе!")

if cow.hs == hunger.norm:
    print("Я сыт")
elif cow.hs == hunger.med:
    print("Терпимо")
elif cow.hs == hunger.hungry:
    print("Я хочу есть")
else:
    print("Покормите меня уже!")

a = 1
x = 5.0
timing = time.time()

while True:
    if time.time() - timing > 5.00:
        timing = time.time()
        print(x," секунд")
        x = x+5
        a = a+0.5
    if a == 2:
        cow.Get_Hungry()
        cow.Get_Bored()

        status_h()
        status_s()
        a = 1

        inn = input("Что сделать? 1 - покормить, 2 - поиграть, 0 - оставить как есть, 9 - выйти ")
        if inn == "1":
            cow.Get_Fed()
            status_h()
            continue
        elif inn == "2":
            cow.Get_Well()
            status_s()
            continue
        elif inn == "0":
            continue
        elif inn == "9":
            exit()
        else:
            print("Неверный ввод")
            break

