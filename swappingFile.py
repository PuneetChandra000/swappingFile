def swapFileData() :
    file1 = open("sample1.txt", 'r')
    a = file1.read()

    file2 = open("sample2.txt")
    b = file2.read()

    file1 = open("sample1.txt", 'w')
    print(file1.write(b))

    file2 = open("sample2.txt", 'w')
    print(file2.write(a))

swapFileData()