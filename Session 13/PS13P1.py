class Employee:

    

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def bonus(self):
        self.bonus_rate = float(input('What is your bonus rate?: '))
        self.pay = float(self.pay * self.bonus_rate)
        print('Bonus: $', self.pay)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.bonus()

