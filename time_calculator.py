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

    print(splitStart, splitStart2,splitDuration)
    print(startHour, startMin, startSign)


add_time("3:30 PM", "2:12")

    # return new_time