x=int(input('Введите x = '))
y=int(input('Введите y = '))

if (x > 0) and (y > 0):
    print('Первый квадрант')

elif (x < 0) and (y > 0):
    print ('Второй квадрант')

elif (x < 0) and (y < 0):
    print ('Третий квадрант')
    
elif (x > 0) and (y < 0):
    print ('Четвертый квадрант')
