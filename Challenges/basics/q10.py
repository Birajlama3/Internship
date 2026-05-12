# Reverse a string using for loop.
org_string = "python"
new_string = ""
for char in org_string:
    new_string = char + new_string

print(f"original string:{org_string}")
print(f"Reversed string:{new_string}")