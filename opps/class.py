# How to create a Class?
class myclass:
    x = 5 # Property of class
    
print(myclass)
# How to create object?

class myclass:
    x = 5 # Property of class
    
# creating object of myclass
m1 = myclass() # m1 is an object of class myclass
print(m1.x)
# Calling a function by object
class myclass:
    def myfunction(self): # Property of myclass
        print("Hello myFunction")
# Creating an object
m1 = myclass()
m1.myfunction()
# How create constructor
class myclass:
    # Creating a constructor
    def __init__(self):
        print("This is my constructor")
        
# creating an object
m1 = myclass()

# Change the value by object
class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfunction(self):
        print("My Name is  : "+self.name)
        
# creating an object
m1 = myclass("Sunit",25)
m1.age
m1.name

# Changing the age using object
m1.age = 26
print("Age : ",m1.age)


# # Delete the object
# del m1.age
# print("Age : ",m1.age)_