# OOPS - OBJECT ORIENTED PROGRAMMING

# TO MAP WITH REAL WORLD SCENARIOS , WE STARTING USING OBJECTS IN CODE
# OOPS IS A FUNCTIONAL PROGRAMMING
# WE USE CLASSES AND OBJECTS IN  OOPS


# 1) CLASS
# CLASS IS A BLUEPRINT OR AN OBJECT
# CLASS IS A TEMPLATE
# CLASS IS A DESIGN PATTERN
# CLASS IS A SET OF STATE AND BEHAVIOR
# CLASS IS A COLLECTION OF DATA AND METHODS
# CLASS IS A COLLECTION OF VARIABLES AND FUNCTIONS
# CLASS IS A COLLECTION OF ATTRIBUTES AND METHODS
# CLASS IS A COLLECTION OF PROPERTIES AND METHODS


# class Student:
#     name='sreenivas'



# 2) OBJECT
# OBJECT IS AN INSTANCE OF A CLASS

# s1=Student()
# print(s1.name)


# EXAMPLE - PRINTING STUDENT NAME AND ROLL NO

# class Student():
#     name='Sreenivas'
#     roll_no=69

# s1=Student()
# print(f'{s1.name} \n{s1.roll_no}')


# EXAMPLE -  CHARACTERISTICS OF A CAR

# class Car:
#     brand='BENZ'
#     color='blue'

# car1=Car()
# print(f'{car1.brand}\n{car1.color}')




# CONSTRUCTOR 
# CONSTRUCTOR IS A SPECIAL METHOD OF A CLASS
# ALL CLASSES HAVE A FUNCTION CALLED   __init__()  , WHICH IS ALWAYS EXECUTED WHEN THE OBJECT IS INITIATED
# CONSTRUCTOR IS USED TO INITIALIZE THE OBJECTS OF A CLASS

# THE DATA WHICH IS STORED IN CLASS IS CALLED ATTRIBUTES
# THE ACTIONS WHICH ARE PERFORMED ON CLASS IS CALLED METHODS
# THE DATA WHICH IS STORED IN OBJECT IS CALLED INSTANCE VARIABLES
# THE ACTIONS WHICH ARE PERFORMED ON OBJECT IS CALLED INSTANCE METHODS
# THE DATA WHICH IS STORED IN CLASS IS CALLED CLASS VARIABLES



# class student():

#     # Default Constructor
#     def __init__(self):
#         pass

#     # Parametrized Constructor
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print('New Student Details Uploading...')

# s1=student('Sai',90)
# print(s1.name,s1.marks)

# s2=student('Sreenivas',99)
# print(s2.name,s2.marks)


# SELF PARAMETER IS A REFERENCE TO THE CURRENT INSTANCE OF THE CLASS, AND USED TO ACCESS THE VARIABLES THAT BELONGS TO THE CLASS
# SELF IS REFERENCE OF OBJECT WHICH IS DIFFERENT TO EACH OBJECT
# SELF IS USED TO DIFFERENTIATE BETWEEN CLASS AND INSTANCE VARIABLES
# SELF IS USED FOR OBJECT LEVEL



# ATTRIBUTES
# ATTRIBUTES ARE THE VARIABLES WHICH ARE USED TO STORE THE DATA IN CLASS
# ATTRIBUTES ARE ALSO CALLED INSTANCE VARIABLES
# ATTRIBUTES ARE USED TO STORE THE DATA WHICH IS SPECIFIC TO THE OBJECTS OF THE CLASS
# ATTRIBUTES ARE USED TO STORE THE DATA WHICH IS COMMON TO ALL OBJECTS OF THE CLASS


# 1) CLASS()
# 2) OBJECT()



# EXAMPLE 1  -  DETAILS OF STUDENT

# class student():
#     # CLASS ATTRIBUTE
#     collage_name='LPU'
#     def __init__(self,name,roll_no):
#         self.name=name          # OBJECT ATTRIBUTE
#         self.roll_no=roll_no    # OBJECT ATTRIBUTE
#         print('New Student...')


