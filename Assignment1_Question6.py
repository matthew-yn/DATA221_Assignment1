def distribution_analysis(numbers):
    #Finds total number of elements in the list.
    total = len(numbers)

    #Creates dictionary to store results.
    result = {}

    #Loops through each unique value in the list.
    for value in set(numbers):
        #Counts number of elements that are <= the current value.
        count = sum(1 for n in numbers if n <= value)

        #Calculates the percentage.
        result[value] = (count / total) * 100

    #Returns the dictionary sorted by key.
    return dict(sorted(result.items()))


#Test list.
number_list = [3, 1, 2, 3, 4, 2]
#Prints output to user.
print(distribution_analysis(number_list))
