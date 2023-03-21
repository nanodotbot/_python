#some hearts to change the world
codecademy_cheatsheet = 'https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-syntax/cheatsheet'
official_python_tutorial = 'https://docs.python.org/3.8/tutorial/index.html'
"""
multi-line
comments
"""

#print
print (codecademy_cheatsheet)
print (official_python_tutorial)
print('"There is something at work in my soul, which I do not understand."')
print('\'single quotes within single quotes\'')


#variables
some_meows = 5 + 5
some_meows = 'meowmeow meow'
print(some_meows)

# a = 'abc&xyz'  # string
# b = 3.16  #float
# c = {2:'a', 3:'b'}  # dictionary
# d = 6 < 2  # boolean
# e = [1,2,3,4,5] # list
# f = sum(e)  # value returned from a function
# g = sum # a function

# for obj in [a,b,c,d,e,f,g]:
#     print(obj)

a_string = 'some text'
an_integer = 1
a_float = 2.1

print('https://docs.python.org/3/tutorial/floatingpoint.html')
print(4*(an_integer + a_float)/2)
print('https://en.wikipedia.org/wiki/Order_of_operations')
print(2**2**2)
print(29%5)
print(a_string + 2*(' ' + a_string))


#errors
print('NameError and SyntaxError')
print('ZeroDivisionError')


#concatenation
the_con_cat = some_meows + ': ' + str(a_float)
print(the_con_cat)
print(some_meows, ':', a_float)


#plus equals
the_con_cat += ', and another meow'
print(the_con_cat)
a_float += an_integer + 1.4
print(a_float)


#multi-line strings
sonnet_130 = '''
My mistress’ eyes are nothing like the sun;
Coral is far more red than her lips’ red;
If snow be white, why then her breasts are dun;
If hairs be wires, black wires grow on her head.
I have seen roses damasked, red and white,
But no such roses see I in her cheeks;
And in some perfumes is there more delight
Than in the breath that from my mistress reeks.
I love to hear her speak, yet well I know
That music hath a far more pleasing sound;
I grant I never saw a goddess go;
My mistress when she walks treads on the ground.
And yet, by heaven, I think my love as rare
As any she belied with false compare.
'''
print(sonnet_130)


#review

print('https://www.youtube.com/watch?v=r5kfkpYtOiw')
print('https://www.youtube.com/watch?v=hpn8MPHOpDo')


#input
# what_she_likes = input('What do you like?')
# print(what_she_likes)



#functions
print('https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-functions/cheatsheet')

def get_and_print(parameter1, parameter2='default text'):
    info = 'meow'
    return parameter1 + ' ' + parameter2, info

return_value1, return_value2 = get_and_print(a_string)
print(return_value1, return_value2)



#control flow

print('https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-control-flow/cheatsheet')


#boolean variables

cat_bool1 = not True == False #True
print(type(cat_bool1))
cat_bool2 = not False == (9 != 8) #True
cat_bool3 = not (7 >= 7) #False

print(cat_bool1)
print(cat_bool2)
print(cat_bool3)


#if if - conditional statements

def cond_stat1(cond1, cond2):
    if cond1:
        print('cond1')
    if cond2:
        print('cond2')

cond_stat1(cat_bool1, cat_bool2)

#else if - conditional statements

def cond_stat2(cond1, cond2, cond3):
    if cond1 or cond3: #False
        return True
    elif not cond2 and not cond3: #True
        return True
    else:
        return False

print(cond_stat2(cat_bool1, cat_bool2, cat_bool3))


#try except - error control

def just_a_test(a, b):
    try:
        print(a/b)
        return a/b
    except ZeroDivisionError:
        print('outch, ZeroDivisionError')

just_a_test(1, 0)

def raise_value_error():
    raise ValueError

try:
    raise_value_error()
except ValueError:
    print('successfully raised ValueError')



#lists

print('https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-lists/cheatsheet')

nano_list = ['l-string', 23, True, the_con_cat]

print(nano_list)

lists_within_lists = [['athena', 23], ['apollo', 43], ['artemis', 31]]


#zip

names_list = ['athena', 'apollo', 'artemis']
ages_list = [23, 43, 31]

zipped_lists = zip(names_list, ages_list) #creates an object with key-value pairs

print(zipped_lists) #prints the location of the object in memory
print(list(zipped_lists)) #converts the object to a list and prints it

zipped_lists = list(zip(names_list, ages_list)) #before, zipped_lists contained the location only
print(zipped_lists)

#append

nano_list.append(an_integer)
nano_list.append(a_float)
print(nano_list)

zipped_lists.append(('nike', 34))
print(zipped_lists)

#plus (+)

nano_list = nano_list + ['just some', 'new items', 3] + ages_list
print(nano_list)

#range

nano_range = range(10) #object of type 'list'
print(nano_range)
nano_range = list(nano_range) #now it's a list
print(nano_range)

nano_range = list(range(1, 11, 2))
print(nano_range)


#length
nano_list_length = len(nano_list)
print(nano_list_length)

#index
nano_list_index_3 = nano_list[3]
print(nano_list_index_3)

#selecting an element that does not exist produces an IndexError

print(nano_list[-1]) #selects and prints the last item of the list

