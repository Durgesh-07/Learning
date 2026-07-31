import re
s1 = "The BodyGuard is the best album"

# Define the pattern to search for
pattern = r"Body"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")
pattern1 = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text1 = "My Phone number is 1234567890"
match1 = re.search(pattern1, text1)

if match1:
    print("Phone number found:", match1.group())
else:
    print("No match")
pattern2 = r"\W"  # Matches any non-word character
text2 = "Hello, world!"
matches2 = re.findall(pattern2, text2) # Find all non-word characters in the string

print("Matches:", matches2)
s2 = "The BodyGuard is the best album of 'Whitney Houston'."


# Use the findall() function to find all occurrences of the "st" in the string
result3 = re.findall("st", s2)

# Print out the list of matched words
print(result3)
# Use the split function to split the string by the "\s"
split_array = re.split(r"\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)
# Define the regular expression pattern to search for
pattern3 = r"Whitney Houston"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern3, replacement, s2, flags=re.IGNORECASE) # re.IGNORECASE makes the search case-insensitive, so it matches "Whitney Houston" in any letter case

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")