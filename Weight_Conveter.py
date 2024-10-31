# weight coveter

weight = float(input("Enter your weight: "))
unit =input("Kilograms or Pound ? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 2)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit ="Kgs."
    print(f"Your weight is {round(weight, 2)} {unit}")

else:
    print(f"{unit} was not valid")

print(f"Your weight is {round(weight, 2)} {unit}")

