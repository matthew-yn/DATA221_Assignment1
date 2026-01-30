#Variable for limit.
threshold = 100
#Initial value for multiplication.
product = 1
#Number to start multiplying.
currentNumber = 1

#Loops until product exceeds threshold.
while product <= threshold:
    #Multiplies current product by current number.
    product *= currentNumber
    #Ends loop if product has exceeded threshold.
    if product > threshold:
        break
    #Increments current number by 1.
    currentNumber += 1

#Prints final product to user.
print("Final product:", product)\
#Prints number that caused product to exceed threshold.
print("Number that caused the product to exceed the threshold:", currentNumber)