def sumall(t):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t > 1:
        return t+sumall(t-1)

print(sumall(6))