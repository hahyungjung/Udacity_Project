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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def task4(texts, calls):

    callers = set()
    called = set()
    texters = set()
    texted = set()

    for i in range(len(calls)):
       callers.add(calls[i][0])
       called.add(calls[i][1])

    for i in range(len(texts)):
        texters.add(texts[i][0])
        texted.add(texts[i][1])

    callers = callers.difference(called)
    callers = callers.difference(texters)
    callers = callers.difference(texted)

    print("These numbers could be telemarketers: ", sorted(callers))

task4(texts, calls)




