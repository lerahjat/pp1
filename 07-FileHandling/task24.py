import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
# complete the program code
print(temperatures)
sum = 0
for i in temperatures:
    sum += int(i)

mid = sum/len(temperatures)
print(mid)


