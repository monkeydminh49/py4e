# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

handle = open(input('Enter a file name: '))
mails = {}

for lines in handle:
    lines.rstrip()
    if not lines.startswith('From '): continue
    words = lines.split()
    if len(words) < 2: continue
    mails[words[1]] = mails.get(words[1], 0) + 1

for k,v in mails.items():
    if v == max(mails.values()):
        print(k, v)
 