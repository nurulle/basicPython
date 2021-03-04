
import shutil


du = shutil.disk_usage("/")
print(du)


a = du.free/du.total*100
print(a)