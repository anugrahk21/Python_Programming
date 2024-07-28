#Regular Expression (Regex)

import re  # Import the re module, which provides support for working with regular expressions in Python.

# Define a function to check if a string is a valid regular expression.
def is_valid_regex(s):
    try:
        re.compile(s)  # Try to compile the string s into a regex object.
        return True  # If compilation succeeds, return True.
    except re.error:  # If a re.error exception is raised during compilation, the regex is invalid.
        return False  # In this case, return False.

# Read the number of test cases.
n = int(input("Enter the number of test cases: "))

# Process each test case.
for _ in range(n):
    test_string = input("Enter the regex pattern to validate: ")
    print(is_valid_regex(test_string))  # Print True if the string is a valid regex, otherwise print False.


'''
Key Concepts in Regular Expressions
Literals:

Characters that match themselves. For example, the regex abc matches the string "abc".
Metacharacters:

Characters with special meanings. Some common metacharacters are:
.: Matches any character except a newline.
^: Matches the start of the string.
$: Matches the end of the string.
*: Matches 0 or more repetitions of the preceding element.
+: Matches 1 or more repetitions of the preceding element.
?: Matches 0 or 1 repetition of the preceding element.
[]: Defines a character class. For example, [abc] matches any one of the characters a, b, or c.
|: Logical OR operator. For example, a|b matches either a or b.
(): Groups subpatterns. For example, (abc)+ matches one or more repetitions of the string "abc".
Escaping Metacharacters:

To use a metacharacter as a literal, you need to escape it with a backslash (\). For example, \. matches a literal period.
Character Classes:

Shorthand for common character sets. For example:
\d: Matches any digit (0-9).
\w: Matches any word character (alphanumeric plus underscore).
\s: Matches any whitespace character (space, tab, newline).
'''

import re  # Import the regular expressions module

# Define a regex pattern to match one or more digits
pattern = r"\d+"  
# The 'r' before the string indicates a raw string, which treats backslashes as literal characters.
# "\d" is a metacharacter that matches any digit (0-9).
# "+" is a quantifier that matches one or more occurrences of the preceding element (in this case, a digit).

# Search for the pattern in a given string
match = re.search(pattern, "The price is 100 dollars")
# re.search() scans through the string looking for the first location where the pattern matches.
# If the pattern is found, it returns a match object; otherwise, it returns None.

if match:  # If a match object is returned (i.e., the pattern was found in the string)
    print("Match found:", match.group())
    # match.group() returns the part of the string where the match was found.
    # In this case, it will return '100', as this is the first sequence of digits found in the string.
else:  # If no match object is returned (i.e., the pattern was not found in the string)
    print("No match found")
    # This would execute if the string did not contain any sequences of digits.
