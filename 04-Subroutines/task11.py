def factorial(f):
    if f==0 or f==1:
        return 1
    elif f> 1:
        return f*factorial(f-1)
x=10
print(f"{x}! = {factorial(x)}")
print(factorial(4))
