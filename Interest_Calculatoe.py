# compound interest calculator 

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in year: "))
    if rate < 0:
        print("time can't be less than zero")
    else:
        break


total = principal * pow((1 + rate / 100),time)
print(f"Balance after {time} year/s: ₹{total:.2f}")
