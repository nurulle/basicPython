multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

#
multiples = [x*7 for x in range(1,11)]
print(multiples)

#
languages = ["python", "perl", "ruby", "go", "java", "C"]
length = [len(languages) for language in languages]
print(length)

#
z = [x for x in range(0,101) if x % 3 == 0]
print(z)



#The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.
def odd_numbers(n):
	return [x for x in range (0,n+1) if x%2 !=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []