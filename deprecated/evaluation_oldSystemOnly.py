import math

file_names = ["2017-02.txt", "2017-03.txt", "2017-04.txt", "2017-05.txt",
              "2017-06.txt", "2017-07.txt", "2017-08.txt", "2017-09.txt",
              "2017-10.txt", "2017-11.txt", "2017-12.txt", 
              "2018-01.txt", "2018-02.txt", "2018-03.txt", "2018-04.txt",
              "2018-05.txt", "2018-06.txt", "2018-07.txt", "2018-08.txt",
              "2018-09.txt", "2018-10.txt", "2018-11.txt", "2018-12.txt",
              "2019-01.txt", "2019-02.txt", "2019-03.txt", "2019-04.txt",
              "2019-05.txt", "2019-06.txt", "2019-07.txt", "2019-08.txt",
              "2019-09.txt", "2019-10.txt", "2019-11.txt", "2019-12.txt",
              "2020-01.txt", "2020-02.txt", "2020-03.txt", "2020-04.txt",
              "2020-05.txt", "2020-06.txt"]

for name in file_names:
    file = open(name, "r")
    print(name)

    line_indicator = ["Mo ", "Di ", "Mi ", "Do ", "Fr "]
    ignore_line = ["Urlaub", "GLZ", "Feiertag"]

    working_days_month = 0

    minutes_sum = 0

    hours_month = 0
    minutes_month = 0

    for line in file:
        if line[0:3] in line_indicator:

            cond_1 = ignore_line[0] in line
            cond_2 = ignore_line[1] in line
            cond_3 = ignore_line[2] in line

            if not(cond_1 or cond_2 or cond_3):
                #print(line)
                idx = line.find("h")
                hour = int(line[idx-2:idx])
                minute = int(line[idx+1:idx+3])
                minutes_sum = minutes_sum + hour*60 + minute
                working_days_month = working_days_month + 1

    hours_month = math.floor(minutes_sum / 60)
    minutes_month = minutes_sum - hours_month * 60

    hours_month = round(hours_month + minutes_month/60,2)

    print(working_days_month)
    print(hours_month/working_days_month)
    print("")
                