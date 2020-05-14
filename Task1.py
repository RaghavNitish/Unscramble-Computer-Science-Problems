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

phone_numbers = []

#Texts file
for element in texts:
    for i in range(2):
        if element[i] not in phone_numbers:
            phone_numbers.append(element[i])
            
#Calls file
for element1 in calls:
    for j in range(2):
        if element1[j] not in phone_numbers:
            phone_numbers.append(element1[j])
            
#Printing
print("There are {} different telephone numbers in the records.".format(len(phone_numbers)))