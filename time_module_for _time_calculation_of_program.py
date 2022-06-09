#Created time module in python, which will calculate time to executes code in python
#Created by Malhar Kulkarni

import time  #Imported time module

initial1 = time.time()  #Declared time for 1st print statement

for i in range(5):   #Using for loop
    time.sleep(2)     #This will sleep program in for loop for 2 seconds
    print("This is Malhar")

print("For loop runs in", time.time() - initial1, "Seconds") #Final statement for for loop including time calculation

initial2 = time.time()   #Declared time for 2st print statement

k = 0
while(k<5):  #Using while loop
    time.sleep(2)     #This will sleep program in while loop for 2 seconds
    print("This is Malhar Kulkarni")
    k+=1

print("While loop runs in", time.time() - initial2, "Seconds") #Final print statement for whle loop including time calculation

localtime = time.asctime(time.localtime(time.time())) #For time right now
print(localtime)