# name=input('Your Name:')
# roll_no=int(input('Your Roll No:'))
# s1=student(name,roll_no)
# print(f'Name:{s1.name} \nRoll No:{s1.roll_no}')
# print(f'Collage Name:{s1.collage_name}')

# name=input('Your Name:')
# roll_no=int(input('Your Roll No:'))
# s2=student(name,roll_no)
# print(f'Name:{s2.name} \nRoll No:{s2.roll_no}')
# print(f'Collage Name:{s2.collage_name}')


# EXAMPLE 2  -  CHARACTERISTICS OF A CAR

# class Car:
#     brand = 'FERRARI'
    
    # def __init__(self, car_model, milage, price):
    #     self.car_model = car_model
    #     self.milage = milage
    #     self.price = price
    #     print('Car Details...')

# car_model = input('Which Model: ')

# if car_model == 'F22':
#     car1 = Car(car_model, 69, 6969)
#     print(f'Brand: {car1.brand}\nCar Model: {car1.car_model}\nMilage: {car1.milage}\nPrice: {car1.price}')
# elif car_model == 'F33':
#     car2 = Car(car_model, 96, 9696)
#     print(f'Brand: {car2.brand}\nCar Model: {car2.car_model}\nMilage: {car2.milage}\nPrice: {car2.price}')
# elif car_model=='F44':
#     car3=Car(car_model,33,3333)
#     print(f'Brand: {car3.brand}\nCar Model: {car3.Car_model}\nMilage: {car3.milage}\nPrice: {car3.price}')
# else:
#     print("Sorry, that model is not available.")




# EXAMPLE 3 -  LIBRARY

# class library():
#     library='SSR Library'
#     def __init__(self,book_name,section,row):
#         self.book_name=book_name
#         self.section=section
#         self.row=row
#         print('Book Details...')

# book_name=input('Which Book: ')

# if book_name=='Harry Potter':
#     book1=library(book_name,'Fantasy',3)
#     print(f'Library Name: {book1.library}\nSection: {book1.section}\nRow: {book1.row}')

# elif book_name=='Hobbit':
#     book2=library(book_name,'Adventure',4)
#     print(f'Library_Name: {book2.library}\nSection: {book2.section}\nRow: {book2.row}')

# elif book_name=='Shades of Grey':
#     book3=library(book_name,'Romance',5)
#     print(f'Library Name: {book3.library}\nSection: {book3.section}\nRow: {book3.row}')

# elif book_name=='Anabel':
#     book4=library(book_name,'Horror',6)
#     print(f'Library Name: {book4.library}\nSection: {book4.section}\nRow: {book4.row}')

# else:
#     print('Not Available')



# METHODS
# METHODS ARE FUNCTIONS THAT BELONGS TO OBJECTS
# IT DEFINES HOW OBJECT WORKS
# IT IS USED TO PERFORM SPECIFIC TASKS
# IT IS USED TO MODIFY THE STATE OF OBJECT
# IT IS USED TO RETURN VALUES


# class student():
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
    
#     def welcome(self):
#         print('Welcome',self.name)
    
#     def marks(self):
#         return self.marks

# s1=student('Sreenivas',69)
# s1.welcome()
# print(f'Marks: {s1.marks}')





# PROBLEMS

# 1) CREATE A STUDENT CLASS THAT TAKES NAME AND MARKS OF 3 SUBJECTS AS ARGUMENTS IN CONSTRUCTOR. THEN CREATE A METHOD TO PRINT THE AVERAGE

# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print(f'Hello, {self.name} Your Average Marks is: {sum/len(self.marks)}')

# s1=Student('Sreenivas',[99,88,77])
# s1.get_avg()




# STATIC METHODS
# STATIC METHODS ARE USED TO PERFORM TASKS THAT DOES NOT DEPEND ON THE STATE OF OBJECT
# IT IS USED TO PERFORM TASKS THAT DOES NOT NEED TO ACCESS THE INSTANCE VARIABLE
# IT IS USED TO PERFORM TASKS THAT DOES NOT NEED TO CALL OTHER INSTANCE METHODS
# IT IS USED TO PERFORM TASKS THAT DOES NOT NEED TO ACCESS THE CLASS VARIABLE

