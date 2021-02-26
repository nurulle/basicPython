# yang mengembalikan panjang string. : len

name = "coco"
number = len(name) * 9

print("hello " + name + " your lucky number is " + str(number))



#
def lucky_number(name):
    number = len(name) * 9
    print("hello " + name + "your lucky number is " + str(number))

lucky_number("caca")
lucky_number("iqball")


# In this code, identify the repeated pattern and replace it with a function called month_days, that receives the name of the month and the number of days in that month as parameters. Adapt the rest of the code so that the result is the same. Confirm your results by making a function call with the correct parameters for both months listed.

def month_days(month,days):
    print( month + " has " + str(days) + " days.")

month_days("june", 30)
month_days("july", 31)