pin = "0805"

for number in range(3):
    pinTry = str(input("Enter your PIN code: "))
    if pinTry != pin:
        print("Incorrect PIN")
    elif pinTry == pin:
        print("Correct")
        break
    if number >= 2 and pinTry != pin:
        print("Sorry, your payment car has been blocked")
        break
