# Regular expresstion in python 

import re
nameage='''my name is Banti kevat  my age is 21
and my friend name is Khushi karihar and age 20'''
print(nameage)
age=re.findall(r'\d{1,3}',nameage)

print("ages",age)
names=re.findall(r'[A-Z][a-z]*',nameage)# findall 
print("names is : ",names)
agesdic={}#seperat data 
counts=0
for eachnmaes in names:
    agesdic[eachnmaes]=age[counts]
    counts+=1
print(agesdic)
# Regular exprestio search function using
import re
string=" my name is banti kevat and my friend  is yash mare"
if re.search('my',string):# seraching value
    print('khusi is my friend')
#total my name find
total=re.findall('my',string)
print(len(total))
import re
string="my name is banti kevat and my friend  is yash mare"
for i in re.finditer('my',string):

    lis=i.span() #cheaking indexing
    print(lis)
import re
str='sat, mat cat nat pat hat kat'# according to requrmet data print
all=re.findall('[smcnphk]at',str)#[a-z] al string print and particular data and name print
print(all)
import re
str='sat, mat cat hat pat '# according to requrmet data print
all=re.findall('[^h-m-p]at',str)# no requrment data 
print(all)
import re
str='sat, mat cat hat pat '# replace  and change 
all=re.compile('[m]at')# no requrment data
str=all.sub('chat',str)
print(str)
import re
str='''my name is banti
my age is 21
B.tech
'''# replace  and change  all code one line
all=re.compile('\n')# no requrment data
str=all.sub(' ',str)
print(str)
import re
str='123456'# replace  and change 
print("matches : ",len(re.findall('\d[6]',str)))# d only  integer number find

import re
str='123456ty'# replace  and change 
print("matches : ",len(re.findall('\D',str))) #capital d is uesd to no number only another word

import re
str='123456'# replace  and change 
print("matches : ",len(re.findall('\d[6]',str)))# d only  integer number find
a=20
b=30
print(a+b)