#slice
nano_list = nano_list[0:3] + nano_list[6:7] + nano_list[9:]
print(nano_list)

nano_list = nano_list[:-1]
print(nano_list)

nano_list = nano_list[-6:]
print(nano_list)

#count
print(nano_list.count('l-string'))
print(nano_list.count(23))
print(nano_list.count('notpartofthelist'))

#sort
#print(nano_list.sort()) #TypeError: '<' not supported between instances of 'int' and 'str'
print(names_list.sort()) #none
sorted_ages = ages_list.sort()
print(sorted_ages) #.sort() modifies the original list and returns None
print(names_list)
print(ages_list)
names_list.sort(reverse=True)
print(names_list)

#sorted
numbers_list = [3, 2, 4, 5, 7, 1, 6]
sorted_numbers = sorted(numbers_list)
print(sorted_numbers)
print(numbers_list)
numbers_list.sort()
print(numbers_list)


#tuple

nano_tuple = ('nada', 'none of this can be changed', 42) #a tuple is an immutable object

def change_tuple(tuple):
    try:
        tuple[1] = 'everything can be changed' #TypeError
        return tuple
    except TypeError:
        return tuple

print(change_tuple(nano_tuple))

#unpacking a tuple
nano_name, nano_info, nano_number = nano_tuple

print(nano_name)
print(nano_info)
print(nano_number)


print(nano_list)
nano1, nano2, nano3, nano4, nano5, nano6 = nano_list
print(nano1)


another_variable = (42)
one_element_tuple = (42,)



#loops

print('https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-loops/cheatsheet')


#for loop

for nano in nano_list:
    print(nano)

for i in range(3):
    print('This will be printed three times')

#infinite loop
#ctrl + c

#break

for nano in nano_list:
    print(nano)
    if nano == 'l-string':
        break

#continue

for nano in nano_list:
    if nano == 23:
        continue
    print(nano)


#while
nada_list = []

while len(nada_list) < 3:
    nano = nano_list.pop()
    nada_list.append(nano)

print(nada_list)
print(nano_list)

nada_list = []
i = 0

while len(nada_list) < 3:
    nada_list.append(nano_list[i])
    i += 1

print(nada_list)
print(nano_list)


#nested loops

nested_list = [['a', 'dream'],['whithin'],['a', 'dream']]

for dream in nested_list:
    for whithin in dream:
        print(whithin)


#list comprehensions

nano_russia = ['maria', 'anastasia', 'alexei', 'tatjana', 'olga']
a_russia = []

for princess in nano_russia:
    if princess[0] == 'a':
        a_russia.append(princess)

print(a_russia)

m_russia = [princess for princess in nano_russia if princess[0] == 'm']

print(m_russia)

all_russia = [princess for princess in nano_russia]

print(all_russia)

all_russia_titles = ['duchess ' + person if person != 'alexei' else 'tsarevich ' + person for person in nano_russia]

print(all_russia_titles)

def add_title(name):
    if name != 'alexei':
        return 'duchess ' + name
    else:
        return 'tsarevich ' + name

all_russia_titles = [add_title(person) for person in all_russia]

print(all_russia_titles)

print('what we do in life\nechoes in eternity')

print('developer documentation: https://www.youtube.com/watch?v=s1PLS3SQHQ0')


#global

some_global = 0
def get_the_global(lst):
    global some_global
    while lst[some_global] % 2 == 0:
        print(lst[some_global])
        some_global += 1
        if some_global == len(lst):
            break
get_the_global([2, 6, 4])


print('difficult excercises:')
print('Code Challenge: Loops')
print('delete starting even numbers\nodd indices')

print('https://www.codecademy.com/articles/how-to-use-jupyter-notebooks')

print('https://jupyter.readthedocs.io/en/latest/')
print('https://jupyter.org/try')

print('C:\\nano\\glx\\prox\\_python\\Reggie\'s+Linear+Regression')



# Project: Linear Regression

def get_y(m, b, x):
    return m*x + b

# print(get_y(1, 0, 7) == 7)
# print(get_y(5, 10, 3) == 25)

def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y = get_y(m, b, x_point)
    return abs(y - y_point)

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
# print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
# print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
# print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
# print(calculate_error(-1, 1, (3, 3)))

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def calculate_all_error(m, b, data):
    total = 0
    for point in data:
        error = calculate_error(m, b, point)
        total += error
    return total

# print(calculate_all_error(1, 0, datapoints))

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))

#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

print('here we are')

#finding floppy
rabbit_names = ['algernon', 'floppy', 'fober']
print('looking for floppy...')
for item in rabbit_names:
    if item == 'floppy':
        print('found him!')
        break
print('end of search.')

for rabbit in rabbit_names:
    if rabbit == 'algernon':
        continue
    print(rabbit)

# functions

rabbit1, rabbit2, rabbit3 = rabbit_names

def greet_rabbits(rabbit1, rabbit2, rabbit3):
    greeting1 = 'hello ' + rabbit1
    greeting2 = 'hi ' + rabbit2
    greeting3 = 'meow ' + rabbit3
    return greeting1, greeting2, greeting3

greeting1, greeting2, greeting3 = greet_rabbits(rabbit1, rabbit2, rabbit3)

print(greeting1, greeting2, greeting3)