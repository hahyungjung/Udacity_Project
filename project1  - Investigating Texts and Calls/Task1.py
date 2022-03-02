"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def task1(texts, calls):

    numbers = []

    for i in range(len(texts)):
        numbers.append(texts[i][0])
        numbers.append(texts[i][1])

    for i in range(len(calls)):
        numbers.append(calls[i][0])
        numbers.append(calls[i][1])

    result = []

    for value in numbers:
        if value not in result:
            result.append(value)

    print("There are", len(result) ,"different telephone numbers in the records.")

    return(result)

task1(texts, calls)