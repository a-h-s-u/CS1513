#####################################
## Alice Hsu
## Chapter 3: Programming Exercise
## HW Pg 201: #2, 5, 8, 11, 17
#####################################


##Areas of Rectangles
length1=float(input("Enter the length of the first rectangle: "))
width1=float(input("Enter the width of the first rectangle: "))
length2=float(input("Enter the length of the second rectangle: "))
width2=float(input("Enter the width of the second rectangle: "))
area1=length1*width1
area2=length2*width2
if area1>area2:
    print("The first rectangle has the greater area.")
elif area2>area1:
    print("The second rectangle has a greater area.")
elif area1==area2:
    print("The areas of both rectangles are the same.")
else:
    print("not coded")

##Mass and Weight
mass=float(input("Enter the object\'s mass in kilograms: "))
weight=mass*9.8
if weight>500:
    print("This object is too heavy!")
elif weight<100:
    print("This object is too light!")
else:
    print(f"The object weighs {weight:.1f} newtons.")

##Hot Dog Cookout Calculator
persons=int(input("Enter the number of people attending the cookout: "))
hotdogs=int(input("Enter the number of hotdogs each person will be given: "))
total=persons*hotdogs
hotdogs_package=10
buns_package=8
min_hotdogs=float(total/hotdogs_package)
min_buns=float(total/buns_package)
if min_hotdogs%1!=0:
    min_hotdogs=int(min_hotdogs+1)
if min_buns%1!=0:
    min_buns=int(min_buns+1)
leftover_hotdogs=min_hotdogs*hotdogs_package-total
leftover_buns=min_buns*buns_package-total
print(f"The minimum number of packages of hot dogs required is {min_hotdogs:.0f}.\n"
      f"The minimum number of packages of hot dog buns required is {min_buns:.0f}.\n"
      f"The number of hot dogs that will be left over is {leftover_hotdogs:.0f}.\n"
      f"The number of hot dog buns that will be left over is {leftover_buns:.0f}.")

##Book Club Points
books=int(input("Welcome to Serendipity Booksellers book club!\n"
                "Enter the number of books purchased this month: "))
if books==0:
    points=1
elif books==2:
    points=5
elif books==4:
    points=15
elif books==6:
    points=30
elif books>=8:
    points=60
else:
    print("invalid number")
print(f"You have been awarded {points} points!")

##Wi-Fi Diagnostic Tree
response=input("Reboot the computer and try to connect.\n"
               "Did that fix the problem? (yes/no): ").lower()
if response == "no":
    input("Reboot the router and try to connect.\n"
          "Did that fix the problem? (yes/no): ").lower()
    if response == "no":
        input("Make sure the cables between the router and modem are plugged in firmly.\n"
              "Did that fix the problem? (yes/no): ").lower()
        if response == "no":
            input("Move the router to a new location.\n"
                  "Did that fix the problem? (yes/no): ").lower()
            if response == "no":
                print("Get a new router.")
