ten = [i for i in range(1, 11)]
evens = list(filter(lambda x: x % 2 == 0, ten))
evens_squared = list(map(lambda x: x ** 2, evens))
print(evens_squared)

def index_finder(l1st = ten):
    while True:
        try:
            sol = input('Введите индекс: ')
            if sol == 'q':
                print('Программа завершена')
                break
            print(f'{l1st[int(sol)]}\n')
        except IndexError:
            print(f'Вводите индекс от 0 до {len(l1st)-1} ')


        except ValueError:
            print('Вводите тоько числа')

index_finder()

af = ['sf', 'sdg', 'gsg']
print(len(af))
