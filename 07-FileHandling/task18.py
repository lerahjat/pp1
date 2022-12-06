with open("MeatAndFish.txt", "r") as f1:
    with open("GrainsAndBread.txt", "r") as f:
        with open("shoppinglist.txt", "w") as f3:
            for line in f1:
                f3.write(line)
            for line in f:
                f3.write(line)
            f3.close()





