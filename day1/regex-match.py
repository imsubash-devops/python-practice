#a match expression is a pattern that is used to search for and match specific strings within a larger text. 
import re

text = "quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match") 
