#Design caculator which gives faulty answer for som operation
#Made ny Malhar Kulkarni
#Faulty only when 45+40 and 5*5
#All other operations are true

print("Enter First Number") #for 1st number
num1 = float(input())
print("Enter Second Number") #for second number
num2 = float(input())
print("Which operation do you want to perform +, -, *, /, %") #Enter which opertaion you want to perform
num3 = input()

if num1 == 45 and num2 == 40 and num3 == "+": #It is faulty case as 45+40=85
    print("Your Answer is: 90")
elif num1 == 5 and num2 == 5 and num3 == "*": #It is also faulty as 5*5=25
    print("Your Answer is: 26")
elif num3 == "+": #For addition
    num4 = num1+num2
    print("Your Answer is:",num4)
elif num3 == "-": #For subtraction
    num4 = num1-num2
    print("Your Answer is:",num4)
elif num3 == "*": #For multiplication
    num4 = num1*num2
    print("Your Answer is:",num4)
elif num3 == "/": #For division
    num4 = num1/num2
    print("Your Answer is:",num4)
else: #It is other than above cases, I also inserted % but not defined it so it will print this
    print("Error, This can't be calculated")

print("Finally, Done")
