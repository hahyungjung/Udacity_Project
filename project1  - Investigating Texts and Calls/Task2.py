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


    slice_list = []

    for i in range(len(calls)):
        slice_list.append([calls[i][0], calls[i][3]])

    for j in range(len(calls)):
        slice_list.append([calls[j][1], calls[j][3]])

    # List of those who made outgoing
    temp = {}

    for i in range(1, len(slice_list)):
        if slice_list[i][0] not in temp.keys():
            temp[slice_list[i][0]] = {
                    "sum": int(slice_list[i][1])
                    }
        else:
            temp[slice_list[i][0]]["sum"] += int(slice_list[i][1])

    out = []

    for key in temp.keys():
        sum_key = int(temp[key]["sum"])
        out.append([key, sum_key])

    max_calls = 0

    for i in range(len(out)):
        if out[i][1] > max_calls:
            max_calls = out[i][1]
            numbers = out[i][0]


    print(numbers, "spent the longest time", max_calls, "seconds on the phone during September 2016.")


task2(texts, calls)


