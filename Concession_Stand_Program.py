# concession stand program 

menu = {"popcorn": 200,
        "soda": 100,
       "nachos": 120,
       "hotdog": 150,
       "candy": 50,
       "chocolate": 60,
       "pizza": 500,
       "pretzel": 70,
       "ice Cream": 75,
       "juice": 80}

cart =[]
total = 0

print("--------- MENU ---------")
for key , value in menu.items():
    print(f"{key:10} : ₹{value:.2f}")
print("-------------------------")

while True:
    food = input("Select an items (q to quit):  ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------- YOUR ORDER -------")
for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ₹{total:.2f}")



