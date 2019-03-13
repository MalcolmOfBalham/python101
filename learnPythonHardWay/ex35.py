#branches and functions

from sys import exit

def gold_room():
    print("this room is full of gold, how much do you take?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("dead: learn to type a number!")

    if how_much < 50:
        print("nice, not greedy, you win!")
        exit(0)
    else:
        dead("you're dead mr. greedy")


def bear_room():
    print("there's a bear in here, with honey,  in front of the door. How will you move it?")


    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("never take a bear's honey")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved! you can go through")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("don't taunt him too much!")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("invalid choice!")

def cthulhu_room():
    print("you're in Cthulu room - do you want to flee or eat your head?")

    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        cthulhu_room()  

def dead(why):
    print(why, "good job!")
    exit(0)

def start():
    print("You're in a room with a left and right door pick one")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around in the room until you starve")

start()
