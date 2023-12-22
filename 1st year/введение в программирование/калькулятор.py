wrong_input = True
a, b = 0, 0
while (wrong_input):
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except (TypeError, ValueError):
        print("Wrong input")
        continue
    wrong_input = False
i = 1
while i < 2:
    op=input("Р—РЅР°Рє (+,-,*,/): ")
    if op in ('+', '-', '*', '/'):
        if op == '+':
            print("%.2f" % (a+b))
        elif op == '-':
            print("%.2f" % (a-b))
        elif op == '*':
            print("%.2f" % (a*b))
        elif op == '/':
            if b != 0:
                print("%.2f" % (a/b))
            else:
                print("Cannot divide by 0")
    else:
        print("Operator is not correct")
    i = i + 1