print ('HomeWork+')
n = input("Ведите целое число: ")
n = int(n) - 2
a1 = a2 = 1
while n > 0:
    a1, a2 = a2, a1 + a2
    n -= 1
print("Значение этого элемента:", a2)