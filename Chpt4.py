#####################################
## Alice Hsu
## Chapter 4: Programming Exercise
## HW Pg 259: #2, 3, 7, 10, 13
#####################################


## Calories Burned
burn_rate=4.2
for mins in [10, 15, 20, 25, 30]:
    calories=mins*burn_rate
    print(f"Number of calories burned after {mins} minutes: {calories}")

## Budget Analysis
budget=float(input("Enter the amount you budgeted for this month: "))
total=0
while True:
    expense=float(input("Enter an expense: "))
    if expense==0:
        break
    total+=expense
difference=budget-total
if difference>0:
    print(f"Amount UNDER budget: ${difference:.2f}.")
elif difference<0:
    print(f"Amount OVER budget: ${-difference:.2f}.")
else:
    print("You exactly met your budget! Keep being financial savvy.")

## Pennies for Pay
days=int(input("Enter the number of days worked: "))
while days<1:
    print("You need to work for at least one day!")
    days=int(input("Enter the number of days worked: "))
salary=1
total=0

print("\nDay\tSalary"
      "\n________________"
      "\n")
for day in range(1,days+1):
    print(f"{day}"
          f"\t${salary/100:.2f}")
    total+=salary
    salary*=2
print("________________"
      "\n"
      f"\nTotal pay: ${total/100:.2f}")

## Tuition Increase
tuition=8000
years=5

print("Year\tProjected Tuition")
print("___________________________")
for year in range(1,years+1):
    tuition+=(tuition*0.03)
    print(f"{year}"
          f"\t${tuition:.2f}")
##Pseudocode
SET tuition=8000
SET years=5
SET rate=0.03
CALCULATE increased cost
    FOR year FROM 1 TO years DO:
    tuition=tuition+(tuition*rate)
DISPLAY years
DISPLAY total tuition

## Population
population=float(input("Starting number of organisms: "))
increase=float(input("Average daily percent increase: "))
rate=increase/100
days=int(input("Number of days to multiply: "))

print("\nDay"
      "\tApproximate Population")
print("_________________________________")
for day in range(1,days+1):
    print(f"{day}"
          f"\t{population}")
    population+=population*rate
