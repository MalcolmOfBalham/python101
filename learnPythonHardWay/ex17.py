from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes")
print(f"Does the output file exist? {exists(to_file)}")

print("Ready, hit return to continue, ctrl+c to abort")
input()

#note again that by opening with "w" the file is truncatedman 
out_file = open(to_file, "w")
out_file.write(in_data)

print(f"data copied from {from_file} to {to_file}")

out_file.close()
in_file.close()

#to run
#& python c:/Users/malco/dev/github/python101/learnPythonHardWay/ex17.py ex15_sampleTextFile.txt copyFile.txt