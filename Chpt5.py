#####################################
## Alice Hsu
## Chapter 5: Programming Exercise
## HW Pg 344: #3, 4, 7, 9, 12
#####################################


## How Much Insurance?
replacement=float(input("Enter the replacement cost of the building: $"))
insurance=0.80
cost=replacement*insurance
print(f"You should buy at least ${cost:.2f} in insurance!")

## Automobile Costs
loan=float(input("Enter the monthly loan payment: $"))
insurance=float(input("Enter the monthly insurance cost: $"))
gas=float(input("Enter the monthly gas cost: $"))
oil=float(input("Enter the monthly oil cost: $"))
tires=float(input("Enter the monthly tires cost: $"))
maintenance=float(input("Enter the monthly maintenance cost: $"))

monthly_total=loan+insurance+gas+oil+tires+maintenance
annual_total=monthly_total*12
print(f"Total monthly cost: ${monthly_total}")
print(f"Total annual cost: ${annual_total}")

## Stadium Seating
class_a=int(input("Enter the number of Class A tickets sold: "))
class_b=int(input("Enter the number of Class B tickets sold: "))
class_c=int(input("Enter the number of Class C tickets sold: "))
price_a = 20
price_b = 15
price_c = 10

income_a=class_a*price_a
income_b=class_b*price_b
income_c=class_c*price_c
total=income_a+income_b+income_c
print(f"Total income generated from ticket sales: ${total}")

## Monthly Sales Taх
total=float(input("Enter the total sales for the month: "))
state_rate=0.05
county_rate=0.025
state_tax=total*state_rate
county_tax=total*county_rate
total_tax=state_tax+county_tax

print(f"County sales tax: ${county_tax}")
print(f"State sales tax: ${state_tax}")
print(f"Total sales tax: ${total_tax}")

## Маximum of Two Values
def max(a,b):
    if a>b:
        return a
    else:
        return b

num1=int(input("Enter the first integer: "))
num2=int(input("Enter the second integer: "))
greater=max(num1,num2)
print(f"The greater value is: {greater}")

##Pseudocode
DEFINE FUNCTION max(a,b)
    IF a>b THEN
        RETURN a
    ELSE
        RETURN b
END FUNCTION

START
DISPLAY "Enter the first integer"
    READ num1
DISPLAY "Enter the second integer"
    READ num2
SET greater TO max(num1, num2)
DISPLAY "The greater value is:"
DISPLAY max
END
