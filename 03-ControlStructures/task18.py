money = int(input("Enter the amount in PLN:"))
def coins(money):
    c5 = money // 5
    c2 = (money%5)//2
    c1 = ((money % 5)%2) //1
    return(f"5 zl = {c5},2 zl = {c2}, 1 zl = {c1}")
print(coins(money))
