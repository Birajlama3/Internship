# Count vowels and consonants in a senctence.
string = "Biraj Tamang"
vowels = "aeiou"
v_count =0
c_count = 0
for char in string.lower():
    if char.isalpha():
        if char in vowels:
         v_count+=1
        else:
            c_count+=1
print(f"Total vowels in {string} is {v_count}")
print(f"Total consonants in { string} is {c_count}")




