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
in Bangalore.
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

# find area code of mobile prefixes (function)
def findCode(pnumber):
    if pnumber[0:3] == '140':
        return 140
    if pnumber[0] == '(':
        str = pnumber.split(')')
        return str[0][1:]
    else:
        return pnumber[0:4]

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

codes = []
for call in calls:
    code1 = findCode(call[0])
    if code1 == '080':
        code2 = findCode(call[1])
        codes.append(code2)

nbangalore = float(codes.count('080'))
frac = nbangalore/len(codes)*100
codes = uniqueArray(codes)
#print("{:0.2f}".format(frac))
#codes = sort(codes)

print("The numbers called by people in Bangalore have codes:")
printCodes(codes)

print("{:0.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(frac))
"""
def test():
    print(findCode('(080)324324'))
    print(findCode('(0805)324324'))
    print(findCode('140324324'))
    print(findCode('08032 43254'))

test()
"""
