mass_objects=[22,3,2,100,23,44,23,20,13,20,22,3,2,100,23,44,23,20,13,20,22,3,2,100,23,44,23,20,13,20]
load_capacity=600
summ=0

for i in mass_objects:
    summ+=i

if summ > load_capacity:
    print('Превышает')
else:
    print('Не превышает')

print(summ)