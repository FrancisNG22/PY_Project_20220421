print('item 3')
a = 10
print(a)
print(type(a))
print('\n')

print('item 4')
b = 5 + 6j
print(b)
print(type(b))
print('\n')

print('item 5')
c = True
print(c)
print(type(c))
print('\n')

print('item 6')
d = 10.5
print(d)
print(type(d))
print('\n')

print('item 7')
e = 'Testing String'
print(e)
print(type(e))
print('\n')

print('item 9')
f = ['1, 2, 3']
print(f)
print(type(f))
print('\n')

f = ['1', '2', '3']
print(f)
print(type(f))
print('\n')

f = [1, 2, 3]
print(f)
print(type(f))
print('\n')

print('item 10')
g = ('4, 5, 6')
print(g)
print(type(g))
print('\n')

g = ('4', '5', '6')
print(g)
print(type(g))
print('\n')

g = (4, 5, 6)
print(g)
print(type(g))
print('\n')

print('item 11')
h = {"Student": "Aaron"}
print(h)
print(type(h))
print('\n')

h = {'Student': 'Aaron'}
print(h)
print(type(h))
print('\n')

print('item 12')
i = {'7, 8, 9'}
print(i)
print(type(i))
print('\n')

i = {'7', '8', '9'}
print(i)
print(type(i))
print('\n')

i = {7, 8, 9}
print(i)
print(type(i))
print('\n')

print('item 13')
j = [1, 2, 3]
k = f + j
print(k)
print(type(k))
print(1 in k)
print('\n')

print('item 14')
l = (10,11, 12)
m = l + g
print(m)
print(type(m))
print('\n')

print('item 15')
#m[0] = 11  TypeError: 'tuple' object does not support item assignment
#print(m)

k[0] = 11
print(k)
print(type(k))
print('\n')

print('item 16')
n = {'Lecturer': 'Judy'}
h.update(n)
print(h)
print(type(h))
print('\n')

print('item 17')
o = {9, 10, 11}
z = (i.union(o))
print(z)
print(type(z))

o = {9, 10, 11}
z = (o.union(i))
print(z)
print(type(z))
print('\n')

o = {9, 10, 11}
z = (i.intersection(o))
print(z)
print(type(z))

o = {9, 10, 11}
z = (o.intersection(i))
print(z)
print(type(z))

print('18)')
p = {'Australia':'AU','Belgium':'BE','China':'CN','Denmark':'DK'}
print(p)
print(type(p))
country=input('Which country do you want:')
print(p.get(country))
print('\n')

print('19)')
q=['Thomas','Linda','Cath','Benny']
q.sort ()
print (q)
print('\n')
x=q.pop(0) #Benny is removed after sort
print(x)
print(q)
print('\n')
x=q.pop(0) #Cath is removed after sort
print(x)
print(q)
print('\n')
x=q.pop(0) #Linda is removed after sort
print(x)
print(q)
print('\n')
x=q.pop(0) #Thomas is removed after sort
print(x)
print(q)
print('\n')

try:
    x = q.pop(0)
except IndexError as e:
    print (e)
    print (q)
print('\n')
