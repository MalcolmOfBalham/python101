from sys import argv


print("############## start of exercise 15 reading files ###############")

script, filename = argv
txt = open(filename)
print(f"here's your filename {filename}:")
print(txt.read())

print("type the filename again:")
file_again = input("> ")
txt = open(file_again)
print(txt.read())

txt.

#to run:

# print("############## start of exercise 14 prompting and passing ###############")
