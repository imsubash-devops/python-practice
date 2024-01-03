import re

text = "quick brown fox"
pattern = r"quick"

search = re.search(pattern, text)
if search:
    print("Match found:", search.group())
else:
    print("No match") 