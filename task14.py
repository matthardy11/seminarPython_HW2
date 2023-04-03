# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число N: "))
counter = 1

while 2 ** counter <= n:
    print(2 ** counter)
    counter = counter + 1