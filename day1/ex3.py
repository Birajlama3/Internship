#  -- File Handling --  

 # Read content of file in readmode as default.
with open("Hello.txt") as f:
    print(f.read())
    print(f.readline())
f.close()

# Append in a file --> will append at the end of the file
with open("Hello.txt", "a") as f:
    f.write(" After appending, This is new text.")
with open("Hello.txt", "rt") as f:
    print(f.read())

# write in a file --> overwite the existing content of a file deleting the old ones.
with open("Hello.txt", "w") as f:
    f.write(" After overwriting, This is new text.")
with open("Hello.txt", "rt") as f:
    print(f.read())


# create a new file 
with open("new.txt", "x") as f:
    f.write("Hello world!")
    print("new.txt created successfully.")
f.close()
 
# To delete a file we need to import OS module.
import os
os.remove("new.txt")

# To delete a entire folder we use rmdir method.
os.rmdir("FolderName")