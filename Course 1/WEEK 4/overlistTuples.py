animals = ["lion", "xebra", "doblin", "monkey"]
chars = 0
for animals in animals:
    chars += len(animals)

print("total character: {}, average length: {}".format(chars, chars/len(animals)))


#
winner = ["ashley", "fylan", "rese"]
for index, person in enumerate(winner):
    print("{} . {}".format(index + 1, person))


#Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.

def skip_elements(elements):
    # code goes here

    new_elements = []
    for index, element in enumerate(elements):
        if (index % 2 == 0):
            new_elements.append(element)
    return new_elements


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']



###
#
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
        return result
print(full_emails([("alexander.com", "alex dieogo"),
                   (" shay@example.com", "shay brandit")]))