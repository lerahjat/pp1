a = float(input("a side:"))
b = float(input("b side:"))
c = float(input("c side:"))
p = (a+b+c)/2
area = ((p*(p-a)*(p-b)*(p-c)) ** (1/2))

print(f"The area of triangle {area}")