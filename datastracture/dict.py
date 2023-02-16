# clear()	Removes all items from the dictionary
bk = {1: "raja", 2: "khusi"}
 
bk.clear()
print('text =', bk)
# copy()	Returns a shallow copy of the dictionary
fruits = {"A" :'banana', 'B': 'orange'}
x = fruits.copy()
print("original:",fruits)
print("copy : ",x)
# fromkeys()	Creates a dictionary from the given sequence
seq = ('a', 'b', 'c')
print(dict.fromkeys(seq, None))
# get()	Returns the value for the given key
d = {'coding': 'good', 'thinking': 'better'}
print(d.get('coding'))
# items()	Return the list with all dictionary keys with values
dk = { 'A': 'rahul', 'B': 4, 'C': 'sonu' }
print("Dictionary item", dk.items())
# keys()	Returns a view object that displays a list of all the keys in the dictionary in order of insertion
Dictionary1 = {'A': 'antim', 'B': 'madhu', 'C': 'krisna'}
 
# Printing keys of dictionary
print(Dictionary1.keys())
# pop()	Returns and removes the element with the given key
fruits = {"A" :'banana', 'B': 'orange'}
fruits.pop("B")
print("original:",fruits)

# popitem()	Returns and removes the key-value pair from the dictionary

d = {1: '001', 2: '010', 3: '011'}
print(d.popitem())
# setdefault()	Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary
d = {'a': 97, 'b': 98, 'c': 99, 'd': 100}
# space key added using setdefault() method
d.setdefault(' ', 32)
print(d)

# update()	Updates the dictionary with the elements from another dictionary
Dictionary1 = {'A': 'BK', 'B': 'RM', }
Dictionary2 = {'B': 'banti'}
 
# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)
 
# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)
# values()	Returns a list of all the values available in a given dictionary

dictionary = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary.values())  