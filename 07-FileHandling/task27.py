import re

with open("task27.txt", "r") as f:
    data = f.read()
    words = re.findall(r"\w{6,}", data)
    for i in words:

        print(i)
