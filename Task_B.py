def kod(x, osnova):
    rez = ""
    while x > 0:
        rez += str(x % osnova)
        x //= osnova
    return rez[::-1]


ban = list(map(int, input().split()))  # на які заборона
find_index = int(input())  # порядковий номер шуканого елементу

lucky_list = [i for i in range(10) if i not in ban]  # формуємо список дозволених чисел
kod_number = kod(find_index, len(lucky_list))  # отримуємо код в системі числення Х (довжини списку дозволених чисел)

number = ""

for j in kod_number:
    number += str(lucky_list[int(j)])

print(number)
