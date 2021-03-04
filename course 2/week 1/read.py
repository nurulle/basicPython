with open("a.txt") as file:
    for line in file:
        print(line.upper())



#

with open("a.txt") as file:
    for line in file:
        print(line.strip().upper())



with open("a.txt") as text:
    for line in text:
	    print(line.strip())



#
file = open("a.txt")
lines = file.readline()
file.close()
lines.sort()
print(lines)