# STATIC METHOD IS USED AT CLASS LEVEL
# WE CAN WRITE A CLASS WITHOUT USING SELF WITH STATIC METHOD

#    @ staticmethod - IT IS A DECORATOR TO WRITE STATIC METHOD

# DECORATOR
# DECORATOR ALLOW US TO WRAP ANOTHER FUNCTION IN ORDER TO EXTEND THE BEHAVIOR OF THE WRAPPED FUNCTION WITHOUT PERMANENTLY MODIFYING IT.


# EXAMPLE

# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     @staticmethod
#     def hello():
#         print("Hello")

#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print(f'Hello, {self.name} Your Average Marks is: {sum/len(self.marks)}')

# s1=Student('Sreenivas',[99,88,77])
# s1.get_avg()
# s1.hello()







# PILLARS OF OBJECT ORIENTED PROGRAMMING

# OOPS HAVE 4 PILLARS

# 1. ABSTRACTION
# 2. ENCAPSULATION
# 3. INHERITANCE
# 4. POLYMORPHISM




# 1. ABSTRACTION



# ABSTRACTION IS THE PROCESS OF HIDING THE IMPLEMENTATION  DETAILS OF CLASS AND SHOWING ONLY THE ESSENTIAL FEATURES TO THE USER

# class car():
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.acc=True
#         self.brk=False
#         self.clutch=True
#         print('Car Started...')
# car1=car()
# car1.start()




# 2. ENCAPSULATION



# WRAPPING DATA AND FUNCTIONS INTO A SINGLE UNIT (OBJECT).
# ENCAPSULATION IS USED TO HIDE THE INTERNAL DETAILS OF AN OBJECT FROM THE OUTSIDE

# class car():
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.acc=True
#         self.brk=False
#         self.clutch=True
#         print('Car Started...')
# car1=car()
# car1.start()




# PROBLEMS

# QUESTION - CREATE A CLASS WITH 2 ATTRIBUTE - BALANCE AND ACCOUNT NUMBER.
#            CREATE A METHOD FOR DEBIT, CREDIT AND PRINTING THE BALANCE

# class Account():
#     def __init__(self,acc_no,bal):
#         self.account_number=acc_no
#         self.balance=bal
#     def debit(self,amount):
#         self.balance -= amount
#         print('Rs.', amount ,'was Debited from your account')
#         print('Remaining Balance: ', self.get_balance())
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs. ",amount,"Credited into account")
#         print("Total Balance: ",self.get_balance())
#     def get_balance(self):
#         return self.balance


# account1=Account(12109469,100000)
# account1.debit(1000)
# account1.credit(2000)
# account1.credit(40000)
# account1.debit(1000)






#  del Keyword 
#  del keyword is used to delete the object properties or object itself from the memory.


# class student():
#     def __init__(self,name):
#         self.name=name

# s1=student('Sreenivas')
# print(s1.name)

# del s1
# print(s1.name)




# PRIVATE ATTRIBUTES and METHODS
# PRIVATE ATTRIBUTES AND METHODS ARE MEANT TO BE USED ONLY WITHIN THE CLASS AND ARE NOT ACCESSIBLE FROM OUTSIDE THE CLASS.
# IT IS USED TO PREVENT EXPOSING INSTANCE ATTRIBUTES OUTSIDE OF THE CLASS
# IT IS USED TO PREVENT EXPOSING INSTANCE METHODS OUTSIDE OF THE CLASS



# class Account():
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
    
#     def reset_pass(self):
#         print(self.__acc_pass)

# account1=Account('1234','1234')
# print(f'{account1.acc_no}\n{account1.reset_pass()}')





# 3. INHERITANCE

# INHERITANCE IS A PROCESS WHERE ONE CLASS (CHILD CLASS / DERIVED CLASS) CAN INHERIT THE PROPERTIES AND METHODS OF ANOTHER CLASS (PARENT CLASS / BASED CLASS)


