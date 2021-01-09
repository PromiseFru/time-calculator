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
    if (sumHours%20) < 12:
        sign = 'AM'
    else:
         sign = 'PM'



    print(sumHours, sumMin, count, sign)


add_time("3:30 PM", "2:12")

    # return new_time