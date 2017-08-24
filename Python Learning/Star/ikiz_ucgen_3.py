count =  input ("Type a Valuable...")
count = int (count)
for i in range(count):
        for j in range(count-i-1):
            print ("_",end="")
        for j in range(i+1):
            print("*",end="")
        print()

for i in range(count):
        for j in range(i+1):
            print ("_",end="")
        for j in range(count-i-1):
            print("*",end="")
        print()
        

