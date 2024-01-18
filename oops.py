#class and object example
class Employee:
    def __init__(self,empid,name,age,designation):
        self.empid=empid
        self.name=name
        self.age=age
        self.designation=designation
        
        
emp1=Employee(1,'yaswanth',23,'consultant')
print(emp1.name)

#ouput:
yaswanth


#single inheritance
class Car:
    def start(self):
        print("engine is started")
    
    def stop(self):
        print("engine is stopped")
        
class Bmw(Car):
    def carname(self):
        print("The car name is BMW")

bmw1=Bmw()
bmw1.carname()
bmw1.start()

#ouput:
The car name is BMW
engine is started


#multilevel inheritance
class Car:
    def start(self):
        print("engine is started")
    
    def stop(self):
        print("engine is stopped")
        
class Bmw(Car):
    def carname(self):
        print("The car name is BMW")
        
class M4(Bmw):
    def modelname(self):
        print("The model name is M4 compitition")

bmw1=Bmw()
bmw1.carname()
bmw1.start()

m4_obj1=M4()
m4_obj1.carname()
m4_obj1.modelname()

#output:
The car name is BMW
The model name is M4 compitition


#hierarical inheritance
class Car:
    def start(self):
        print("engine is started")
    
    def stop(self):
        print("engine is stopped")
        
class Bmw(Car):
    def carname(self):
        print("The car name is BMW")
        
class Audi(Car):
    def carname(self):
        print("The car name is Audi")

bmw1=Bmw()
bmw1.carname()
bmw1.start()

audi1=Audi()
audi1.carname()
audi1.start()

#output:
The car name is BMW
engine is started
The car name is Audi
engine is started


#multiple inheritance
class Car:
    def start(self):
        print("engine is started")
    
    def stop(self):
        print("engine is stopped")
        
class Bmw:
    def carname(self):
        print("The car name is BMW")
        
class M4(Car,Bmw):
    def modelname(self):
        print("The model name is M4 Compitition")

bmw1=Bmw()
bmw1.carname()

m4=M4()
m4.carname()
m4.modelname()
m4.start()
output:
The car name is BMW
The car name is BMW
The model name is M4 Compitition
engine is started



#polymorphism
class Car:
    def start(self):
        print("engine is started")
    
    def stop(self):
        print("engine is stopped")
        
    def drive(self):
        print("All four wheel drive")
        
class Bmw(Car):
    def carname(self):
        print("The car name is BMW")
        
    def drive(self):
        print("Front wheel drive")  
    
        
class Audi(Car):
    def carname(self):
        print("The car name is Audi")
        
    def drive(self):
        print("Back wheel drive")

car1=Car()
car1.start()
car1.drive()

bmw1=Bmw()
bmw1.carname()
bmw1.drive()

audi1=Audi()
audi1.carname()
audi1.drive()

output:
engine is started
All four wheel drive
The car name is BMW
Front wheel drive
The car name is Audi
Back wheel drive




#encapsulation
class Employee:

    def __init__(self):
        self.__id=1
        self.__name = 'Yaswanth'
        self.__age=23
        
    def setId(self,id):
        self.__id=id
    
    def setName(self,name):
        self.__name=name
    
    def setAge(self,age):
        self.__age=age
    
    def getAge(self):
        return self.__age


e1 = Employee()
print(e1.getAge())

# change the price
e1.__age = 25
print(e1.getAge())

# using setter function
e1.setAge(25)
print(e1.getAge())





#dataabstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def noofwheels(self): 
        pass
    
class Car(Vehicle):
    
    def noofwheels(self): 
        print("Four Wheel")
        
        
class Bike(Vehicle):
    
    def noofwheels(self):
        print("Two wheels")
        
        
c1=Car()
b1=Bike()

c1.noofwheels()
b1.noofwheels()

output:
Four Wheel
Two wheels






