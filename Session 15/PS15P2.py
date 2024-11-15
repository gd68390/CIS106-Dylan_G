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
        print('Sticker price of', self.make, self.model, ': $', f'{self.sticker:.2f}')
        print('Total cost for', self.make, self.model, ': $', f'{self.discount:.2f}')
        print()

class Luxury(Sport):

    def options(self, SportWheels, SportEngine, SportInterior, GPS, Self_Driving):
        super().options(SportWheels, SportEngine, SportInterior)

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

        if GPS == 'Y':
            self.GPS = 5000
            print('GPS Unit: $', self.GPS)
        else:
            self.GPS = 0

        if Self_Driving == 'Y':
            self.Self_Driving = 10000
            print('Self-Driving feature: $', self.Self_Driving)
        else:
            self.Self_Driving = 0

    def pricewithoptions(self):
        self.discount = (self.SportInterior + self.SportEngine + self.SportWheels + self.GPS + self.Self_Driving + self.sticker) * .90
        print('Sticker price of', self.make, self.model, ': $', f'{self.sticker:.2f}')
        print('Total cost for', self.make, self.model, ': $', f'{self.discount:.2f}')
        print()

car_1 = Sport('Honda', 'Civic Type R', 45500)
car_1.options('Y', 'Y', 'Y')
car_1.pricewithoptions()

car_2 = Sport('Acura', 'TLX Type S', 54600)
car_2.options('Y', 'Y', 'Y')
car_2.pricewithoptions()

car_3 = Luxury('Mercedes-Maybach', 'S 580 4MATIC', 203500)
car_3.options('Y', 'Y', 'Y', 'Y', 'Y')
car_3.pricewithoptions()



