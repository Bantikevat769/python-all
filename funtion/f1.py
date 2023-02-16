# funtion 
def weekday():
    day=int(input("enter a numbr : "))
    if day==1:
        print("Monday")
    elif day==2:
        print("Tuesday")
    elif day==3:
        print("Wednesday")
    elif day==4:
        print("Thursday")
    elif day==5:
        print("Friday")
    elif day==6:
        print("Saturday")
    elif day==7:
        print("Sunday")
    else:
        print("your number is invalid")
       
weekday()


# add two number addtion TN and RN
def add():
    print("Enter two number")
    a=int(input())
    b=int(input())
    c=a+b
    print("sum is :",c)
add()



#Multiple TS and RN
def mul(a,b):
    
    c=a*b
    print("Multiplication is :",c)
mul(8,9)




#Divition TN and RS
def division():
    print("Enter two number")
    a=int(input())
    b=int(input())
    c=a/b
    return c
div=division()
print("divition : ",div)



#subtraction Ts and RS
def sub(a,b):
    c=a-b
    return c
s=sub(8,4)
print("subtraction : ",s)