def has_33(num):
      for i in range(0,len(num)-1):
          if num[i:i+2] == [3,3]:
              return True
    
      return False

print(has_33([1, 3, 1, 3]))

def paper_doll(text):
      result = ''

      for char in text:
              result += char*3
              return result
print('hello')
print('yes')

def blackjack(a,b,c):

      if sum ([a,b,c]) <= 21:
          return sum([a,b,c])
      elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
          return sum([a,b,c])-10
      else:
          return 'BUSTED'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(6,4,5))

def summer_69(arg):

     total = 0
     add = True

     for num in arg:
         while add:
             if num!= 6:
                 total += num
                 break
             else:
                 add = False
         while not add:
             if num != 9:
                 break
             else:
                 add = True
                 break
     return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))













































































































































































































































































