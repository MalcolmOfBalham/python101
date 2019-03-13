#exercise 18 functions and variables

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} arg2:{arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} arg2:{arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print(f"no args")


#exercise 19 functions and variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses")
    print(f"you have {boxes_of_crackers} boxes")





#execute ex 18 stuff
print_two(1, 2)
print_two_again("one", "two")
print_one("just one")
print_none()

#execute ex19 stuff
print("just give numbers to the function")
cheese_and_crackers(5, 2)

print("or use variables")
num_cheeses = 10
num_boxes_crackers = 3
cheese_and_crackers(num_cheeses, num_boxes_crackers)

print("combine with maths operations")
cheese_and_crackers(num_cheeses*2, num_boxes_crackers*10)

