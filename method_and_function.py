import secrets


# mylist = [1,2,3]
# mylist.append(4)
# mylist.pop
# help(mylist.insert)

# def name_of_function(name):
#     '''
#     docstring explain function
#     '''
#     print('hello '+name)

# name_of_function('joe')

# def add_function(num1,num2):
#     return num1+num2

# result = add_function(1,2)
# print(result)

# def name_function():
#     '''
#     docstring: info about the function
#     input: no input ...
#     output: hello ..
#     '''
#     print('hello')
# help(name_function())

# def say_hello(name='NAME'):
#     return'hello '+name
#result = say_hello('zach')


# def add(n1,n2):
#     return n1+n2

# result = add(20,30)
# print(result)

# find out if the word dog is in a string
# def dog_check(mystring):
#     return 'dog' in mystring.lower()

# print(dog_check('Dog ran away'))

# 'dog' in 'dog ran away'

def pig_latin(word):

    first_letter = word[0] 

    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

        return pig_word

print(pig_latin('apple'))




























































