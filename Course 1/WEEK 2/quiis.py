#
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


#
def exam_grade(score):
	if score == 100:
		grade = "Top Score"
	elif 95 >= score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


#
def format_name(first_name, last_name):
	# code goes here

	if first_name != "" and last_name != "":
		return ("Name: " + last_name + ", " + first_name)
	elif first_name != "" or last_name != "":
		return ("Name: " + last_name + first_name)
	else:
		return ''
		return string

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"
#
print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"
#
print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"
#
print(format_name("", ""))
# Should return an empty string


#

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


#
def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))


#
def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient
    if denominator > 0:
        return (numerator / denominator) % 1
        return 0


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0