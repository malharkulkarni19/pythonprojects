#Game devolopment- Mobile, Laptop, Computer
#Created by Malhar Kulkarni

import random  #import random function

list1 = ["mobile", "laptop", "computer"]  #list contains input

print("Welcome to the Game")

n = 0
while n < 5:  # while loop used 
    choice = random.choice(list1)
    a = choice
    m1 = str(input("Enter your componoent between these 3\nmobile laptop computer\n"))
    c = m1.capitalize()
    if c == a: #if-condition
        my_score = 1
        print("The score is", my_score)
        print("Yey, you won!\n")
        print("You have no chances remaining", 5-n)
    else: #else-condition
        system_score = 1
        print("system score is", system_score)
        print("Oops, you lost\n")
        print("The chances lefts are", 4-n)
        n = n + 1

print("Game Ended!")
