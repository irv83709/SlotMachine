#
# Apple/Slots Attempt 1
#
print("Welcome to the Slot Machine Simulator")
print("To win the jackpot you need to have 3 cherries in a row.")
print("You can play up to 10 rounds at once. Please select a number between 1 and 10.")
games = input("How many games would you like to run?")
slotsPossible = ("apple", "apple", "apple", "cherry", "crown", "lemon", "lemon")
losePossible = ("\nYou lose!", "\nSucker!", "\nThanks for the money chump!, "\n¯\_(ツ)_/¯")
from random import *
if int(games)<1 :
    print ("Well, you didn't deserve to play anyway!")
if int(games)>10 :
    print ("Sorry you can only play 10 games so 10 is all you get!")
    games=10
def play():
    slot1=choice (slotsPossible)
    slot2=choice (slotsPossible)
    slot3=choice (slotsPossible)
    lose1=choice (losePossible)
    win = lose1
    print("")
    if(slot1==slot2==slot3=="cherry"):
        win = "\nYou're a big winner! Nice! $500!"
    if(slot1==slot2==slot3=="crown"):
        win = "\nYou're kind of a winner... Woot? $100"
    if(slot1==slot2==slot3=="apple"):
        win = "\nYou win an apple!"
    if(slot1==slot2==slot3=="lemon"):
        win = "\nTime to make some lemonade."
    return slot1+":"+slot2+":"+slot3+" "+win
for i in range(int(games)) :
    print(play())









