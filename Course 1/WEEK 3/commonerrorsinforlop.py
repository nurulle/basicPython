#false
# for x in 25:
#     print(x)

#true
for y in range(25):
    print(y)


#
for z in [25]:
    print(z)

#
def greet_friend(friends):
    for friend in friends:
        print("hi " + friend)

greet_friend(['cici', 'cucu', 'bhb'])
greet_friend("barry")


#The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling it like in this example, something is not right. Can you figure out what to fix?
def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat"])