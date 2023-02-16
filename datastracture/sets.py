print("======= Add funtion using  is sets ========")
lang={ 'python','java','c++','c'}
lang.add('pHp')
print(lang)
print("======== C  lear funtion using  is sets=========== ")
lang={ 'python','java','c++','c'}
lang.clear()
print(lang)
print("=========== Difference funtion using  is sets ============ ")
num1={1,2,2,6,3,4,5}
num2={4,5,6,7,9,8,8}
num1.difference(num2)
num2.difference(num1)
print(num1,num2)
print("============= Copy funtion using  is sets ============== ")
lang={ 'python','java','c++','c'}
lang2=lang.copy()
print("Original set:",lang)
print("copy set:",lang2)
print("============== Discard funtion using  is sets ============== ")
lang={'python','java','c++','c','php','r'}
lang.discard('php')
print(lang)
print("=============== clear funtion using  is sets =================") 
lang={ 'python','java','c++','c'}
lang.clear()
print(lang)
print("================== Pop funtion using  is sets =================") 
lang={ 'python','java','c++','c'}
lang.pop()
print(lang)
print('================== Remove funtion using  is sets ================') 
lang={ 'python','java','c++','c'}
lang.remove('python')
print(lang)
lang={()}

print(type(lang))