# IT IS USED TO CREATE A HIERARCHICAL CLASS STRUCTURE
# IT IS USED TO REUSE THE CODE
# IT IS USED TO CREATE A SPECIALIZED CLASS
# IT IS USED TO CREATE A GENERALIZED CLASS
# IT IS USED TO CREATE A CLASS HIERARCHY
# IT IS USED TO CREATE A CLASS TREE
# IT IS USED TO CREATE A CLASS GRAPH
# IT IS USED TO CREATE A CLASS NETWORK
# IT IS USED TO CREATE A CLASS WEB
# IT IS USED TO CREATE A CLASS MATRIX
# IT IS USED TO CREATE A CLASS GRID



# EXAMPLE

# class Car:

#     @staticmethod
#     def start():
#         print('Car Started...')
    
#     @staticmethod
#     def stop():
#         print('Car Stopped...')

# class toyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# car1=toyotaCar('Fortuner')
# car2=toyotaCar('Prius')

# print(car1.name)
# print(car1.start())

# print(car2.name)
# print(car2.stop())






# THERE ARE  3 TYPES OF INHERITANCE

# 1) SINGLE INHERITANCE
# 2) MULTI-LEVEL INHERITANCE
# 3) MULTIPLE INHERITANCE



# 1) SINGLE INHERITANCE

# IN SINGLE INHERITANCE THERE WILL BE ONLY ONE PARENT CLASS AND ONE CHILD CLASS


# EXAMPLE

# class Car:

#     @staticmethod
#     def start():
#         print('Car Started...')
    
#     @staticmethod
#     def stop():
#         print('Car Stopped...')

# class toyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# car1=toyotaCar('Fortuner')
# car2=toyotaCar('Prius')

# print(car1.name)
# print(car1.start())

# print(car2.name)
# print(car2.stop())



# 2) MULTI-LEVEL INHERITANCE

# In multilevel inheritance, a class is derived from another derived class, creating a chain of inheritance.
# The derived class inherits the properties and methods of the parent class and the grandparent class.
# There is a parent class, a child class derived from the parent, and another child class derived from the first child class.
# Each level of inheritance adds new properties and behaviors to the classes.


# EXAMPLE


# class Car:

#     @staticmethod
#     def start():
#         print('Car Started...')
    
#     @staticmethod
#     def stop():
#         print('Car Stopped...')

# class toyotaCar(Car):
#     def __init__(self,brand):
#         self.name=brand

# class fortuner(toyotaCar):
#     def __init__(self,type):
#         self.type=type

# class Prius(toyotaCar):
#     def __init__(self,type):
#         self.type=type

# car1=fortuner('diesel')
# print(car1.type)
# print(car1.start())

# car2=Prius('Petrol')
# print(car2.type)
# print(car2.start())





# 3) MULTIPLE INHERITANCE

# In multiple inheritance, a child class inherits from more than one parent class. 
# This allows the child class to inherit properties and behaviors from all of its parent classes, combining them into a single class.


# EXAMPLE

# class A:
#     varA='welcome to class A'

# class B:
#     varB='welcome to class B'

# class C(A , B):
#     varC='welcome to class C'

# C1=C()
# print(C1.varA)
# print(C1.varB)
# print(C1.varC)





# SUPER METHOD 

# super() METHOD IS USED TO ACCESS THE METHODS OF THE PARENT CLASS
# IT IS USED TO CALL THE CONSTRUCTOR OF THE PARENT CLASS
# IT IS USED TO ACCESS THE VARIABLES OF THE PARENT CLASS
# IT IS USED TO ACCESS THE CLASS OF THE PARENT CLASS


# EXAMPLE

# class Car:
#     def __init__(self,type):
#         self.type=type
    
#     @staticmethod
#     def start():
#         print('Car Started...')
    
#     @staticmethod
#     def stop():
#         print('Car Stopped...')

# class toyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# car1=toyotaCar('fortuner','electric')
# print(car1.name)
# print(car1.type)




