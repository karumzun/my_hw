class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self, fullname, age, is_married):
        print('fullname: ' + self.fullname, 'age: ' + self.age, 'is_maried: ' + self.is_married)

class Students(Person):
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = dict(marks)

    def average(self):
        print(sum(self.marks) / len(self.marks))



class Teacher(Person):
    salary = 20000
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience

    # def total_salary(self):
    #     c = self.experience - 3
    #     b = self.salary / 100 * 5
    #     self.salary = b * c + self.salary
    #     print(int(self.salary))
    def Teacher_cash(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary / 100 * 5) * (self.experience - 3))
            return new_salary

a = Teacher('Наталья Сорокина', 35, 'yes', 14)
print('fullname: ' + a.fullname, 'age: ' + str(a.age), 'is_maried: ' + a.is_married, 'experience: ' + str(a.experience), 'salary ' + str(a.Teacher_cash()))




def create_students():
    student1 = Students(fullname="Алибек", age=22, is_married=True, marks={
        "биология": 5,
        "история": 4,
        "математика": 5,
        "физика": 2,
        "русский-язык": 3,
    })
    student2 = Students(fullname="Игорь", age=26, is_married=False, marks={
        "биология": 4,
        "история": 4,
        "математика": 4,
        "физика": 3,
        "русский-язык": 4,
    })
    student3 = Students(fullname="Алихан", age=15, is_married=False, marks={
        "биология": 5,
        "история": 5,
        "математика": 5,
        "физика": 5,
        "русский-язык": 5,
    })
    g = [student1, student2, student3]
    return g



for i in create_students():
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.fullname}\n"
          f"Age: {i.age}\n"
          f"Maried: {i.is_married}\n"
          f"Average marks: {sum(list)/len(list)}\n")




