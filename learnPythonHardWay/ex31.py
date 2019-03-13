print("""You enter a dark room with 2 doors.
Do you go through door 1 or 2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear in here eating a cheese cake")
    print("what do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off")
    elif bear == "2":
        print("the bear eats your legs off")
    else:
        print(f"Well, doing {bear} is probably better")

elif door == "2":
    print("no way could be bothered typing this one in")
    print("good choice of door")

    