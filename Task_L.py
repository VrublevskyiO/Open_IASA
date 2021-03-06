A, B = list(map(int, input().split(" ")))  # замість input(0) використовуємо raw_input(0)
a = A % 10
b = B % 10
ost = B % 4
lucky = [0, 1, 5, 6]

if a in lucky:
    print(a)

elif a == 4:
    if b % 2 == 0:
        print(6)
    else:
        print(4)

elif a == 9:
    if b % 2 == 0:
        print(1)
    else:
        print(9)

elif ost == 0:
    if a % 2 != 0:
        print(1)
    else:
        print(6)
else:
    print(a ** ost % 10)

