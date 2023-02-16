# #sort(): Sorts the list in ascending order.
a=[55,63,2,4,8,9,71]
a.sort()
print("sorting: ",a)
# type(list): It returns the class type of an object.
fam = ["abs", 1.57, "egfrma", 1.768, "mom", 1.71, "dad"]
print(type(fam))


#append(): Adds one element to a list.
months = ['January', 'February', 'March'] 
months.append('April') 
print("appending: ",months)
# extend(): Adds multiple elements to a list.
list = [1, 2, 3] 
list.extend([4, 5, 6]) 
print("extend : ",list)
# index(): Returns the first appearance of a particular value.
months = ['January', 'February', 'March', 'April', 'May'] 
print("indexing: ",months.index('March'))
# max(list): It returns an item from the list with a max value.
prices = [589, 237, 230, 463, 42] 
price_max = max(prices) 
print("maximum: ",price_max)
# min(list): It returns an item from the list with a min value.
prices = [589, 237, 230, 463, 42] 
price_min = min(prices) 
print("minimum : ",price_min)
# len(list): It gives the overall length of the list.
list_1 = [50.29] 
list_2 = [76.14, 89.64, 167.28] 
print('list_1 length is ', len(list_1)) 
print('list_2 length is ', len(list_2))
# clear(): Removes all the elements from the list.
months = ['January', 'February', 'March', 'April', 'May'] 
print("clear",months.clear())
# insert(): Adds a component at the required position.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(2, "pineapple")
print("inserting",fruits)
# count(): Returns the number of elements with the required value.
fruits = ['apple', 'banana', 'cherry']
print("counting:",fruits.count("apple"))
# pop(): Removes the element at the required position.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(0)
print("pop",fruits)
# remove(): Removes the primary item with the desired value.
fruits = ['apple', 'banana', 'cherry']
fruits.remove("cherry")
print("remove",fruits)
# reverse(): Reverses the order of the list.
fruits = ['apple', 'banana', 'cherry', 'orange', 'pineapple']
fruits.reverse()
print("reversing: ",fruits)
# copy():  Returns a duplicate of the list.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print("original:",fruits)
print("copy : ",x)