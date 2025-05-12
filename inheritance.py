# Types of Inheritance

# 1. Single Inheritance
class Parent:
    pass
class Child(Parent):
    pass
# 2. Multiple Inheritance
class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass
# 3. Multilevel Inheritance
class GrandParents:
    pass

class Parents(GrandParents):
    pass 

class Child(Parents):
    pass
# 4. Hybrid Inheritance

class A:
    pass
class B(A):
    pass
class C:
    pass
class D(B, C):
    pass

# 5. Hierarchical Inheritance
class Parent1:
    pass

class Child1(Parent1):
    pass 

class Child2(Parent1):
    pass

class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} makes a sound")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"{self.name} is a {self.breed}")
        
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")
    
        
scoobyDo = Dog("Scooby Do", "Great Dane")
scoobyDo.speak()

pinky = Cat("Pinky")
pinky.speak()