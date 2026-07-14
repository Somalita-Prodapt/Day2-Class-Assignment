#Vehicle Management System
#attribute - brand, model, year
#method - startengine, showinfo

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting ")

    def show_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}") 
#create object for class
car1=Car("Toyota","Camry",2020)
car2=Car("Honda","Civic",2019)

#Call methods on the object 
car1.start_engine()
car1.show_info()

car2.start_engine()
car2.show_info()

#Another way to call methods on the objects using a list of cars
cars = [car1, car2]

for car in cars:
    car.start_engine()
    car.show_info()
