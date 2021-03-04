numbers = [4, 6, 2, 7, 1]
numbers.sort()
print(numbers)

names = ["carlos", "ray", "coc", "cici"]
print(names)

print(sorted(names))



print(sorted(names, key=len))



####

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))
