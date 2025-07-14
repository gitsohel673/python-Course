try:

    FileOpen = open('output.txt','w')
    str1 = input("Enter to write to the file: ")
    FileOpen.write(str1)
    print("Data successfully written to output.txt")
    FileOpen.close()

    FileOpen = open('output.txt','a')
    str2 = input("Enter additional text to append: ")
    FileOpen.write("\n"+ str2)
    print("data successfully appended.")

    FileOpen = open('output.txt','r+')
    readline = FileOpen.read()
    print(readline)

except:
    print("There are a problem!")