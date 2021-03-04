file_counts = {"jpg":10, "txt":14, "cvs":2,"py":23}
for extention in file_counts:
    print(extention)


#
for ext, amount in file_counts.items():
    print("there are {} files with me .{} extension".format(amount, ext))


#
print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
    print(value)


#Now, it's your turn! Have a go at iterating over a dictionary!
#Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.


cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))


#mngtahu jmlh hruf
def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letter("aaaaaaaa"))

print(count_letter("tenant"))

print(count_letter("a long string with a lot of letter"))

