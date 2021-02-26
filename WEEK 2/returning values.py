def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b

print("the sum of both areas is: " + str(sum))


# Use the get_seconds function to work out the
# amount of seconds in 2 hours and 30 minutes,
# then add this number to the amount of seconds in
# 45 minutes and 15 seconds. Then print the result.

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)


#
def convert_second(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_second = seconds - hours * 3600 - minutes * 60
    return  hours, minutes, remaining_second

hours, minutes, seconds = convert_second(5000)
print(hours, minutes, seconds)




#
def greeting(name):
    print("welcome, " + name)

result = greeting("coco")

print(result)

#None is a very special data type in Python used to indicate that things  are empty or that they return nothing