def Power(x, y):
    if y>0:
        return x * Power(x, y-1)
    else:
        return 1
print(Power(2, 4))

