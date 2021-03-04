name = "sasha"
color = 'gold'
place = "cambridge"

print("nama " + name +", favorit color: " + color)



#
"example" * 3

#
pet = "loooooooooooooooooooooooooooooooooo"
len(pet)

#Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.


def double_word(word):
    word *= 2
    count = 0
    for letter in word:
        count += 1
    return word + str(count)
print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0



#untuk
nama = "jaylen"
print(nama[1])
print(nama[0])
print(nama[5])


#
text = "random string with a lot of characters"
print(text[-1])

print(text[-2])


#

#
fruit = "pineapple"
print(fruit[:4])

print(fruit[4:1])


print(fruit[4:])