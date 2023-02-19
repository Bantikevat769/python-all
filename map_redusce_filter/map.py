#map function using
def square(n):
    return n*n
my_list=[7,8,6,2,5,2]
p=map(square,my_list)
print(list(p))


#round function with map function

my=[2.5362,3.5978,8.9586, 9.8526]
p=map(round,my)
print(list(p))


#map funtion using list number

def multi(n):
    return n*10
my_list=[7,8,6,2,5,2]
p=map(multi,my_list)
print(list(p))