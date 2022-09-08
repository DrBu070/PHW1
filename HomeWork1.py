print ('HomeWork1')
D=int(input('Ведите день недели: '))
while D > 7 or D < 1:
    print('Это не день недели! ')
    D=int(input('Ведите день недели: '))
    if D == 6 or D == 7:
        print("Да, это выходной день: ")
    else:
        print("Нет, это будний день: ")

