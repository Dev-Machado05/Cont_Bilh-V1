import datetime
LocalTime = datetime.datetime.now().strftime("%H:%M:%S")
hr = int(LocalTime[:2])
mn = int(LocalTime[3:5])

def Lc_time():

    if hr >= 0 and hr <= 11:
        bin = 0
    elif hr >= 12 and hr <= 16 or hr == 17 and mn <= 30:
        bin = 1
    elif hr == 17 and mn > 30 or hr >= 18 and hr <= 23:
        bin = 2
    return bin
