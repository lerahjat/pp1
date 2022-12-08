import re
mes = "To be, or not to be, that is the question"
words = len(re.findall('\w+', mes))
print(words)