# class Clothing:
#     stock = {'name': [], 'material': [], 'amount': []}
#
#     def __init__(self, name):
#         material = ""
#         self.name = name
#
#     def add_item(self, name, material, amount):
#         Clothing.stock['name'].append(self.name)
#         Clothing.stock['material'].append(self.material)
#         Clothing.stock['amount'].append(amount)
#
#     def Stock_by_Material(self, material):
#         count = 0
#         n = 0
#         for item in Clothing.stock['material']:
#             if item == material:
#                 count += Clothing.stock['amount'][n]
#                 n += 1
#         return count
#
#
# class Shirt(Clothing):
#     material = "Cotton"
#
#
# class Pants(Clothing):
#     material = "Cotton"
#
#
# formal = Shirt("Formal")
# dress_pants = Pants("Dresspants")
# formal.add_item(formal.name, formal.material, 13)
# dress_pants.add_item(dress_pants.name, dress_pants.material, 7)
# current_stock = polo.Stock_by_Material("Cotton")
# print(current_stock)



class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
        self.packages[package.name] =package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return  result