one = 1
hundred = 100
attempts = 0

file = open('results.txt', 'a', encoding='UTF-8')


while True:
        a = 0
        current = (one + hundred)//2
        number = input('Ваше число {}? '.format(current))
        if number.lower() == 'да':
            attempts += 1
            file.write(f'{current} {number}\n')
            a = current
            file.write(f'Попытки: {attempts} Загаданное число: {a}\n')
            print('Я отгадал число')
            break
        elif number == '>':
            attempts += 1
            file.write(f'{current} {number}\n')
            one = current + 1
        elif number == '<':
            attempts += 1
            file.write(f'{current} {number}\n')
            hundred = current - 1
        else:
            print('Вводите только <,> и «да»')









