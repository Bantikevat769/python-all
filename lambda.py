def add(a,b):
 return a+b
print(id(add))

b=add(3,8)
print(id(b))
print(b)
  
#lambda a,b : a+b
k=(lambda a,b:a+b)(3,5) #only simple one time using 
print(k)