# iterates over a section

for x in range(5):

    print(x)

######################
#Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included). Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).


def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285



######################

friends = ['taylor', 'alex', 'pat']
for friends in friends:
    print("Hi " + friends)


######################

values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("total sum: " + str(sum) + "- average : " + str(sum/length))


######################
product = 1
for n in range(1,10):
    product = product * n
print(product)



############

#In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return the right number.

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


#
def tocelcius(y):
    return  (y-32)*5/9

for y in range(0,101,10):
    print(y,tocelcius(y))


#