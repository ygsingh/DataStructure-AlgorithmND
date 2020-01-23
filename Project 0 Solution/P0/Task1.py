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

# list to store all the phone numbers
phoneNumbers = []

# get all phone numbers from call records
for i in range(len(calls)):
    phoneNumbers.append(calls[i][0])
    phoneNumbers.append(calls[i][1])

# get all phone numbers from text records
for i in range(len(texts)):
    phoneNumbers.append(texts[i][0])
    phoneNumbers.append(texts[i][1])

# Takes a sequence and return a sequence of unique
# values in the input sequence

def uniqueArray(seq):
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

# get unique phone numbers from the list off all phone numbers
uniquePhoneNumbers = uniqueArray(phoneNumbers)

# count the unique phone numbers
count = len(uniquePhoneNumbers)
# print the required result
print("There are {} different telephone numbers in the records.".format(count))

# Tests to check uniqueArray function
#def test():
#    print(uniqueArray([1,1,1,1,1,1]))
#    print(uniqueArray([1,1,2,2,3,3]))
#test()
