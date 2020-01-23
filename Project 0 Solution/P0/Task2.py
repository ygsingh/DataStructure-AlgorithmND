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
dicts = {}
#intialize values for each phone number key
for call in calls:
    dicts[call[0]] = 0#dicts[call[0]] + call[3]
    dicts[call[1]] = 0#dicts[call[1]] + call[3]

for call in calls:
    dicts[call[0]] = dicts[call[0]] + int(call[3])
    dicts[call[1]] = dicts[call[1]] + int(call[3])

# algoithm to extract the max_duration and the telephone number
# with maximum duration
number_list = list(dicts.keys())
duration_list = list(dicts.values())
max_duration = max(duration_list)
tel_n = number_list[duration_list.index(max_duration)]
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(tel_n,max_duration))
