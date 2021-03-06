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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def task3(texts, calls):

    # part A

    calledNumber = []
    res = []

    for i in range(len(calls)):
        if calls[i][0][0:5] == "(080)":
            if calls[i][1][0] == "7" or calls[i][1][0] == "8" or calls[i][1][0] == "9":
                calledNumber.append(calls[i][1][0:4])
            elif calls[i][1][0:3] == "140":
                calledNumber.append("140")
            elif calls[i][1][0] == "(":
                for j in range(len(calls[i][1])):
                    if calls[i][1][j] == ")":
                        calledNumber.append(calls[i][1][0:(j+1)])

    for i in calledNumber:
        if i not in res:
            res.append(i)

    print("The numbers called by people in Bangalore have codes:", *sorted(res), sep="\n")

    # part B


    called_list = []
    received_list = []
    count1 = 0
    count2 = 0

    for i in range(len(calls)):
        called_list.append(calls[i][0])

    for i in range(len(calls)):
        received_list.append(calls[i][1])

    for i in range(len(calls)):
        if "(080)" in called_list[i][0:5]:
            count1 += 1
            if "(080)" in received_list[i][0:5]:
                count2 += 1
    percentageBanga = count2 / count1 * 100

    print(round(percentageBanga, 2), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

task3(texts, calls)