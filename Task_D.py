Na, Nb = list(map(int, input().split()))    # raw_
A = input()[::-1]
B = input()
t = int(input())
stek = A + B

for i in range(t):
    remember = ""
    for j in range(len(stek) - 1):
        if stek[j] in A and stek[j+1] in B and stek[j] != remember:
            remember = stek[j]
            stek = stek[:j] + stek[j+1] + stek[j] + stek[j+2:]
            # print(i, j, ": ", stek[:j] + " " + stek[j] + " " + stek[j+1] + " " + stek[j+2:])

    if stek == B + A or i > t:  # виглядає як діч, але я вже не чіпав
        # print("STOP")
        break

print(stek)

