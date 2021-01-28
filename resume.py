fname = input("Enter file name: ")
import csv
abc = input('Enter keywords: ')
wxy = abc.upper()
ghi = [wxy]
for row in csv.reader(ghi, delimiter=" "):
    count = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
f = open(fname)
lines = f.readlines()
f.close()
for line in lines:
    line = line.strip().upper().split()
    for words in line:
        if words.find(row [0].upper()) != -1:
            count += 1
#print (row[0])
#print (count)
with open(fname) as f:
    if row [0] in f.read().upper():
        print(row [0],'found on page', count)
    else:
        print(row [0],'- NEGATIVE')
print()
for line in lines:
    line = line.strip().upper().split()
    for words in line:
        if words.find(row [1].upper()) != -1:
            count_1 += 1
#print (row [1])
#print (count_1)
with open(fname) as f:
    if row [1] in f.read().upper():
        print(row [1],'found on page',count_1)
    else:
        print(row [1],'- NEGATIVE')
print()
for line in lines:
    line = line.strip().upper().split()
    for words in line:
        if words.find(row [2].upper()) != -1:
            count_2 += 1
#print (row[2])
#print (count_2)
with open(fname) as f:
    if row [2] in f.read().upper():
        print(row [2],'found on page',count_2)
    else:
        print(row [2],'- NEGATIVE')
print()
for line in lines:
    line = line.strip().upper().split()
    for words in line:
        if words.find(row [3].upper()) != -1:
            count_3 += 1
#print (row [3])
#print (count_3)
with open(fname) as f:
    if row [3] in f.read().upper():
        print(row [3],'found on page',count_3)
    else:
        print(row [3],'- NEGATIVE')
print()
print ('Complete')
