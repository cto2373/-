import math

n=int(input('Введите целое число '))
a=0
while n > 0:
    a+=n*3
    a=math.sqrt(a)
    n-=1

print(f'{a:.2f}')
