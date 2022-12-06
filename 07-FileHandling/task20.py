with open("file_1.txt", "w") as f_1:
    for i in range(1,51):
        print(i)
        f_1.write(str(i) + '\n')