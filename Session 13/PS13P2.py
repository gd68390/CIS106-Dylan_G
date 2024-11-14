class Student:

    def __init__(self, first, last, code, credit):
        self.first = first
        self.last = last
        self.code = code
        self.credit = credit

    def tuition(self):
        if self.code == 'I':
            self.cost = 250 * int(self.credit)
        else:
            self.cost = 500 * int(self.credit)

    def statement(self):
        self.sentence = 'Student name is ' + self.first + ' ' + self.last + '. ' + '\n' + 'They owe $' + str(self.cost) + ' for tuition.'

stu_1 = Student('Leif', 'Erikson', 'I', '18')


print(stu_1.first)
print(stu_1.last)
print(stu_1.code)
print(stu_1.credit)
stu_1.tuition()
print(stu_1.cost)
stu_1.statement()
print(stu_1.sentence)
