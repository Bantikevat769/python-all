#raise  method using for python
try:

    age =int(input("Enter your age is :"))
    if age <0:
      raise ValueError("invalid age ") # raise kyeword use according to you used error massage
    print("your age is :",age)
except ValueError as ve:# ve is value error is alis
    print(ve)

print("rest of code") # raise keyword use any exception used particular condition 
