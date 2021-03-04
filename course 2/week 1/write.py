#ganti isi file

with open("a.txt", "w") as file:
    file.write("coco cantik")

import os

# mnghapus
#os.remove("a.txt")


#merename
os.rename("a.txt", "b.txt")

# mengecek file ada apa ga
print(os.path.exists("b.txt"))


print(os.path.exists("c.txt"))


# mengecek size
print(os.path.getsize("b.txt"))

# time
print(os.path.getatime("b.txt"))

timestamp = os.path.getmtime("b.txt")

# mngcek lokasi
print(os.path.abspath("b.txt"))