# Intro 
print("In the middle of the night you see an Arby's")
print("since you are always hungry you enter looking for food")
print("But you find that the door is locked and you need to find a key")

# choice 1
c1 = input("Do you choose do look in the [dumpster] or under the [floor mat]")
if "floor" in c1:
    print("You look under the floor mat and... you find the Key!")
    c2 = input("you open the door and head inside")
elif "mat" in c1:
    print("you look under the mat and... you find the Key!!")
    c2 = input("you open the door and head inside")
else:
    print("you look in the dumpster and... now your covered in trash")
    c3 = input("game over")

# Choice 2
print("you see a janitor and a cash register")
c2 = input(" do you choose to talk to the [janitor] or go to [cash register]")
if "janitor" in c2:
    print("you heard over to the janitor and... he attacks you!")
    c4 = input ("you have now entered a fight with the janitor!")
else:
    print("you steal from the register and the alarm goes off and your arrested")
    c5 = input("game over")

# choice 4
c4 = input("do you run into a [random room] or [fight janitor]?")
if "random room" in c4:
    print("you run in the room and close the door just in time and turn on the light")
    c6 = input("you see two doors")
else:
    print("you lunge at the janitor and he picks you up and throws you out the window!")
    c7 = input("game over")

# choice 6
c6 = input("you see two door with scribbled text do you go in the [right door] or the [left door]")
if "right door" in c6:
    print("you find the pantry and acquire the sandwich")
    c9 = input("Now you need a way to escape")
else:
    print("you open the door and it's a big freezer that freezes you until you are just ice")
    c8 = input("game over")

# choice 9
c9 = input("you see two windows a [cracked window] and a [drive through window] which one do you go to")
if "cracked window" in c9:
    print("you jump through the window and see the janitor throwing away trash")
    c10 = input("you've yet again entered a fight with the janitor")
else:
    print("you jump on a car and you hightail outta there")
    c15 = input("you escaped!")

# choice 10
c10 = input("do you [run] or [fight]")
if "fight" in c10:
    print("you throw hands with the janitor and you K.O him and take his keys")
    c11 = input("You don't know what the key leads to")
else:
    print("you run into the bushes and find another sandwich ")
    c12 = input("What do you do?")

# choice 11
c11 = input("Do you go through the [pantry] or the [front door]?")
if "front door" in c11:
    print("yeah that should have been obvious how else could he have entered the store")
    c15 = input("you got away with the sandwich!")
else:
    print("theres no way you thought you could leave through the pantry i'm gonna end the game cause of you")
    c13 = input("game over")

# choice 12
c12 = input("[eat] or [run]")
if "run" in c12:
    print("You run behind a Mcdonald's and escape with both sandwiches")
    print("You escaped!")
else:
    print("You eat the sandwich and the janitor picks you up and throws you in the dumpster")
    c14 = input("game over")
