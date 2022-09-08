print ('HomeWork1')
D=int(input('Ведите день недели: '))
if D > 7 or D < 1:
    print('Ведите коректый день недели: ')
elif D == 6 or D == 7:
    print("Да, это выходной день: ")
else:
    print("Нет, это будний день: ")
