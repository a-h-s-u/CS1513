####################################
## Alice Hsu
## Chapter 1&2: Programming Exercises
## HW Pg 146 #1, 2, 3, 4, 5, 10
####################################


##Personal Information
name=input("What is your name? ")
address=input("What is your address? ")
secondary_address=input("What is the city, state, and ZIP? ")
telephone=input("What is your telephone number? ")
major=input("What is your college major? ")
print("Name:", name,
      "\nAddress:", address, secondary_address,
      "\nTelephone Number:", telephone,
      "\nCollege Major:", major)

##Sales Prediction
total_sales=float(input("Enter the projected amount of total sales: $"))
annual_rate=0.23
profit=total_sales*annual_rate
print("Your annual profit made is: $",profit)

##Land Calculation
land=int(input("Enter the total square feet in the tract of land: "))
acres=land/43560
print(f"The number of acres in the tract is {acres:.2f}")

##Total Purchase
item1=float(input("What is the price for your first item? "))
item2=float(input("What is the price for your second item? "))
item3=float(input("What is the price for your third item? "))
item4=float(input("What is the price for your fourth item? "))
item5=float(input("What is the price for your fifth item? "))
subtotal=item1+item2    +item3+item4+item5
sales_tax=0.07
total=subtotal+(subtotal*sales_tax)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total: ${total:.2f}",
      "\nThanks for shopping at UCO student stores!")

##Distance Traveled
print("The car is traveling at 70 miles per hour down the interstate.")
speed=70
time1=6
time2=10
time3=15
distance1=speed*time1
distance2=speed*time2
distance3=speed*time3
print(f"The distance the car will travel in {time1} hours is {distance1}"
      f"\nThe distance the car will travel in {time2} hours is {distance2}"
      f"\nThe distance the car will travel in {time3} hours is {distance3}")

##Ingredient Adjuster
amount=int(input("How many cookies would you like to make? "))
recipe=48
sugar=(amount*1.5)/recipe
butter=(amount*1)/recipe
flour=(amount*2.75)/recipe
print(f"For {amount} number of cookies, the recipe calls for the following ingredients:"
      f"\n{sugar:.2f} cups of sugar"
      f"\n{butter:.2f} cups of butter"
      f"\n{flour:.2f} cups of flour")
