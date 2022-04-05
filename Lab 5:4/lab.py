#### fix the following errors!

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list[my_list_len-1])

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z.append('d')

#5 why does the x not display 10, followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
fav_color='Turquoise'
color = 'My favorite color is {}, what is yours?'.format(fav_color)
print(color)

#### answer the following questions without changing the code given

#7 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
temp=[]
for x in schools:
    if x not in temp:
        temp.append(x) 

print(temp)

schools = ['harris', 'booth', 'crown', 'harris', 'harris']
print(set(schools))

#8 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals=list(animals)
animals[2]='cat'
print(animals)

#9 make this string take a name based on a variable (you can modify the code on this one)
name=input('Enter your name: ')
welcome = 'Hello {}, and welcome to Data and Programming!'.format(name)
print(welcome)

#10 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'
my_sent=my_sent.lower().split()
print(my_sent)

