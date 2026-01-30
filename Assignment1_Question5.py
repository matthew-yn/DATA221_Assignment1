#Imports math package.
import math

"""
Function takes the radius of two circles, computes the areas, and finds the percentage of the 
larger circle that can be covered by the smaller circle.
"""
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    #Checks if radii are integers.
    if not (isinstance(radiusOfCircle1, int) and isinstance(radiusOfCircle2, int)):
        return "Radii must be an integer."

    #Checks if radii are positive.
    if radiusOfCircle1 < 0 or radiusOfCircle2 < 0:
        return "Radii must be positive."

    #Computes area of both radii.
    area1 = math.pi * radiusOfCircle1 ** 2
    area2 = math.pi * radiusOfCircle2 ** 2

    #Determines which area is larger.
    smallerArea = min(area1, area2)
    largerArea = max(area1, area2)

    #Calculates coverage percentage.
    percentageCovered = (smallerArea / largerArea) * 100

    #Returns result.
    return f"{percentageCovered}%"

#Prints output to user.
print(circleAreaCoverage(3, 5))