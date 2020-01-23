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

incoming = []
outgoing = []
send = []
recieve = []

for text in texts:
    send.append(text[0])
    recieve.append(text[1])

for call in calls:
    outgoing.append(call[0])
    incoming.append(call[1])



# Function to find unique elements
def uniqueArray(seq):
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

# Function to sort lexicographic
def printCodes(seq):
    temp = seq
    while len(temp) > 0:
        first = min(temp)
        print(first)
        temp.remove(first)



tele = []
for outcall in outgoing:
    if outcall not in incoming and outcall not in send and outcall not in recieve:
        tele.append(outcall)

tele = uniqueArray(tele)
print("These numbers could be telemarketers: ")
printCodes(tele)
