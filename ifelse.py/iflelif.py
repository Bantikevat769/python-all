# day is print input fuction 
day=int(input("Enter number"))
if(day==1):
    print("Sunday")
elif(day==2):
    print("Monday")
elif(day==3):
    print("Tuesday")
elif(day==4):
    print("Wednesday")
elif(day==5):
    print("Thursday")
elif(day==6):
    print("Friday")
elif(day==7):
    print("Saturday")
elif(day<=0 or day>=8):
    print("No day in list")






# traffic light single program
light = input("Enter your color light single : ")
if light == 'Red' or light == 'red':
    print("car is stop")
elif light == 'Green'or light == 'green':
    print("car is go")
elif light == 'Yellow' or light == 'yellow':
    print("car is wait ")
else:
    print(" your colar is not match")
