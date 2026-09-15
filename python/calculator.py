a = int(input(" Enter no 1 :"))
b = int(input(" Enter no 2 :"))
op = input("Enter operator :")

match op:
    case "+":
        print("Addition", a+b)
    case "-":
        print("Substraction", a-b)
    case "*":
        print("Multiplication", a*b)
    case "/":
        print("Division", a/b)
    case "%":
        print("Modulus", a%b)
    case _:
        print("invalid operator")


