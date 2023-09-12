# Dziedziczenie Przykład 1:
class A:

    def firstFood (self):
        print ('Kawa')

class B(A): 

    def secondFood (self):
        print('Herbata')

class C(B):

    def thirdFood (self):
        print('Ciasto')

class D(C, B):

    pass

d = D()

print(d.thirdFood())

# Dziedziczenie Przykład 2:

class Human:

    first_name = 'Jan'

class Polish: 

    country = 'Polsce'

class AllMen (Polish, Human):

    def info (self):
        print (f'{self.first_name} mieszka w {self.country}')

man = AllMen()

print(man.info())

# Dziedziczenie przykład 3:

class Flat ():

    def __init__(self, price):
        self.price = price

class Mokotow (Flat):
    def __init__(self, price, distance):
        super().__init__(price)
        self.distance = distance

flatOne = Mokotow(450000,10)

print(f'Cena mieszkania na Mokotowie wynosi: {flatOne.price} zł')

