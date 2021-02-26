def greeting(name):
    print("welcome, " + name)

greeting("kay")


def greeting1(nama, departement):
    print("welcome, " + nama)
    print("you are part of " + departement)

greeting1("coco", "ceo")



# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.
def print_seconds(hours, minutes, seconds):
    print(3600 + 60 + seconds)

print_seconds(1,2,3)