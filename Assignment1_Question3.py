"""
Function computes x to the power of y.
"""
def power(x, y):
    return x ** y

#List of (x, y) pairs.
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
#Creates a list of valid pairs.
results = []

#Loops through list of (x, y) pairs using argument unpacking.
for x, y in pairs:
    #Skips pair if y is negative.
    if y < 0:
        continue
    #Appends valid pairs to result list.
    results.append(power(x, y))

#Prints results back to user.
print(results)