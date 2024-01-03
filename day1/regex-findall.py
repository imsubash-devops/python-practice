#The findall function in the re module is used to find all occurrences of a pattern in a given string. 
#It returns a list of all non-overlapping matches.
import re
text = "The quick brown fox jump over the lazy dog. The quick fox is quick"
pattern = r"quick"

match = re.findall(pattern, text)
if match:
    print("match found:", match)
else:
    print("match not found")