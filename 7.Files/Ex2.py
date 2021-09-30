# # Exercise 2: Write a program to prompt for a file name, and then read
# # through the file and look for lines of the form:
# # X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence90 CHAPTER 7. FILES
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

# Test your file on the mbox.txt and mbox-short.txt files.

fout = open(input('Enter a file name: '))
count = 0
s = 0

for i in fout:
    if not i.startswith('X-DSPAM-Confidence:'):
        continue

    f = i.find(' ', 21)
    n = float(i[20:f])
    count += 1
    s = s + n
      
    # stp = i.rstrip()
    # count += 1
    # n = float(stp[20:])
    # s = s + n

print('Average spam confidence: ', s/count)

