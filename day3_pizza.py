print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# How much their bill is based on their size
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You type the wrong input.")

# Want pepperoni on your pizza?
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add to the bill the extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")