message = "hello there world"
print(message)
print(message.capitalize())
print(message.upper())

myNumberForDebug = 10
5
myNumberForDebug += 5

x = 5
#x = int(input("Please enter in a number!"))
if (x < 0):
    print("negative!")
elif (x == 0):
    print("zero!")
else:
    print("positive!")

#some list examples
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(letters[2:5])
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

words = ['cat', 'snake', 'dog', 'elephant']
print(words)
for w in words:
    print(w)

#the slice notation creates a copy of the list
for w in words[:]:
    print(w)
    words.remove(w)

print(words)
#using the slice before is preferred, so the iteration works. Otherwise you interfere with what you're looping through

#range function generates arithmetic progressions
#range works in a start, stop, step syntax
myRange = range(5) 
for i in myRange: #this will print from 0 to 4
    print(i)

for i in range(5, 50, 7): #start at 5, stop at 100, go up in 7s
    print(i)
#print(myRange) - ranges are iterable, you cannot just print, it's a target for functions etc. to iterate over

print(range(5))
print(list(range(5)))

#create a loop to print out prime numbers
#this involves 2 loops, for each number see if it has any factors
#NOTE THE ELSE STATEMENT ON THE FOR LOOP FOR WHEN IT DOESN't BREAK!
for i in range(2, 50):
    for x in range(2, i):
        if (i % x == 0):
            break #we found a factor so this ain't a prime
    else:
        #loop has fallen through it's a prime!
        print(i, ' is a prime number')

