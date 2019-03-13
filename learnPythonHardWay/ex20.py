from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(f, line_count):
    print(line_count, f.readline())


#now the commands to execute the functions above
current_file = open(input_file)

print("Print the whole file\n")
print_all(current_file)

print("now rewind")
rewind(current_file)

print("now print 3 lines")

current_line = 1
print_a_line(current_file, current_line)
current_line += 1
print_a_line(current_file, current_line)
current_line += 1
print_a_line(current_file, current_line)

