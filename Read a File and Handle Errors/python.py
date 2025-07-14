try:
    fileName = open('sample1.txt')
    print(fileName.read())

    fileName.close()
except FileNotFoundError:
    print(f"the file 'sample1.txt' was not found")