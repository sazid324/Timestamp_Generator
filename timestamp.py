from datetime import datetime

timeline = ["00:00:00", "00:00:31", "00:02:58", "00:03:52", "00:05:24", "00:08:05", "00:10:36", "00:14:53", "00:25:44", "00:42:14",
            "00:43:10", "00:46:02", "00:48:42", "00:53:10", "00:57:53", "01:00:00", "01:06:00", "01:07:47", "01:22:00", "01:30:00", "01:34:00"]

newtimeline = []

base_time = "12:47:59"

for i in range(len(timeline) - 1):
    base_datetime = datetime.strptime(base_time, '%H:%M:%S')
    time2 = datetime.strptime(timeline[i+1], '%H:%M:%S')
    time1 = datetime.strptime(timeline[i], '%H:%M:%S')

    timegap = time2 - time1

    result_time = base_datetime + timegap

    base_time = result_time.strftime('%H:%M:%S')

    newtimeline.append(base_time)

print("Result:", newtimeline)