# CLASS METHOD (DECORATOR)

# NOTE :- THERE ARE 3 TYPES OF METHODS IN CLASSES 



# NOTE
# 1. INSTANCE METHOD
# 2. STATIC METHOD (DECORATOR)
# 3. CLASS METHOD  (DECORATOR)
# 4. GETTER        (DECORATOR)
# 5. SETTER        (DECORATOR)



# CLASS METHOD IS A "DECORATOR"  SIMILAR TO STATIC METHOD

# @staticmethod  ==  @classmethod

# CLASS METHOD IS BOUND TO THE CLASS AND RECEIVES THE CLASS AS IMPLICIT FIRST ARGUMENT

# NOTE :- STATIC METHOD CAN'T ACCESS OR MODIFY CLASS STATE AND GENERALLY FOR UTILITY

# CLASS METHOD IS A SPECIAL TYPE OF METHOD WHICH IS USED TO CALL THE CLASS AS A FUNCTION
# IT IS USED TO CREATE A CLASS OBJECT WITHOUT CALLING THE CONSTRUCTOR
# IT IS USED TO ACCESS THE CLASS VARIABLES
# IT IS USED TO ACCESS THE CLASS METHODS
# IT IS USED TO ACCESS THE CLASS ATTRIBUTES





# TYPE 1 TO CHANGE THE ATTRIBUTES OF THE CLASS

# class person:
#     name='Sreenu'

#     def change_name(self,name):
#         # self.name=name
#         person.name=name

# p1=person()
# p1.change_name('sreenivas')
# print(p1.name)
# print(person.name)
    



# TYPE 2 TO CHANGE THE ATTRIBUTES OF THE CLASS

# class person:
#     name="sreenu"

#     def change_name(self,name):
#         self.__class__.name="Sreenivas"
    
# p1=person()
# p1.change_name('sai')
# print(p1.name)
# print(person.name)
    



# USING CLASS METHOD


# class person:
#     name='Sreenivas'

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1=person()
# p1.changeName('Sreenu')
# print(p1.name)
# print(person.name)







# PROPERTY (DECORATOR)

# WE USE   @property   DECORATOR ON ANY METHOD IN CLASS TO USE THE METHOD AS PROPERTY



# EXAMPLE 

# CALCULATING PERCENTAGE OF STUDENT MARKS AND CHANGING MARKS OF SUBJECT AND PRINTING PERCENTAGE AGAIN



# NORMAL METHOD

# class student:
#     def __init__(self,math,science,chemistry):
#         self.math=math
#         self.science=science
#         self.chemistry=chemistry
#         self.percentage=str((self.math+self.science+self.chemistry)/3)+ '%'
    
#     def calcPercentage(self):
#         self.percentage=str((self.math+self.science+self.chemistry)/3)+ '%'

# student1=student(100,90,80)

# # print(student1.percentage)

# student1.math=70
# student1.science=60
# student1.chemistry=80

# student1.calcPercentage()
# print(student1.percentage)




# BY USING PROPERTY DECORATOR


# class student:
#     def __init__(self,math,science,chemistry):
#         self.math=math
#         self.science=science
#         self.chemistry=chemistry

#     @property
#     def percentage(self):
#         return str((self.math+self.science+self.chemistry) / 3) + '%'
    


# student1=student(100,90,80)
# print(student1.percentage)

# student1.math=70
# student1.science=60
# student1.chemistry=80

# print(student1.percentage)















# 4. POLYMORPHISM

# POLY - MANY       AND        MORPH - FORMS

# POLYMORPHISM IS THE CAPABILITY OF AN OBJECT TO TAKE ON MANY FORMS.
# THE OBJECT CAN BE USED IN MANY DIFFERENT WAYS AND IT CAN BE TREATED AS DIFFERENT OBJECTS IN DIFFERENT SITUATIONS.




# OPERATOR OVERLOADING

# WHEN THE SAME OPERATOR IS ALLOWED TO HAVE DIFFERENT MEANING ACCORDING TO THE CONTEXT.


