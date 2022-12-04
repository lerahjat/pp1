with open("shopping.txt", "a") as f:
    item = input("Enter item:")
    f.write(f"{item}\n")