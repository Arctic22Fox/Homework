from pyOOP import Account
from person import Person
from Dog import Dog
from Dog import Bulldog
from Shape import Cube
from Shape import Circle
# from <filename> import <class>

some_account = Account(1000.00)
some_account.deposit (500)
some_account.deposit (100)
some_account.withdraw (200)

print(some_account.getbalance())

lou = Account(500)
lou.withdraw (100)
print(lou.getbalance())

Jay = Person("Jay", 20)
Jay.getInformation()
print("Jay's name is " + Jay.name)

# base/super class
mainDog = Dog("Fenton")
print(mainDog.bark())

# derived class
bdog = Bulldog("Fenton", "Bulldog")
print(bdog.run())

# exercise 1
cube = Cube("Blue", 5, 5, 5)
print(cube.area())

circle = Circle("Green", 6)
print(circle.circumference())

# exercise 2