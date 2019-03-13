#start of exercise 5

my_name = 'whoever'
my_age = 101 #old
my_height = 205
my_weight = 99


print(f"age: {my_age}")
print(f"height: {my_height}")
print(f"weight: {my_weight}")

#can put expressions in there too
print(f"weight in pounds: {my_weight * 2.2046}")

total = my_age + my_height + my_weight

print(f"sum of {my_age}, {my_height} and {my_weight} should be {total}")

#end of exercise 5 / start of 6

types_of_people = 10

#note that the formatted string is nothing to do with the print command...
#..so can have a formatted string set up ahead of multiple processing
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of a..."
e = "A string with a right side"
print(w + e)

print("######end of exercise 6, start of 7########")

print("Mary had a little lamb")
print("Its fleece was white as {}".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
#"end" just appends to the end. 
print(end1 + end2 + end3 + end4 + end5 + end6, end='   ')
print(end7 + end8 + end9 + end10 + end11 + end12)


print("######end of exercise 7, start of 8########")

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))

print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format("here's",
"a version",
"over",
"multiple lines"))

