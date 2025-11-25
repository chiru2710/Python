# ------------------------------------------------------
# Types of Inheritance in Python (With Definitions & Examples)
# ------------------------------------------------------

# 1. Single Inheritance
# Definition: A child class inherits from only one parent class.
class Parent:
    def display(self):
        print("This is the Parent class (Single Inheritance)")

class Child(Parent):
    def show(self):
        print("This is the Child class (Single Inheritance)")

print("\n=== 1. Single Inheritance ===")
obj_single = Child()
obj_single.display()
obj_single.show()


# 2. Multiple Inheritance
# Definition: A child class inherits from more than one parent class.
class Father:
    def father_method(self):
        print("This is the Father class (Multiple Inheritance)")

class Mother:
    def mother_method(self):
        print("This is the Mother class (Multiple Inheritance)")

class ChildMultiple(Father, Mother):
    def child_method(self):
        print("This is the Child class (Multiple Inheritance)")

print("\n=== 2. Multiple Inheritance ===")
obj_multiple = ChildMultiple()
obj_multiple.father_method()
obj_multiple.mother_method()
obj_multiple.child_method()


# 3. Multilevel Inheritance
# Definition: A chain of inheritance, where one class inherits from another derived class.
class Grandparent:
    def grandparent_method(self):
        print("This is the Grandparent class (Multilevel Inheritance)")

class ParentML(Grandparent):
    def parent_method(self):
        print("This is the Parent class (Multilevel Inheritance)")

class ChildML(ParentML):
    def child_method(self):
        print("This is the Child class (Multilevel Inheritance)")

print("\n=== 3. Multilevel Inheritance ===")
obj_multilevel = ChildML()
obj_multilevel.grandparent_method()
obj_multilevel.parent_method()
obj_multilevel.child_method()


# 4. Hierarchical Inheritance
# Definition: Multiple child classes inherit from the same parent class.
class ParentH:
    def parent_method(self):
        print("This is the Parent class (Hierarchical Inheritance)")

class Child1(ParentH):
    def child1_method(self):
        print("This is Child1 class (Hierarchical Inheritance)")

class Child2(ParentH):
    def child2_method(self):
        print("This is Child2 class (Hierarchical Inheritance)")

print("\n=== 4. Hierarchical Inheritance ===")
obj_child1 = Child1()
obj_child2 = Child2()
obj_child1.parent_method()
obj_child1.child1_method()
obj_child2.parent_method()
obj_child2.child2_method()


# 5. Hybrid Inheritance
# Definition: A combination of two or more types of inheritance.
class A:
    def method_a(self):
        print("This is Class A (Hybrid Inheritance)")

class B(A):
    def method_b(self):
        print("This is Class B (Hybrid Inheritance)")

class C(A):
    def method_c(self):
        print("This is Class C (Hybrid Inheritance)")

class D(B, C):  # Hybrid (Multiple + Hierarchical)
    def method_d(self):
        print("This is Class D (Hybrid Inheritance)")

print("\n=== 5. Hybrid Inheritance ===")
obj_hybrid = D()
obj_hybrid.method_a()
obj_hybrid.method_b()
obj_hybrid.method_c()
obj_hybrid.method_d()








#examples
class Suresh:
    property = "10Cr"  # cls variable
    def __init__(self, s_Name):
        self.surName = s_Name  # instance variable

class Chiru(Suresh):
    pass

a = Chiru("Jangili")
print(a.property)
print(a.surName)

#multiple inheritance
class bcci:
    def __init__(self):
        self.revenue = 10000
        print("BCCI initialized with revenue:", self.revenue)

class ipl:
    def __init__(self):
        self.teams = ["CSK", "MI", "RCB", "SRH"]
        print("IPL initialized with teams:", self.teams)

class srh(bcci, ipl):
    def __init__(self):
        bcci.__init__(self)
        ipl.__init__(self)
        self.team_name = "Sunrisers Hyderabad"
        print("SRH initialized with team name:", self.team_name)
team = srh()


class Employee:
    def _init_(self,id):
        self.emp_id=id
        print(f"{self.emp_id} is my emp_id")
        
    def details1(self):
        print("hello1")
    

class Salary:
    def _init_(self,sal):
        self.emp_sal=sal
        print(f"{self.emp_sal} is my emp_sal")
    
    def details2(self):
        print("hello2")
    
class Developer(Employee,Salary):
    def _init_(self,i_d,salary):
        Employee._init_(self,i_d)
        Salary._init_(self,salary)
        
        
a=Developer("123A","50000")   
a.details1()
a.details2()

#single inheritance
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    

class Car(Vehicle):
   def display(self):
       print("Brand: ",self.brand)
       print("Speed: ",self.speed,"Kmph")

c=Car("honda","152")
c.display()

#Multiple Inheritance – Profile Creation
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person1(self):
         print("-------------Employee Details------------")
         print("Name: ",self.name)
         print("Age: ",self.age)
class ContactDetails:
    def __init__ (self,email, phone):
        self.email=email
        self.phone=phone
    def contact(self):
        print("Email id: ",self.email)
        print("Phone no: ",self.phone)

class UserProfile(Person,ContactDetails):
    def __init__(self,name,age,email,phone):
        Person.__init__(self,name,age)
        ContactDetails.__init__(self,email,phone)
       
        
d=UserProfile("Chiranjeevi","22","chiru@gmail.com","7075897466")
d.person1()
d.contact()

#Multiple Inheritance – Student Activities
class Academics:
    def __init__(self,marks, grade):
        self.marks=marks
        self.grade=grade
    def dispaly1(self):
        print("Marks:",self.marks)
        print("Grade: ",self.grade)
class Sports:
    def __init__(self,sport_name, position):
        self.sport_name=sport_name
        self.position=position
    def display2(self):
        print("Sport_name: ",self.sport_name)
        print("Position: ",self.position)
class Student(Academics,Sports):
    def __init__(self, marks, grade,sport_name,position):
        Academics.__init__(self,marks, grade)
        Sports.__init__(self,sport_name,position)
s=Student(92,"A+","Cricket","Sr.All-Aounder")
s.dispaly1()
s.display2()

#Multilevel Inheritance – Student Marks Example
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Marks(Student):
    def __init__(self, name, id, subject1, subject2):
        super().__init__(name, id)
        self.subject1 = subject1
        self.subject2 = subject2

class Result(Marks):
    def __init__(self, name, id, subject1, subject2):
        super().__init__(name, id, subject1, subject2)

    def display_result(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Subject 1 Marks:", self.subject1)
        print("Subject 2 Marks:", self.subject2)
        total = self.subject1 + self.subject2
        print("Total:", total)
        print("Average:", total / 2)

r = Result("Chiranjeevi", "CSE560", 85, 90)
r.display_result()


#Multilevel Inheritance – Bank Customer Profile
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Account(Person):
    def __init__(self, name, age, account_number, balance):
        super().__init__(name, age)
        self.account_number = account_number
        self.balance = balance

class Customer(Account):
    def __init__(self, name, age, account_number, balance):
        super().__init__(name, age, account_number, balance)

    def display_customer(self):
        print("Customer Profile")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


c = Customer("Chiranjeevi", 22, "AC123456", 75000)
c.display_customer()

