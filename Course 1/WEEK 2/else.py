def hint_username(username):
    if len(username) < 3:
        print("invalid username. must be at least 3 characters long")

    else:
        print("valis username")

print(hint_username("co"))

#
def is_positive(number):
  if number > 0:
    return True
  else:
    return False

print(is_positive(4))


#
def is_even(number):
    if number % 2 == 0:
        return  True
    return False
print(is_even(5))


#
if number > 11:
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

#

print("A dog" + "A mouse")
print(9999+8888 + 100*100)

#
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % 4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096 * (full_blocks + 1)
    return full_blocks * 4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192