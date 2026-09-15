correct_pass = "some_pass"
while True:
    string = input("Enter a String : ")
    if string == correct_pass:
        break
    else:
        print("Wrong Password try again !")
print("Password Matched")