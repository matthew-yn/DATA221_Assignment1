"""
Function converts seconds since midnight into hours, minutes, seconds, and AM or PM.
"""
def convert_seconds(seconds):
    #Validates input.
    if not isinstance(seconds, int) or seconds < 0 or seconds >= 86400:
        return "Invalid input."

    #Calculates hours, minutes, and seconds.
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    #Determines AM or PM.
    period = "AM"
    if hours >= 12:
        period = "PM"

    #Converts to 12-hour format.
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12

    #Returns time.
    return f"{hours}:{minutes}:{secs} {period}"

#Test
print(convert_seconds(19067))