# OPERATORS AND DUNDER FUNCTIONS

# DUNDER   =  __DUNDER__

# EXAMPLE

# ADDITION            a+b   ==   a.__add__(b)
# SUBTRACTION         a-b   ==   a.__sub__(b)
# multiplication      a*b   ==   a.__mul____(b)
# DIVISION            a/b   ==   a.__truediv____(b)
# modulo              a%b   ==   a.__mod____(b)





# EXAMPLE

# CREATING TWO COMPLEX NUMBERS AND ADDING BOTH COMPLEX NUMBERS AND PRINTING FINAL NUMBER

# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
    
#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")


#     # def add(self,num2):
#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return complex(newReal,newImg)
    
#     # def sub(self,num2):
#     def __sub__(self,num2):
#         newReal=self.real-num2.real
#         newImg=self.img-num2.img
#         return complex(newReal,newImg)
    
#     # def mul(self,num2):
#     def __mul__(self,num2):
#         newReal=self.real*num2.real
#         newImg=self.img*num2.img
#         return complex(newReal,newImg)

# num1=complex(4,6)
# num1.showNumber()

# num2=complex(5,7)
# num2.showNumber()


# # num3=num1.add(num2)
# num3=num1+num2
# num3.showNumber()

# #num3=num1.add(num2)
# num3=num1-num2
# num3.showNumber()

# #num3=num1.mul(num2)
# num3=num1*num2
# num3.showNumber()





# PROBLEMS IN OOPS



# 1) DEFINE A CIRCLE CLASS TO CREATE A CIRCLE WITH RADIUS R USING THE CONSTRUCTOR
#    AND DEFINE A AREA() METHOD OF THE CLASS WHICH CALCULATES THE AREA OF THE CIRCLE.
#    AND DEFINE A PERIMETER() METHOD OF THE CLASS WHICH CALCULATES THE PERIMETER OF THE CIRCLE.


# class circle:
#     def __init__(self,radius):
#         self.radius=radius

#     # METHOD FOR RADIUS
#     def area(self):
#         # return 3.14 * self.radius ** 2
#         return (22/7) * self.radius ** 2
    
#     # METHOD FOR PERIMETER
#     def perimeter(self):
#         # return 2 * 3.14 * self.radius
#         return 2 * (22/7) *self.radius

# circle1=circle(21)
# print(circle1.area())
# print(circle1.perimeter())




# 2) DEFINE A EMPLOYEE CLASS WITH ATTRIBUTES ROLE , DEPARTMENT , SALARY . THIS CLASS ALSO HAS A SHOW DETAILS METHOD.
#    AND CREATE AN ENGINEER CLASS THAT INHERITS PROPERTIES FROM EMPLOYEE AND HAS ADDITIONAL ATTRIBUTES NAME AND AGE.

# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
    
#     # METHOD TO SHOW DETAILS OF EMPLOYEE
#     def showDetails(self):
#         print('Role = ',self.role)
#         print('Department = ',self.dept)
#         print('Salary = ',self.salary)


# # CREATING ENGINEER CLASS THAT INHERITS EMPLOYEE PROPERTIES

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__('Engineer','IT','100,000')

#         # OVERRIDE showDetails to include NAME AND AGE
#     def showDetails(self):
#         print('name = ',self.name)
#         print('Age = ',self.age)
#         super().showDetails()


# emp1=Engineer('Sreenu',21)
# emp1.showDetails()






# 3) CERATE A CLASS CALLED ORDER WHICH STORES ITEM AND IT'S PRICE
#    USE DUNDER FUNCTION    __gt__()  TO CONVEY THAT:                         __gt__    (greater)
#           ORDER1 > ORDER2 IF PRICE OF ORDER1 > PRICE OF ORDER2

# class Order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price

#     # DUNDER FUNCTION TO COMPARE ORDER OBJECTS
#     def __gt__(self , order2):
#         return self.price > order2.price

# order1=Order('Shirt',1000)

# order2=Order('T-Shirt',800)

# print(order1 > order2)
