student = {"alice": 54, "sohel" : 81, "ashok" : 56, "narayan" : 36}

studentName = input("Enter Student Name :").lower()

if studentName in student :
    print(studentName, " marks :" , student[studentName])
else:
    print("Student not found")