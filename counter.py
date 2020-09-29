from collections import Counter

l = [1,1,1,2,3,3,4,5,6,7,7,8,9,10]

print(Counter(l))

s =  'assssssdasewsadccserdfhhhh'

print(Counter(s))

sentence = 'This is my sentence'
words = sentence.split()
c =  Counter(words)

print(c)