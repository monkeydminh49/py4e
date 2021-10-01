# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


handle = open(input('Enter a file name: '))
mails = {}

for lines in handle:
    lines.rstrip()
    words = lines.split()

    if not lines.startswith('From '): continue
    if len(words) < 2: continue

    m = words[1]
    x = m.find('@')
    domain = m[x+1:]
    mails[domain] = mails.get(domain, 0) + 1
    
print(mails)


