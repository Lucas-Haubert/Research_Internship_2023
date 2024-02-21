import time

# Getting spent time in unit "unit" from 2020/01/02 at 09:31:00 for a given data/time
def getTimeFromReference(date,clockTime,unit):
    
    # Converting DATE with shape YYYYMMDD into a time structure
    dateStruct=time.strptime(date,"%Y%m%d")
    
    # Converting TIME with shape HHMMSS into a time structure
    timeStruct=time.strptime(clockTime,"%H%M%S")
    
    # Global time structure
    specifiedTime=time.struct_time((dateStruct.tm_year, dateStruct.tm_mon, dateStruct.tm_mday,
                                       timeStruct.tm_hour, timeStruct.tm_min, timeStruct.tm_sec,
                                       timeStruct.tm_wday, timeStruct.tm_yday, timeStruct.tm_isdst))
    
    # Reference and specified times
    referenceTime=time.mktime(time.strptime("20200102 093100","%Y%m%d %H%M%S"))
    specifiedTime=time.mktime(specifiedTime)
    
    # The result
    timeDifference=specifiedTime-referenceTime
    
    # Dealing with the choice of unit, among "min" and "days"
    if unit=="min":
        secondsPerMin=60
        return timeDifference/secondsPerMin
    elif unit=="hours":
        secondsPerHour=60*60
        return timeDifference/secondsPerHour
    elif unit=="days":
        secondsPerDay=60*60*24
        return timeDifference/secondsPerDay
    else:
        return None

# print(getTimeFromReference("20200102", "103100", "min")) # returns 60.0

# Getting the current date after waiting timeMeasure unit from 2020/01/02 at 09:31:00
def getDate(timeMeasure,unit):

    # Converting time in seconds according to the specified united
    if unit=="min":
        secondsPerMin=60
        timeMeasure=timeMeasure * secondsPerMin
    elif unit=="hours":
        secondsPerHour=60*60
        timeMeasure=timeMeasure * secondsPerHour
    elif unit=="days":
        secondsPerDay=60*60*24
        timeMeasure=timeMeasure * secondsPerDay
    else:
        return None
    
    # Converting time in seconds spent for 2 Jan 2020 at 9:31
    referenceTime=time.mktime(time.strptime("20200102 093100", "%Y%m%d %H%M%S"))
    
    # Final time in seconds
    finalTime=referenceTime + timeMeasure
    
    # Convertir final time in a time structure
    finalStruct=time.localtime(finalTime)
    
    # Building DATE and TIME
    finalDate=time.strftime("%Y%m%d", finalStruct)
    
    return finalDate

# Getting the current time after waiting timeMeasure unit from 2020/01/02 at 09:31:00
def getTime(timeMeasure,unit):

    # Converting time in seconds according to the specified united
    if unit=="min":
        secondsPerMin=60
        timeMeasure=timeMeasure * secondsPerMin
    elif unit=="hours":
        secondsPerHour=60*60
        timeMeasure = timeMeasure * secondsPerHour
    elif unit=="days":
        secondsPerDay=60*60*24
        timeMeasure = timeMeasure * secondsPerDay
    else:
        return None
    
    # Converting time in seconds spent for 2 Jan 2020 at 9:31
    referenceTime=time.mktime(time.strptime("20200102 093100", "%Y%m%d %H%M%S"))
    
    # Final time in seconds
    finalTime=referenceTime + timeMeasure
    
    # Convertir final time in a time structure
    finalStruct=time.localtime(finalTime)
    
    # Building DATE and TIME
    finalTime=time.strftime("%H%M%S", finalStruct)
    
    return finalTime

# print(getTime(1.0,"days")) # returns "093100"
# print(getDate(1.0,"days")) # returns "20200103"

# Getting the literal expression of date/time
def getLiteralDateAndTime(DATE,TIME):
    year=DATE[:4]
    month=DATE[4:6]
    day=DATE[6:]
    hours=TIME[:2]
    minutes=TIME[2:4]
    seconds=TIME[4:]

    # Create the literal expression
    literalDate = "{:02d} {} {} at {}:{}:{}".format(
        int(day), getMonthName(int(month)), year, hours, minutes, seconds
    )

    return literalDate

# Getting month name from month number
def getMonthName(month):
    monthNames=[
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    return monthNames[month - 1]

# print(getLiteralDate("15891212","234500")) # returns 12 Dec 1589 at 23:45:00


