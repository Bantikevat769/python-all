from functools import reduce
def add(x,y):
      return x+y
num=[5,6,3,8,4,2]

print("sum all value = ",reduce(add,num))




from functools import reduce

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)




from functools import reduce

scores = [75, 65, 180, 95, 50]

total = reduce(lambda a, b: a + b, scores)

print(total)
