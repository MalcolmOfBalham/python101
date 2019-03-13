from sys import argv

script, filename = argv
print(f"we're going to erase filename {filename}")
print("if you don't want that, press ctrl+c, else press return")

input("?")

print("opening the file...")

#note this doesn't fail if the file doesn't exist... maybe would if reading?
target = open(filename, "w")

print("Trucating it...")
#note that opening a file with 'w' truncates it anyway.. as not for appending
target.truncate()

print("now need 3 lines from you:")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

# target.write(line1 + "\n")
# target.write(line2 + "\n")
# target.write(line3 + "\n")

target.write(f"{line1}\n{line2}\n{line3}\n" )

target.close()
