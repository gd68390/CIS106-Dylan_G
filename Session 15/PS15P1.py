class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def Bonus(self):
        self.rate = 0.2
        self.pay = float(self.pay * self.rate)


class Manager(Employee):
    def LongTermBonus(self):
        self.rate = 0.4
        self.pay = float(self.pay * self.rate)


class Executive(Manager):
    def ExecutiveBonus(self):
        self.rate = 2
        self.pay = float(self.pay * self.rate)
    def LongTermBonus(self):
        self.rate = 0.5
        self.pay = float(self.pay * self.rate)
    



em1 = Employee('Jack','Black',52000)
em2 = Employee('John','Doe',65000)
em3 = Employee('Chris','Johnson',62500)
em4 = Employee('Martina','Lewis',71000)
em5 = Employee('Reid','Settler',46200)
em6 = Employee('Blake','Wonders',49000)
mg1 = Executive('Arian','Thomas',82000)
mg2 = Manager('Jackie','Eifert',82000)
mg3 = Manager('Delaney','Murphy',69000)
ex1 = Executive('Vincent','Ortega',105000)
ex2 = Executive('Holden','Palewski',352000)


print(mg1.pay)
print(mg2.pay)
mg1.LongTermBonus()
mg2.LongTermBonus()
print(mg1.pay)
print(mg2.pay)
print(ex2.pay)
print(ex1.pay)
ex2.ExecutiveBonus()
print(ex2.pay)
print(ex1.pay)
ex1.ExecutiveBonus()
print(ex1.pay)







