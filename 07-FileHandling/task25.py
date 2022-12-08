import re
mes = "To be, or not to be, that is the question"
vowels = re.findall("[aeiou]",mes)
print(vowels)
print(len(vowels))



