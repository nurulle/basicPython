class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny = Apple("green", "tart")
carlenian =Grape("purple", "sweet")
print(granny.flavor)

print(carlenian.color)


##############

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(
            name=self.name, sound=self.sound
        ))

class Piglet(Animal):
    sound = "oink"

hamlet = Piglet("hamlet")
hamlet.speak()


class Cow(Animal):
    sound = "moo"

milku = Cow("milky white")
milku.speak()