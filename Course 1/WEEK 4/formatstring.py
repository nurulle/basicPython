#format
name = "manny"
number = len(name) * 3
print("hello {}, your lucky number is {}".format(name, number))

print("your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))


#Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

def student_grade(name, grade):
	return ("{} received {}% on the exam".format(name, grade))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


#
price = 7.5
with_tax = price * 1.09
print(price, with_tax)

print("base price: ${:.2f}. With tax: ${:.2f}".format(price, with_tax))



#
def to_celcius(x):
    return  (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celcius(x))


#

def to_celcius(x):
    return  (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))


#

# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""



##########

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""