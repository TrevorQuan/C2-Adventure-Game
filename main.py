import random
import time
print("Welcome to Minecraft Speedrunners VS Hunters, The Choice Game!")
print("The rules are simple avoid the hunters, get to The End, and beat the ender dragon...")
print("You will have 4 choices to choose from, Eat, Run, Status Check, and Collect Resources.")
print("e = Eat")
print("t = Travel")
print("r = Collect Resources")
print("s = Status Check")
print("q = Quit")
print("When you put in your choice, put the letter that corresponds to the choice(above).")
print("There will be warnings when something bad might happen. Be on a lookout for them, they are important.")
print("GOODLUCK!")
print(" ")
e = ("Eat")
t = ("Travel")
r = ("Collect Resources")
s = ("Status Check")
q = ("Quit")
hunterDistance = 0
userDistance = 35
hungerBar = 10
userResources = 0
userFood = 5


userName = input("What is your UserName, type here: ")
userReady = input("Are You Ready? Enter 'r' if ready: ")
startTime = time.time()
userAction = input("Pick a Choice(Type EXACTLY What You Want To Do): ")
while(True):
  #userInput Check
  if (userAction == 'e'):
    if (userFood != 0):
      print() 
      print("You are eating your given steak. You up your hunger-bar.")
      hungerBar += 4
      userFood -= 1
    else:
      print()
      print("You are all out of food.")
        # Printing Options again... User Choice
    print(" ")
    print("Choices:")
    print(e)
    print(t)
    print(r)
    print(s)
    print(q)
    userAction = input("Pick a Choice(Type EXACTLY What You Want To Do): ")
  if (userAction == 't'):
    Travel = random.randint(12,17)
    userDistance += Travel
    hunterTravel = random.randint(6,12)
    hunterDistance += hunterTravel
    hungerBar -= random.randint(1,2)
    print()
    print("You have traveled " + str(Travel) + " chunks.")
        # Printing Options again... User Choice
    print(" ")
    print("Choices:")
    print(e)
    print(t)
    print(r)
    print(s)
    print(q)
    userAction = input("Pick a Choice(Type EXACTLY What You Want To Do): ")
  if (userAction == 'r'):
    getResource = random.randint(7,10)
    userResources += getResource
    print()
    print("You collected " + str(getResource) + " resources.")
    hunterTravel = random.randint(6,14)
    hunterDistance += hunterTravel
        # Printing Options again... User Choice
    print(" ")
    print("Choices:")
    print(e)
    print(t)
    print(r)
    print(s)
    print(q)
    userAction = input("Pick a Choice(Type EXACTLY What You Want To Do): ")
  if (userAction == 's'):
    print()
    print("The Hunters are " + str(userDistance - hunterDistance) + " chunks behind you.")
    print("Your hunger-bar is at " + str(hungerBar) + ".")
    print("You have " + str(userResources) + " resources.")
    print("You have traveled " + str(userDistance) + " chunks.")
    print("You have " + str(userFood) + " pieces of food left.")
    print(" ")
        # Printing Options again... User Choice
    print(" ")
    print("Choices:")
    print(e)
    print(t)
    print(r)
    print(s)
    print(q)
    userAction = input("Pick a Choice(Type EXACTLY What You Want To Do): ")
  if (userAction == 'q'):
    print()
    print("You have quit the game.")
    break

  #Win
  if(userDistance >= 225 and userResources >= 45):
    print()
    print("Congrats, " + userName + ", you reached The End and defeated the Ender Dragon!")
    endTime = time.time()
    print("You beat Minecraft with hunters on your tail in: " + str(endTime-startTime) + " seconds!")
    break
  
  #Lose
  if(hunterDistance >= userDistance):
    print()
    print("The hunters have caught up to you and you can't take them down... you lost, GAME OVER.")
    break
  if(userDistance >= 225 and userResources <= 44):
    print()
    print("You made it to The End, BUT you don't have enough resources so you have been slayed by the ender dragon... GAME OVER.")
    break
  if (hungerBar <= -1):
    print()
    print("You starved to death... GAME OVER.")
    break

  #Warning
  if(userDistance - hunterDistance <= 20):
    print()
    print("The hunters are near... HURRY!")
  if(hungerBar <= 4):
    print()
    print("Your getting hungry, better eat or you'll starve.")