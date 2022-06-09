#Created by Malhar
#Created a program that is guess a number, simply a delared number i.e. 45


n = 45 #Guess a number i.e. 45
print("Please, enter a number")
guess = 0 #Starts from 0
while (guess < 5):
    guess = guess + 1
    num = float(input()) #input of number i.e. int or float, I have used float
    if (num > n): #for guessed big number
        print("Enter small number of guess", 5-guess)

    elif(num < n): #for guessed small number
        print("Enter bigger number of guess", 5-guess)

    elif(num == n): #for correct guess
        print("Great, you guessed correct!")
        break  #after correct guess, program will break

else: #after 5 in corrected gusses
    print("Sorry, guesses are over!")
