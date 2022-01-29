


mylist = [1,2,3]
for num in range(0,10,2):
    print(num)
list(range(0,11,2))
word = ' abcde'
for index,letter in enumerate(word):

    print(index)
    print(letter)
    print('/n')

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2):
    print(item)
list(zip(mylist1,mylist2))

'x' in [1,2,3]

'x' in ['x','y','z']

'a' in ['a world']

'mykey' in {'mykey':345}

d = {'mykey':345}
345 in d.keys()

mylist4 = [10,20,30,40,100]
min(mylist4)
max(mylist4)

from random import randint #shuffle
mylist5 = [1,2,3,4,5,6,7,8,9,10]
#shuffle(mylist5)

randint(0,100)

rusult = int(input('fav num: '))

float(rusult) #int(rusult)































































