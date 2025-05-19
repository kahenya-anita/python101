class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def display_books(self):
        for book in self.books:
            book.display_info()
            
#Instance of the Library
library = Library()
#Creating an instance of books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
#Adding books to the library
library.add_book(book1)
library.add_book(book2)
#Displaying books in the library
library.display_books()


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def display_employees(self):
        for employee in self.employees:
            print(employee.name)
        

class Employee:
    def __init__(self, name):
        self.name = name
        

tech = Department("Tech")
tech.add_employee(Employee("John"))
tech.add_employee(Employee("Jane"))
marketing = Department("Marketing")
marketing.add_employee(Employee("Bob"))
marketing.add_employee(Employee("Alice"))
tech.display_employees()


class Animal:
        
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")
        
class Chicken(Animal):
    def speak(self):
        print(f"{self.name} clucks")
     
#Association between the classes
class Apartment:
    def __init__(self, number, city):
        self.number = number
        self.city = city
        
    def get_apartment_info(self):
        print(f"Apartment Number: {self.number}")
        print(f"City: {self.city}")
        
class Person:
    def __init__(self, name, apartment):
        self.name = name
        self.apartment = apartment
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Apartment: {self.apartment.number}, {self.apartment.city}")
        

        
#Create an instance of the apartment
apartment = Apartment("123", "New York")
#Create an instance of the person
person = Person("John", apartment)
#Display the person and the aprtment info
person.display_info()