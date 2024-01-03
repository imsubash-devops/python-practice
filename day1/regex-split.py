import re

text = "ai,ui,ux,ml"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)