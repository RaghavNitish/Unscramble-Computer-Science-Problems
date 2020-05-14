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

dict_times = {}

for element in calls:
    for i in range(2):
        if element[i] not in dict_times.keys():
            dict_times[element[i]] = int(element[3])
        else:
            dict_times[element[i]] += int(element[3])

max_phone = max(dict_times, key=dict_times.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_phone, dict_times[max_phone]))



            




