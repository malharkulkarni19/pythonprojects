number = int(input("Enter number of rows:\n")) #Number of rows
stairs = int(input("Enter 1 for increasing tairs & 0 for decreasing stairs")) 
c = bool(stairs)
if stairs:
    for i in range(number): # For increasing stairs
        print('*'*i)
else:
    for i in range(number, 0, -1):  #For decreasing stairs
        print('*'*i)
