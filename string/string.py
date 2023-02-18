str="banti  kevat"
str.capitalize()
print("capitalize :",str)#Returns a capitalized string.

str.casefold()
print("casefold:",str)#Returns the lower case string.
#str.find(substr, start, end)
print("find funtion",str.find('k'))
# substr: (Required) The substring whose index has to be found.
# start: (Optional) The starting index position from where the searching should start in the string. Default is 0.
# end: (Optional) The ending index position untill the searching should happen. Default is end of the string.
print("index funtion",str.index('k'))


#isalnum() using  characters and alphanumeric 
mystr = 'Hello123'
print(mystr.isalnum())

mystr = '12345'
print(mystr.isalnum())

mystr = 'mynameis'
print(mystr.isalnum())

#String join() Method
sep = ','
names = ['Steve', 'Bill', 'Ravi', 'Jonathan'] # list
print(sep.join(names))

mystr = 'Hello' # string
print(sep.join(mystr))

nums = ('1', '2', '3', '4') # tuple
print(sep.join(nums))

langs = {'Python', 'C#', 'Java', 'C++'} # set
print(sep.join(langs))

#String replace() Method

mystr = 'Hello World!'
print(mystr.replace('Hello','Hi'))




#String split() Method
mystr = 'Hello World'
print(mystr.split())

print('Hello     World'.split())
print('Hello\tWorld'.split())
print('Hello\nWorld'.split())
print('Hello\u2028World'.split())


#String strip() Method
mystr = '     Hello World     '
print( mystr.strip() )

mystr = '''
Python is 
a programming language'''
print( mystr.strip() )
mystr = '----Hello World----'
print(mystr.strip('-')  )

