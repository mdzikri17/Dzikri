class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.door = 'Tutup'
        self.car = 'Mati'

    def bukaPintu(self):
        if self.door == 'Tutup':
            print('Pintu Dibuka')
            self.door = 'Buka'
        else:
            print('Pintu Ditutup')
    def tutupPintu(self):
        if self.door == 'Buka':
            print('Pintu Ditutup')
            self.door = 'Tutup'
        else:
            print('Pintu Dibuka')
    def mobilNyala(self):
        if self.car == 'Mati':
            print('Mobil Dinyalakan')
            self.car = 'Nyala'
        else:
            print('Mobil Dimatikan')
    def mobilMati(self):
        if self.car == 'Nyala':
            print('Mobil Dimatikan')
            self.car = 'Mati'
        else:
            print('Mobil Dinyalakan')
            


car1 = Car('Yaris','2022')
car1.bukaPintu()
car1.tutupPintu()
car1.mobilNyala()
car1.mobilMati()