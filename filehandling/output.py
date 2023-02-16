from posixpath import split


print("***********:Text file : ***************")
# text file
# deep=open("banti.txt",'w')
# print("file name is : ",deep.name)
# print('''my name is banti kevat
#  i am from guna distic..........''')
# deep.close()
print("***********:Read fuction : ***************")
# read function using text file  read
f = open("banti.txt", 'r')
p = f.read(20)  # size using according print character
s = f.read(-1)  # again print same file
print(p)
print(s)
f.close()
print("***********:Readline  function : ***************")
# readline function single line read
f = open("banti.txt", 'r')
p = f.readline()  # full line read
t = f.readline(2)  # size : number of character  to read from line
print("readline function:", p, end="")
print("readline charcter :", t)
f.close()
print("***********:Readlines  function : ***************")
# readline function list formate line read
f = open("banti.txt", 'r')
p = f.readlines()  # print .list
print("simple", p)
for line in p:  # for loop help
    print(line)
f.close()
print("***********:Tell()function : ***************")
# tell() using current indexing
f = open("banti.txt", 'r')
p = f.tell()  # tell ()
print("starting index :", f.tell())
p = f.read(8)
print("tell:", p)
print(" read indexing is :", f.tell())
f.close()
print("***********:Seek()function : ***************")
# Seek() using current indexing
f = open("banti.txt", 'r')
print(f.tell())  # staring 0 position
print(f.read(5))  # read 5 charecter
print(f.seek(2))  # change index positin
print(f.read())  # read all character
f.close()
print("***********:Text mode : ***************")
# text mode
f = open("banti.txt", 'r')
p = f.read()
print(p, end="")  # empty line remove with the help of end=""
f.close()
print("***********:Bainary mode : ***************")
# bainary mode
f = open("banti.txt", mode='rb')
p = f.read()
print(p)
f.close()
print("***********:line count: ***************")
# simple line ccount this file
f = open("banti.txt",mode="r")
li = 0
char = 0
word = 0
for line in f:
    li+=1
    # line = line.strip("\n")
    # char += len(line)
    # lis = line.split()
    # word += len(lis)
f.close()
print("lines count : ",li)
# print("number of  charecter: ",char)
# print("count number of word",word)
print("***********:write function: ***************")
f=open("banti.txt" ,mode="w")
f.write("my name is rahul kevatand \nmy freind name is khishi chimli")
f.write("hi dear ")
f.close()