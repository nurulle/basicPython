class Piglet:
    def speak(self):
        print("oink drink")

hamlet = Piglet()
hamlet.speak()


class Piglet1:
    name = "piglet"
    def speak(self):
        print("oink drink ! I'm {}! oink!".format(self.name))

hamlet = Piglet1()
hamlet.name = "hamlet"
hamlet.speak()



class Piglet2:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = Piglet2()
print(piggy.pig_years())



#OK, now it’s your turn! Have a go at writing methods for a class.
#Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).


class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())



