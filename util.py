# Standup Bot by Christina Aiello, 2017
import re
import logger

# For logging purposes
def format_minutes_to_have_zero(minutes):
    if minutes == None:
        return "00"
    else:
        if(int(minutes) < 10):
            return "0" + str(minutes)
        else:
            return str(minutes)


# Scheduler doesn't like zeros at the start of numbers...
# @param time: string to remove starting zeros from
def remove_starting_zeros_from_time(time):
    return (re.search( r'0?(\d+)?', time, re.M|re.I)).group(1)


# Adds 12 if PM else keeps as original time. When we insert
# data from the form into the database, we convert from AM/PM
# to 24-hour time.
def calculate_am_or_pm(reminder_hour, am_or_pm):
    logger.log("Reminder hour is: " + str(reminder_hour) + " and am or pm is: " + am_or_pm, "INFO")
    reminder_hour = int(reminder_hour)
    if (am_or_pm == "pm" and reminder_hour != 12):
        reminder_hour =  + 12
    elif (am_or_pm == "am" and reminder_hour == 12):
        reminder_hour = 0
    return reminder_hour
