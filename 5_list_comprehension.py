mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
mylist = [letter for letter in mystring]
mylist = [x for x in 'word']
mylist = [x**2 for x in range(0,11)]
mylist = [x**2 for x in range(0,11) if x%2==0] 
mylist
C = [0,10,20,34.5]
F = [( (9/5)*temp + 32)for temp in C]
F = []
for temp in C:
    F.append(()(9/5)*temp + 332)

result = [x if x%2==0 else 'odd' for x in range (0,11)]

mylist = []
for x in [2,4,6]:
    for y in [1,100,200,300]:
        mylist.append(x*y)

mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
















































































