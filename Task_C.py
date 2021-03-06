M, n = list(map(float, input().split()))    # поміняти потім на raw_input()
n = int(n + 1)

kef = []  # створюємо єдине сховище коефіцієнтів
a, b = list(map(float, input().split()))  # тут записуємо коефіцієнти для Землі

kef.append(a)  # прискорення від Землі

for i in range(n):  # коефіцієнти для решти планет у порядку гальмування перед ними, а потім розгону від них
    kef.extend(list(map(float, input().split()))[::-1])

kef.append(b)  # гальмування перед Землею

gallon = 0  # сума топлива

try:
    for i in kef[::-1]:
        k = (M + gallon) / (i - 1)
        gallon += k
except ZeroDivisionError:
    gallon = -1

for i in kef:
    if i <= 1:
        gallon = -1

print(gallon)
