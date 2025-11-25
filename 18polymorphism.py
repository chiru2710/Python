#polymorphism-->poly means many && morphism means forms
#polymorphism using inheritance   (TYPE--1)
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism in action
def make_animal_speak(animal):
    print(animal.speak())

# Creating objects
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!



#polymorphism without using inheritance   (TYPE--2)
class Dog:
    def speak(self):
        return "Woof!"

class Robot:
    def speak(self):
        return "Beep!"

def make_it_speak(obj):
    print(obj.speak())

# Different classes with same method name
d = Dog()
r = Robot()

make_it_speak(d)   # Output: Woof!
make_it_speak(r)   # Output: Beep!
