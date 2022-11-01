x = int(input("x"))
y = int(input("y"))
if x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the 1 quadrant of the coordinate system")
elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the 4 quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the 3 quadrant of the coordinate system")
else:
    print(f"Point P({x},{y}) is in the 2 quadrant of the coordinate system")
