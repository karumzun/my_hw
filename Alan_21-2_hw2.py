class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        return f'Area: {self.calculate_area}{self.unit} '
        pass

class Circle(Figure):
    def __init__(self, radius):
        Figure.__init__(self)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int) or value <= 0:
            raise AttributeError('Радиус должен быть int и не отрицательным числом')
        else:
            self.__radius = value



    def calculate_area(self):
        return 3.14 * self.__radius ** 2


    def info(self):
        return f'Circle radius:{self.__radius}{self.unit} Area:{self.calculate_area()}{self.unit}'


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        Figure.__init__(self)
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        if not isinstance(value, int) or value <= 0:
            raise AttributeError('Сторона должен быть int и не отрицательным числом')
        else:
            self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        if not isinstance(value, int) or value <= 0:
            raise AttributeError('Сторона должен быть int и не отрицательным числом')
        else:
            self.__side_b = value

    def calculate_area(self):
        return self.__side_a * self.__side_b / 2

    def info(self):
        return f'A={self.__side_a}{self.unit} b={self.__side_b}{self.unit} Area:{self.calculate_area()}{self.unit}'

figure = [Circle(21), Circle(7), RightTriangle(3, 4), RightTriangle(7, 9), RightTriangle(10, 9)]
for i in figure:
    print(i.info())




