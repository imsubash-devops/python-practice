import re

text = "I am Software Engineer"
pattern = r"Software"

replacement = "DevOps"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)