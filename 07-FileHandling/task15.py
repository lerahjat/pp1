with open('15file.txt', 'r') as f:
    for i in range(0, 5):
        first_line = f.readline()
        print(first_line)
    a = input("Press enter to continue")
    for i in range(5, 10):
        first_line = f.readline()
        print(first_line)
    a = input("Press enter to continue")
    for i in range(10, 15):
        first_line = f.readline()
        print(first_line)
    a = input("Press enter to continue")
    for i in range(15, 20):
        first_line = f.readline()
        print(first_line)