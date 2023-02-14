#third method is 
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
try:
    div=num1/num2
    print("distion", div)
except ZeroDivisionError as  ze: #ZeroDivisionError is builtin class
    print(ze.__class__)# all error is built in class 
    print(ze)
except NameError as ne:
    print(ne.__class__) # print is class type
    print(ne) # information is print 





#second method is  try except
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
try:
    div=num1/num2
    print("distion", div)
except:#single error find
    print("this is error")
else:
    print("an exception didn't occure")
finally:
    print("this is always run")








# simple method
# num1=int(input("Enter a number"))
# num2=int(input("Enter a number"))
# try:
#     div=num1/num2
#     print("distion", div)
# except (ValueError,ZeroDivisionError,NameError): #multiple error used but , sepretor but only same massage print

#     print("this is error")


