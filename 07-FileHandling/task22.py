with open("file_2.txt", "w") as f:
    for i in range(1,10):
        f.write(str(i) + " ")
        f.write(str(i**2) + " ")
        f.write(str(i ** 3) + " " + "\n")