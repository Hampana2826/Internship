from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("Animal is sleeping...")
class Dog(Animal):
    def sound(self):
        print("bark")
class Cat(Animal):
    def sound(self):
        print("meow")
class Cow(Animal):
    def sound(self):
        print("moo")
dog=Dog()
cat=Cat()
cow=Cow()

dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()