print("\t____Simple calculator______")
def add():
    c = a+b
    print("sum is :", c)
def sub():
    c = a-b
    print("subtraction is :", c)
def mul():
    c = a*b
    print("multiplication :", c)
def div():
    c = a/b
    print("divition :", c)
def squre():
    c = a*a
    print("squre :", c)
while (True):
    print("===========================================")
    print("\n 1.Addition")
    print("\n 2.Subtraction")
    print("\n 3.Multiplication")
    print("\n 4.Divition")
    print("\n 5.Squre root")
    print("\n 6.Exit")
    print("===========================================")
    select = int(input("Select number : "))
    if select == 1:
        print("Enter two number : ")
        a = int(input())
        b = int(input())
        add()
        print("========================")
    elif select == 2:
        print("Enter two number : ")
        a = int(input())
        b = int(input())
        sub()
        print("========================")
    elif select == 3:
        print("Enter two number : ")
        a = int(input())
        b = int(input())
        mul()
        print("========================")
    elif select == 4:
        print("Enter two number : ")
        a = int(input())
        b = int(input())
        div()
        print("========================")
    elif select == 5:
        print("Enter a number : ")
        a = int(input())
        print("========================")
        squre()
        print("========================")  
    else:
        print("\n choice is Wrong :")
        break
        

