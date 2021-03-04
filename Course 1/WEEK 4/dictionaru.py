x = {}
print(type(x))

#
file_counts = {"jpg":10, "txt":14, "cvs":2, "py":23}
print(file_counts)

print(file_counts["txt"])

print("jpg" in file_counts)

print("html" in file_counts)

file_counts["cfg"] = 8
print(file_counts)

file_counts["cvs"] = 17
print(file_counts)

del file_counts["cfg"]
print(file_counts)


#The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	1) Add an entry for Epilogue on page 39. 	2) Change the page number for Chapter 3 to 24. 	3) Display the new dictionary contents. 	4) Display True if there is Chapter 5, False if there isn't.


toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc ["Epilogue"] = 39 # Epilogue starts on page 39
toc ["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc)
 # Is there a Chapter 5?