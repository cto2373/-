from datetime import timedelta ,datetime

g = int(input('Введите год '))
m = int(input('Введите месяц '))
n = int(input('Введите число '))

d = datetime(g, m, n)

oneDay=timedelta(1)

yesterday = d - oneDay
tomorrow = d + oneDay


print("Дата предыдущего дня: {} год  {} месяц   {} число".format(yesterday.year, yesterday.month, yesterday.day))
print("Дата следующего дня: {} год  {} месяц   {} число".format(tomorrow.year, tomorrow.month, tomorrow.day))
