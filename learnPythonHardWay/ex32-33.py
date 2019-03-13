#ex32 - loops and lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for loop goes through a list
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"this is fruit {fruit}")


#also can go through a mixed list
for i in change:
    print(f"i got {i}")

#build a list, starting with an empty one
elements = []

for i in range(0, 6):
    print(f"adding {i} to the list")
    elements.append(i)

#note instead of the above you could do
#elements = range(0, 6)

#and now print the elements
for i in elements:
    print(f"element was {i}")


#exercise 33 while loop stuff
def print_nums_using_while(number, increment=1):
    i = 0
    numbers = []
    while i < number:
        numbers.append(i)
        i += increment
        print(f"From inside function, bottom of loop is {i}")

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")

    numbers.append(i)
    i += 1
    print("numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("THe numbers:")

print(numbers)

for num in numbers:
    print(num)

print("from the function")
print_nums_using_while(20)