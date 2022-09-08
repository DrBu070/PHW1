print ('HomeWork3')
x = int(input('Ведите координату X: '))
y = int(input('Ведите координату Y: '))
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')
if x == 0 and y != 0:
    print('OX')
if x != 0 and y == 0:
    print('OY')