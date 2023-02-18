 #table print any number
a=int(input("Enter any number"))
for i in range(1,11):
    print(a, "*" ,i,"=",i*a)



#sum of natural number
a=int(input("Enter any number"))
sum=0
for i in range(1,a+1):
    print(i)
    sum=sum+i
print("total number is ",sum)