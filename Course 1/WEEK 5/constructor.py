class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

janagold = Apple("red", "sweet")
print(janagold.color)

print(janagold)



class Apple1:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "this apple is {} an its flavor is {}".format(self.color, self.flavor)

janagold = Apple1("red", "sweet")
print(janagold)






#

class Apple3:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        def __str__(self):
            return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

# help(Apple3)
#
# class Apple4(builtins.object)
#     Methods defined here: __init__(self, color, flavor)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  __str__(self)
#  |      Return str(self).
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#

#
def to_second(hours, minutes, second):
    """Return the amount of second in the given haours, minutes, and second."""
    return hours*3600+minutes*60+second

print(help(to_second))