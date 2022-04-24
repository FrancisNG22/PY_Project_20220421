print('Step 3')
print('Single Quotes')
print("Double Quotes")
print('\n')
print('Step 4')
print('Single'+'Quotes')
print("Single"+"Quotes")
print("Single",'Quotes')
print('\n')
print('Step 5')
b = 'Quote'
print('Single %s' %b)
a = "Single"
print ('%a %a' %(a, b))
print('\n')
print('Step 6')
c = 5
print(c)
print('There are', c, 'apple in the fridge')
print('There are %d' %c, 'apple in the fridge')
print('\n')
print('Step 7')
name = input("Please enter your name: ")
print(name) #you will see the name you type in the console.
print('\n')
print('Step 8')
a = 10
b = 20
x = a + b
print(a+b)
print(x)
print('\n')
print('Step 9')
a = [1,2,3]
b = [1,2,3]
print('a is equal to b:', a==b)
print('\n')
print('Step 10')
a = 2**4
print(a)
b = pow(2,4)
print(b)
print('\n')
print('Step 11')
a = 19 / 5
b = 19 % 5
print(a)
print(b)
print('\n')
print('Step 12')
a = 10
b = 12
print('a > b is', a > b)
print('\n')
print('Step 13')
a = True
b = False
print('Combine result of x and y is', a==b)
print('Combine result of x and y is', a and b)
print('\n')
print('Step 14')
a = [1,2,3]
b = [1,2,3]
c = b
print('a is equal to b', a is b)
print('c is equal to b', c is b)