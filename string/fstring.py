#f-Strings
language = "Python"
school = "alpain"
print(f"I'm learning {language} from {school}.")

#number
num1 = 83
num2 = 9
print(f"The product of {num1} and {num2} is {num1 * num2}.")


#fstring conditional 
num =int(input("Enter a number"))
print(f"Is num even? {True if num%2==0 else False}")


#Call Methods with Python f-Strings

author = "jane smith"
print(f"This is a book by {author}.")


#Call Functions Inside Python f-Strings
def choice(c):
  if c%2 ==0:
    return "Learn Python!"
  else:
    return "Learn JavaScript!"
