
from sys import argv
print("############## start of exercise 13 parameters, unpacking, variables ###############")

script, first, second, third = argv

print("script name:", script)
print("first variable:", first)
print("second variable:", second)
print("third variable:", third)

third = input("you entered {} for the 3rd value, please enter another".format(third) )

print("third variable:", third)


#note need to run the script like this
#python c:/Users/malco/dev/github/python101/learnPythonHardWay/ex13-x.py 1 2 3

#so the script name itself is always the first command line arg
