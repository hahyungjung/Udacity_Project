"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
Code Review Comments : You need to find the addition of the total time spent on call either as a caller or a receiver.
"""

def task2(texts, calls):

    # List of those who made outgoing
    temp = {}

    for i in range(1, len(calls)):
        if calls[i][0] not in temp.keys():
            temp[calls[i][0]] = {
                    "sum": int(calls[i][3])
                    }
        else:
            temp[calls[i][0]]["sum"] += int(calls[i][3])

    out = []

    for key in temp.keys():
        sum_key = int(temp[key]["sum"])
        out.append([key, sum_key])

    max_calls_called = 0

    for i in range(len(out)):
        if out[i][1] > max_calls_called:
            max_calls_called = out[i][1]
            numbers_called = calls[i][0]

    # List of those who received calls
    temp = {}

    for i in range(1, len(calls)):
        if calls[i][1] not in temp.keys():
            temp[calls[i][1]] = {
                    "sum": int(calls[i][3])
                    }
        else:
            temp[calls[i][1]]["sum"] += int(calls[i][3])

    out = []

    for key in temp.keys():
        sum_key = int(temp[key]["sum"])
        out.append([key, sum_key])

    max_calls_received = 0

    for i in range(len(out)):
        if out[i][1] > max_calls_received:
            max_calls_received = out[i][1]
            numbers_received = calls[i][0]

    if max_calls_received > max_calls_called:
        print(numbers_received, "spent the longest time", max_calls_received, "seconds on the phone during September 2016.")
    else :
        print(numbers_called, "spent the longest time", max_calls_called, "seconds on the phone during September 2016.")

task2(texts, calls)
