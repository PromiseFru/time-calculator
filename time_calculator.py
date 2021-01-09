def add_time(start, duration, day = ""):
    splitStart = start.split(':')
    splitStart2 = splitStart[1].split();
    splitDuration = duration.split(':')

    # start variables
    startHour = int(splitStart[0])
    startMin = int(splitStart2[0])
    startSign = splitStart2[1]

    # duration variables
    durationHour = int(splitDuration[0])
    durationMin = int(splitDuration[1])

    # convert start hour to 24 hours
    if startSign == "PM":
        startHour = startHour + 12

    # add hours
    sumHours = startHour + durationHour
    # add minutes
    sumMin = startMin + durationMin

    # round up minutes
    sumHours = sumHours + int(sumMin/60)
    sumMin = sumMin%60

    # day count
    count = int(sumHours/24)

    # get sign 
    if (sumHours%24) < 12:
        sign = 'AM'
    else:
         sign = 'PM'
    
    # hour
    sumHours = sumHours%24
    # change hour to 12hour format
    if sumHours > 12:
        sumHours = sumHours-12
    if sumHours == 0:
        sumHours = 12
    
    countString = ''
    if count == 1:
        countString = "(next day)"
    elif count > 1:
        countString = "(" + str(count) + " days later)"

    new_time = str(sumHours) + ":" + str(sumMin) + " " + sign + " " + countString

    print(new_time)
    # return new_time

add_time("3:30 PM", "2:12")

