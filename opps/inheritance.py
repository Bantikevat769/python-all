# single in heritance
# class A:
#     def displayA(self):
#         print("Welcome to dear sir ji")
# class B(A):
#     def dispalyB(self):
#         print("Welcome to dear kapil sir ji")

# obj=B()
# obj.displayA()
# obj.dispalyB()

# miltilevel in heritance
class X:
    def displayX(self):
        print("Welcome to dear sir ji")
class Y(X):
    def dispalyY(self):
        print("Welcome to dear kapil sir ji")
class Z(Y):
    def dispalyZ(self):
        print(" All dear Friends")

obj=Z()
obj.displayX()
obj.dispalyY()
obj.dispalyZ()
# miltiple in heritance
class X:
    def displayX(self):
        print("HI Dear ")
class Y:
    def dispalyY(self):
        print("Jee dear")
class Z(X,Y):
    def dispalyZ(self):
        print(" Bye Dear")

obj=Z()
obj.displayX()
obj.dispalyY()
obj.dispalyZ()

# Music
class Music:
    
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")

Music.play()

obj = Music()
obj.stop()

# Hierarchical inheritance
 
 
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
 
 
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()



