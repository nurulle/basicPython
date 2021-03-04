def hint_username(username):
    if len(username) < 3:
        print("invalid username. must be at least 3 characters long")

    else:
        if len(username) > 15:
            print("invalid username. must be at least 3 characters long")
        else:
            print("valis username")


#

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

#
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))