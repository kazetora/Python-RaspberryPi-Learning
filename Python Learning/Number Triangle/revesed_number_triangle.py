# Works on Python 2.x.x

count = input ("Enter a Valuable...")
count = int(count)

for i in range(count):
    for j in range(count-i):
        print " ",
    for k in reversed(range(i)):
        print k,
    print ""
