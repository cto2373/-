a=0
b=1

h=float(input('Введите шаг'))

while (a <= b):
    x=1-((3*a)+(a**4))
    print(f"{x:.2f}")
    a+=h
