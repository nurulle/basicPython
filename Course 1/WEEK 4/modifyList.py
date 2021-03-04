#
fruit = ["pinaple", "bansana", "apple", "melon"]
fruit.append("kiwi")
print(fruit)

#mnmbhkan di awal
fruit.insert(0, "orange")
print(fruit)

#mnmbhkan di akhir
fruit.insert(25, "peach")
print(fruit)

#mnghapus
fruit.remove("melon")
print(fruit)

#hasil eror kaena ga ada
# fruit.remove("pear")
# print(fruit)

#
print(fruit.pop(3))

print(fruit)


#
fruit[2] = "strawberry"
print(fruit)
