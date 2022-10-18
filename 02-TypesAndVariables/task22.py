amount = float(input("Your amount:"))
x = 23
vat = (amount*x)/(100+x)
format_vat =("VAT is = {:.2f}".format( vat ))
print(f"Your amount is {amount}, {format_vat}")