import sys
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
try:
    div=num1/num
    print("distion", div) #acording to change this type error than show massage 
except:
    print(sys.exc_info ()[0])#lass 'ZeroDivisionError'
    print(sys.exc_info ()[1])#division by zero
    
