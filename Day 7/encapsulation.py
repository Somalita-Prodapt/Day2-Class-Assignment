#Vehicle Management System
#attribute - brand, model, year
#method - startengine, showinfo

class Car:
    def __init__(self, brand, model, year, owner=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.__owner = owner #Private attribute to store the owner of the car

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting ")

    def show_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}") 

    def set_owner(self,owner):
        if not self.__owner: #check if no owner is set
            self.__owner = owner #set the owner of the car
        else:
            print(f"The car already has an owner: {self.__owner}. Cannot change owner.")    

    def get_owner(self):
        return self.__owner #Get the owner of the car

#create object for class
car1 = Car("Toyota","Camry",2020)
car2 = Car("Honda","Civic",2019)
print(car1.brand) #Output:Toyoto
#print(car2.__owner) --- this wont get executed as its private and it can be only be accessed by that paticular class
car1.set_owner("Alice")
print(car1.get_owner())#Alice

car1.set_owner("Bob")
print(car1.get_owner())

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
