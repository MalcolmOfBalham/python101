from sys import argv

print("############## start of exercise 14 prompting and passing ###############")

script, user_name = argv
prompt = '> '
print(f"Hi {user_name}, I'm the {script} script")
print("i'd like to ask a few questions")

print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
ok so you said {likes} about liking me.
you livein {lives}.
and you have a {computer} computer.
""")


# to run 
#  python c:/Users/malco/dev/github/python101/learnPythonHardWay/ex14.py bob
