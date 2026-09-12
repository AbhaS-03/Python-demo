m = int(input("Enter marks: "))

if m <= 0 or m >= 100:
    print("Grade Invalid")

elif m >= 90:
    print("Grade O")

elif m >= 80:
    print("Grade A")

elif m >= 65:
    print("Grade B")

elif m >= 35:
    print("Grade C")

else:
    print("Grade F")