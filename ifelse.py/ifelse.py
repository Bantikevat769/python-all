#If Else with condition true
a = 2
b = 4
if a<b:
	print(a, 'is less than', b)
else:
	print(a, 'is not less than', b)



#If Else with condition r flase
a = 5
b = 4

if a<b:
	print(a, 'is less than', b)
else:
	print(a, 'is not less than', b)

#Nested If Else
a = 2
b = 4
c = 5

if a<b:
	print(a, 'is less than', b)
	if c<b:
		print(c, 'is less than', b)
	else:
		print(c, 'is not less than', b)
else:
	print(a, 'is not less than', b)

#If Statement with AND Operator
a = 5
b = 2

#nested if
if a==5:
	if b>0:
		print('a is 5 and',b,'is greater than zero.')
		
#or you can combine the conditions as
if a==5 and b>0:
	print('a is 5 and',b,'is greater than zero.')

#elif Statement with AND Operator
a = 8

if a<0:
	print('a is less than zero.')
elif a>0 and a<8:
	print('a is in (0,8)')
elif a>7 and a<15:
	print('a is in (7,15)')



# even and old number
a=int(input("Enter any number"))
if a%2==0:
    print("Even" )
else:
    print("old")




#positive and negetive and zeero
a=int(input("Enter any number"))
if a>0:
    print("Positive" )
elif a==0:
    print("Number is zero  ")
else:
    print("negetive")

# find grater than 
a=int(input("Enter any number"))
b=int(input("Enter any number"))
c=int(input("Enter a number"))
if a>b and a>c:
    print("a is grater  ")
elif b>a and b>c:
    print("b is grater ")
elif c>a and c>b:
    print("c is grater ") 
