"""
Function takes a list of strings and returns a dictionary with the strings as keys and values
as a dictionary containing the length of the string and whether it is even or odd.
"""
def string_info_dictionary(strings):
    #Creates an empty dictionary to store results.
    result = {}

    #Loops through each string in the list.
    for s in strings:
        #Finds length of the string.
        length = len(s)

        #Checks if length of string is even or odd.
        if length % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        #Stores info into nested dictionary.
        result[s] = {"length": length, "parity": parity}

    #Returns nested dictionary.
    return result


#Test list of strings.
words = ["data", "science"]
#Prints output of function to user.
print(string_info_dictionary(words))