lis= [1,2,3,4,5]
print(lis)
print(list[2])
print(list[5])
# negative indexing of lists
print(list[-2])
print(list[-8])
#List[Start : Stop : Stride]
list= [5,2,9,7,5,8,1,4,3]
print(list[0:6])
print(list[1:9:2])
print(list[-1:-5:-2])

#index and slice a tuple
tup=('tum', 'po', 2023,True)
print(tup)

#Positive Indexing

tuple=(5,2,9,7,5,8,1,4,3)
print(tuple[3])
print(tuple[7])
#Negative Indexing
tuple= (5,2,9,7,5,8,1,4,3)
print(tuple[-2])
print(tuple[-8])
#tuple[Start : Stop : Stride]
tuple= ('a','b','c','d','e','f','g','h','i','j')
print(tuple[0:6])
print(tuple[1:9:2])
print(tuple[-1:-5:-2])

my_tuple = ('t', 'u', 'r', 'i', 'a', 'l', 's', 'p','o', 'i', 'n', 't')
print(my_tuple[1:]) #Print elements from index 1 to end 
print(my_tuple[:2]) #Print elements from start to index 2 
print(my_tuple[5:12]) #Print elements from index 1 to index 3 
print(my_tuple[::5]) #Print elements from start to end using step size
