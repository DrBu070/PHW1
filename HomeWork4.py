print ('HomeWork4')
n = int(input('Ведите номер четверти плоскости(1,2,3,4): '))
while n < 1 or n > 4:
    print('Не верно!')
    n = int(input('Ведите номер четверти плоскости(1,2,3,4): '))
if n == 1:
    print('x > 0 и y > 0')
elif n == 2:
    print('x < 0 и y > 0')
elif n == 3:
    print('x < 0 и y < 0')
elif n == 4:
    print('x > 0 и y < 0')
    