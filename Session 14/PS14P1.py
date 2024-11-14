class Employee:

    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def bonus(self):
        self.bonus_rate = float(input('What is your bonus rate?: '))
        self.pay = int(self.pay * self.bonus_rate)
        print('Employee Bonus: $', emp_1.pay)

class Manager(Employee):
    bonus_rate = .40
    def bonus(self):
        self.pay = int(self.pay * self.bonus_rate)
        print('Manager Bonus: $', man_1.pay)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
man_1 = Manager('John', 'Jones', 120000)

emp_1.bonus()

man_1.bonus()


