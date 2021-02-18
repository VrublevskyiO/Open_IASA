A, B = map(int, input().split())

a = A % 10
lucky = [0, 1, 5, 6]
if a in lucky:
    print(a)
    quit()

if a == 4:
    if b % 2 ==0:
        print("6")
    else: print("4")
    quit()
elif a == 9:
    if b % 2 ==0:
        print("1")
    else: print("9")
    quit()

ost = B % 4

if ost == 0 and a % 2 != 0 and a != 5:
    print(1)
elif ost == 0 and a % 2 != 0 and a != 0:
    print(6)
elif ost == 1:
    print(a)
elif ost == 2:
    C = A**2
    c = C % 10
    print(c)
elif ost == 3:
    D = A ** 3
    d = D % 10
    print(d)




