age = int(input("Enter age :"))
t_price = int(input("Enter price"))

if age <= 12:
   a = 1000*(10 /100)
   dis = t_price - a
   print ("hey you got a discout in ticket price ")
   print("Amt to be paid is " ,dis)
else:
    print("Amt to be paid is " ,t_price)