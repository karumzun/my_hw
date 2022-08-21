class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        if not isinstance(value, int) or value <= 0:
            raise AttributeError('Значение должно быть  int и не отрицательным числом')
        else:
            self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        if not isinstance(value, int) or value <= 0:
            raise AttributeError('Значение должно быть  int и не отрицательным числом')
        else:
            self.__memory = value

    def make_computations(self):

        return self.__cpu + self.__memory

    def __gt__(self, other):
        return self.__memory > other


    def __lt__(self, other):
        return self.__memory < other


    def __eq__(self, other):
        return self.__memory == other

    def __str__(self):
        return f'CPU = {self.__cpu}, Memory = {self.__memory}, Sum of CPU & Memory = {self.make_computations()}'

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = list(sim_cards_list)

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        if not isinstance(value, list):
            raise AttributeError('Значение должно быть  int и не отрицательным числом')
        else:
            self.__sim_cards_list = value


    def call_number(self, sim_number, number):
        print(f'Идет звонок на номер - {number}\nСимка: {self.__sim_cards_list[sim_number -1]}')

    def __str__(self):
        return f'Simcards List: {self.__sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
       print(f'Чтобы прийти к {location}, нужно пройти 300 метров прямо,после чего повернуть на право и пройти 60 метров')
    def __str__(self):
        return super(Computer, self).__str__() + super(Phone, self).__str__()

# l1st = [Computer(85, 16000), Phone(['1 - BeeLine', '2 - MegaCom']), SmartPhone(50,1000, ['1 - MegaCom', '2 -O!']), SmartPhone(70,2000, ['1 - O!', '2 - MegaCom'])]
# for i in l1st:
#      print(i.__str__())
# print(l1st[0] > l1st[2])
# print(l1st[2] < l1st[3])
# print(l1st[0] == l1st[3])
intel = Computer(85, 16000)
print(intel)
intel.make_computations()

sony_ericsson = Phone(['1 - BeeLine', '2 - MegaCom'])
print(sony_ericsson)
sony_ericsson.call_number(2, 99655225484)

samsung = SmartPhone(50, 1000, ['1 - MegaCom', '2 - O!'])
print(samsung)
samsung.call_number(1, 996704057267)
samsung.make_computations()
samsung.use_gps('Ahunbaeva')

iphone = SmartPhone(70, 2000, ['1 - O!', '2 - MegaCom'])
print(iphone)
iphone.call_number(1, 99656789067)
iphone.make_computations()
iphone.use_gps('China')
print(samsung < iphone)
print(intel == iphone)
print(intel > samsung)
