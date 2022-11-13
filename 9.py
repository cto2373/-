
text=str(input(' Введите предложение '))

splitted_text = text.split()

for i in range(len(splitted_text)):
    if len(splitted_text[i]) > 10:
        print(' Да больше ')
        break
    else:
        print(' Нет меньше ')
        break