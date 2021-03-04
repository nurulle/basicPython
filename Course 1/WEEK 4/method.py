#function associated with specific class

#
pets = "cats & dog"
print(pets.index("&"))


print(pets.index("c"))

print(pets.index("dog"))

print(pets.index("s"))

#print(pets.index("x")) eror karena ga ada


##
#Try using the index method yourself now!Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

a = "cats" in pets
print(a)


#
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_emil = email[:index] + "@" + new_domain
        return new_emil
    return email



#upper : jadi kapital\

b = "mountains".upper()
print(b)

#lwer " jadi kecil
c = "moNtain".lower()

print(c)


#
answer = 'YES'
if answer.lower() == "yes":
    print("user said yes")

#strip
e = " yes ".strip()
print(e)

#lstrip
f = " yes ".lstrip()
print(f)

#rstrip
g = " yes ".rstrip()
print(g)


#count
h = "the number of times e occurs in this stiring is 3".count("e")
print(h)


#isnumeric
i = "forest".isnumeric()

print(i)

j = "12345".isnumeric()
print(j)

#
k = int("12345") + int("54321")
print(k)


#join

l = " ".join(["this", "is", " a", "apple", "joined", "by", "spaces"])
print(l)

m = "...".join(["this", "is", " a", "apple", "joined", "by", "triple", "dots"])
print(m)


#split

n = "this is another example".split()
print(n)



# Want to try some string methods yourself? Give it a go!
# Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS



