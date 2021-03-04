import random
print(random.randint(1, 10))


import datetime
now = datetime.datetime.now()
type(now)

print(now)


now.year

print(now + datetime.timedelta(days=28))