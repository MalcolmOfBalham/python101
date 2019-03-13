print("############## start of exercise 9 printing printingprinting ###############")

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print("here are the days: ", days)
print("and the months: ", months)

print("""
And here is
a great big
multiline thing
"""
)

print("############## start of exercise 10 what was that ###############")

#escaping characters - example here using either single or double quotes
print("i am 6'2\" tall")
print('i am 6\'2" tall')

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


print("############## start of exercise 11 asking questions ###############")

#note commented following as is refactored in exercise 12

# print('how old are you?', end = ' ')
# age = input()

# print('how tall are you?', end = ' ' )
# height = input()

# print('how heavy are you?', end = ' ')
# weight = input()

# print(f"you're {age} years old, {height} tall and {weight} heavy")
# weight = int(weight) * 2
# print(weight)


print("############## start of exercise 12 prompting people ###############")

age = input("how old?")
height = input("how tall?")
weight = input ("how heavy?")

print(f"you're {age} years old, {height} tall and {weight} heavy")
