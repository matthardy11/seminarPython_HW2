# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите число колличество монет: "))
headsCounter = 0
tailsCounter = 0

for i in range(n):
  x = int(input("Введите 0 если решка или 1 если орел: "))
  if x == 0:
    tailsCounter = tailsCounter + 1
  else:
    headsCounter = headsCounter + 1

if tailsCounter > headsCounter:
  print("Минимальное число монет: ", headsCounter)
else:
  print("Минимальное число монет: ", tailsCounter)