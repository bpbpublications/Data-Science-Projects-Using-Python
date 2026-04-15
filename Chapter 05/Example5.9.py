class Animal:
    def make_sound(self):
        print("Animals make sound")
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")
class Lion(Animal):
    def make_sound(self):
        print("Lion roars")

# Using polymorphism
animal1 = Animal() #animal1 is the object of Animal class
animal1.make_sound()
animal2=Dog() #animal2 is the object of Dog class
animal2.make_sound()
animal3=Lion() #animal3 is the object of Cat class
animal3.make_sound()
