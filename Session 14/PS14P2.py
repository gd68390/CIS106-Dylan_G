class Car:
    def __init__(self, make, model, sticker):

        self.make = make
        self.model = model
        self.sticker = sticker
        self.discount = self.sticker * .90
        


class Sport(Car):

    def options(self, SportWheels, SportEngine, SportInterior):
        if SportWheels == 'Y':
            self.SportWheels = 1000
            print('Touring Wheels: $', self.SportWheels)

        else:
            self.SportWheels = 0
            
        if SportEngine == 'Y':
            self.SportEngine = 3000
            print('Upgraded engine: $', self.SportEngine)

        else:
            self.SportEngine = 0
            
        if SportInterior == 'Y':
            self.SportInterior = 2000
            print('Premium Interior: $', self.SportInterior)

        else:
            self.SportInterior = 0
    

    def pricewithoptions(self):
        self.discount = (self.SportInterior + self.SportEngine + self.SportWheels + self.sticker) * .90
        print('Sticker price of', self.make, self.model, ': $', self.sticker)
        print('Total cost for', self.make, self.model, ': $', f'{self.discount:.2f}')



car_1 = Sport('Honda', 'Civic Type R', 45500)
car_1.options('n', 'Y', 'Y')
car_1.pricewithoptions()

car_2 = Sport('Acura', 'TLX Type S', 54600)
car_2.options('Y', 'n', 'n')
car_2.pricewithoptions()



