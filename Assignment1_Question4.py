#Imports random package.
from random import random

#Generates a list of 20 random numbers between 0 and 1.
values = [random() for _ in range(20)]

#Generates a random value x.
x = random()

#Sorts the list in ascending order.
values.sort()

#Prints the sorted list.
print("Sorted values:", values)

#Prints the random value x.
print("x:", x)

#Loops through the list to find the first value >= x.
for i in range(len(values)):
    if values[i] >= x:
        print("First index where value >= x:", i)
        break
else:
    #Runs only if no break occurred.
    print("No values greater than or equal to x.")