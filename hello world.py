print("Hello World")
f = [0,1,2,3,4,5,6,16,8]
a = 8
b = 7.5
c = 8.5
d = "The Answer is "
h = "64"
e = a + b + c
g = b + c
i = 10
j =  0
k = 'n'
l = " "
listM = ['man', 'goat', 'foolish']
N = [8, 16, 10, 9, 14, 15, 12]
f.sort(reverse=True)
print(d.rstrip() + str(e))
print(d + str(e))
print(f[-4] + f[-6] + f[-1])
print (f[-9])
print(g)
print(b + c)
print(e / a)
print(e * g)
print(int(h))
print(bool(i))
print(bool(j))
print(bool(k))
print(bool(l))
print(len(listM))
print(len(f))
print(max(f))
print(max(listM))
print(f)
f.sort()
print(f)
N.append(13)
print(N)
N.insert(3,7)
print(N)
N.pop(2)
print(N)
o = [1,3,5,7,9]
p = [2,4,6,8,10]
r = o[0] + p[0]
s = o[1] + p[1]
t = o[2] + p[2]
u = o[3] + p[3]
v = o[4] + p[4]
q = [r,s,t,u,v]
print (q)
print(d.upper())
A = ' Nsikan Abasi Ime Akpan'
B = ' Ibiono-Ibom Local Government'
C = ' Python.'
D = (f'\tMy Name Is{A}\nI am from{B}\nMy Preferred programming language is{C}.\n\tEven tho i do not have a programming language of choice')
print(D.lstrip())
print(D.strip())
print(D.rstrip())
print(D.upper())
# these are for sets 
E = {16, 'modify', 15.9, True}
# these are for tuples
F = (32, "diddy", 31.9, False)
# print sets
print(E)
# print tuples
print(F)
# print another set
G = ({'mother', 48.23, 63.9, True, 64})
# working with adding in a set
print(G)
G.add(128)
G.add('father')
print(G)
E.add(256)
print(E)
# the two ways of removing from a set using set.remove() and set.discard()
# the set.remove() pops a key error when the element can't be found.
# While the set.discard() doesn't pop the key error when the element cannot be found 
# The set.pop() does not take any arguments, it removes any arbitrary element from set. 
# the Set.pop() also works in-place but unlike other methods it returns the removed element.
G.remove(128)
print(G)
E.discard(31.9)
print(E)
P = G.pop()
print(P)
print(G)
# creating a dictionary
# also note that a dictionary must have a key which is before the column and the value is after the column
# as the syntax shows. dictionary{key1 : value1, key2 : value2} or dict({key1 : value1, key2 : value})
H = {}
print("this is an Empty dictionary: ",H)
I = dict({1 : 'Hello', 2 : 'World', 3 : '!!!'})
print(I)
# adding dictionaries
# J = { int : input('Please enter the first number ')}
# K = { int : input('Please Enter The Second Number ')}
# conclusion of adding dictionaries
# L = J + K
# print(L)
# ADVANCED PROBLEMS
# M = 250
# N = 8
# O = M / N
# if O == float():
#     print (True)
# elif H == int():
#     print (False)
# print(O)

# IF STATEMENTS BIG LESSON
age = int(input('Please Enter Your Age: '))

if age < 18:
    print('You are a minor, go and play with sand!!')
elif age >= 18 and age <= 29:
    print('You are a young adult, enjoy your youth!!')
elif age >= 30 and age <= 64:
    print('you are an adult, work hard and stay healthy!!')
elif age >=65 and age <= 120:
    print('You are a senior citizen, enjoy your golden years!!')
else:
    print('You suppose don die naaaaa!!!')
# if else statement lessons
a = int(input('input a number: '))
if a <= 4:
    print('This person is a toddler')
elif a >= 5 and a <= 12:
    print('This person is a child')
elif a >= 13 and a <= 19:
    print('This person is a teenager')
elif a >= 20 and a <= 30:
    print('This person is a young adult')
elif a >= 30 and a <= 44:
    print('This person is a adult')
elif a >= 45 and a <= 59:
    print('This person is a middle age')
elif a >= 60 and a <= 89:
    print('This person is an elder')
elif a >= 90:
    print('This person is a sage')