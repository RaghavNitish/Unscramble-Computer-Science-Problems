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

total_list = []

#Creating a total set of calling phone numbers
for element in calls:
    if element[0] not in total_list:
        total_list.append(element[0])

#Removing the phone numbers from texts
for element1 in texts:
    for i in range(2):
        if element1[i] in total_list:
            total_list.remove(element1[i])

#Removing the receiving phone numbers
for element2 in calls:  
    if element2[1] in total_list:
        total_list.remove(element2[1])
       
#Printing in lexicographic order
total_list = sorted(total_list)
print("These numbers could be telemarketers: ")
for element3 in total_list:
    print(element3)





