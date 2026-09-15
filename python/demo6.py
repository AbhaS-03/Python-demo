role=input("enter the role: ")
age = int(input("Enter age : "))

print("Eligible :", role=='student' or 'Student' and age <21)