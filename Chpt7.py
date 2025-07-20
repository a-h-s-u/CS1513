#####################################
## Alice Hsu
## Chapter 7: Programming Exercise
## HW Pg 482 #3, 7, 10, 11, 13
#####################################


## Rainfall Statistics
calendar=("January","February","March","April","May","June",
        "July","August","September","October","November","December")
rainfall=[]
for month in calendar:
    amount = float(input("Enter amount of total rainfall for " + month + ": "))
    rainfall.append(amount)

total=sum(rainfall)
average=total/len(rainfall)
max_rain=max(rainfall)
min_rain=min(rainfall)
max_month=calendar[rainfall.index(max_rain)]
min_month=calendar[rainfall.index(min_rain)]

print(f"Total rainfall for the year: {total}\n"
      f"Average monthly rainfall: {average}\n"
      f"Month with the highest rainfall: {max_month} with {max_rain}\n"
      f"Month with the lowest rainfall: {min_month} with {min_rain}")

## Driver's License Exam
answers=[
    "A","C","A","A","D","B","C","A","C","B",
    "A","D","C","A","D","C", "B", "B", "D", "A"
]
student=[
    "B","C","A","A","D","B","C","A","C","B",
    "A","D","C","A","D","C", "B", "B", "D", "A"
]

file=open("student.txt","w")
for answer in student:
    file.write(answer+"\n")
file.close()

file=open("student.txt","r")
student=[]
for line in file:
    student.append(line.strip().upper())
file.close()

correct=0
wrong=[]
for bubble in range(len(answers)):
    if student[bubble]==answers[bubble]:
        correct+=1
    else:
        wrong.append(bubble+1)
if correct>=15:
    print("YOU PASSED!!!")
else:
    print("YOU FAILED :(")

print(f"Total correct answers: {correct}\n"
      f"Total incorrect answers: {20-correct}\n"
      f"Questions answered incorrectly: ")
for num in wrong:
    print(num)

## World Series Champions
winners=[
    "San Francisco Giants",
    "St. Louis Cardinals",
    "San Francisco Giants",
    "Boston Red Sox",
    "San Francisco Giants",
    "Kansas City Royals",
    "Chicago Cubs",
    "Houston Astros",
    "Boston Red Sox",
    "Washington Nationals",
    "Los Angeles Dodgers",
    "Atlanta Braves",
    "Houston Astros",
    "Texas Rangers",
    "Los Angeles Dodgers"
]

file=open("WorldSeriesWinners.txt","w")
for team in winners:
    file.write(team+"\n")
file.close()

file=open("WorldSeriesWinners.txt","r")
winners=[]
for line in file:
    winners.append(line.strip())
file.close()

team=input("Enter the name of a team: ")
count = 0
for name in winners:
    if name==team:
        count+=1
print(f"The team {team} won the World Series {count} times!")

## Lo Shu Magic Square
magic_square=[
    [4,9,2],
    [3,5,7],
    [8,1,6]
]

def lo_shu(square):
    numbers=[]
    for row in square:
        for num in row:
            if num<1 or num>9 or num in numbers:
                return False
            numbers.append(num)

    added=15
    for row in square:
        if sum(row)!=added:
            return False
    for col in range(3):
        total=square[0][col]+square[1][col]+square[2][col]
        if total!=added:
            return False

    diag_left=square[0][0]+square[1][1]+square[2][2]
    diag_right=square[0][2]+square[1][1]+square[2][0]
    if diag_left!=added or diag_right!=added:
        return False
    else:
        return True

if lo_shu(magic_square):
    print("The list is a Lo Shu Magic Square!")
else:
    print("The list is not a Lo Shu Magic Square!")

## Magic 8 Ball
prompts=[
    "Yes, of course!",
    "Without a doubt, yes.",
    "You can count on it.",
    "For sure!",
    "Ask me later.",
    "I'm not sure.",
    "I can't tell you right now.",
    "I'll tell you after my nap.",
    "No way!",
    "I don't think so.",
    "Without a doubt, no.",
    "The answer is clearly NO."
]

file=open("8_ball_responses.txt","w")
for response in prompts:
    file.write(response+"\n")
file.close()

file=open("8_ball_responses.txt","r")
response=[]
for line in file:
    response.append(line.strip())
file.close()

print("Let's start the Magic 8 Ball!")
print("Ask a yes or no question, or type 'quit' to stop.")

import random
while True:
    question=input("Your question: ")
    if question.lower()=="quit":
        print("Ba-Bye!")
        break
    answer=random.choice(response)
    print(f"Magic 8 Ball says: {answer}")

## Pseudocode
START
CREATE list of 12 Magic 8 Ball responses
OPEN file called "8_ball_responses.txt"
FOR each response IN list:
    WRITE response to  file
CLOSE file

OPEN "8_ball_responses.txt"
CREATE  empty list
FOR each line IN  file:
    DELETE newline characters
    ADD line to the list
CLOSE file

PRINT "Let's start the Magic 8 Ball!"
PRINT "Ask a yes or no question, or type 'quit' to stop."

REPEAT:
    ASK user to INPUT
        IF "quit":
            PRINT goodbye
            STOP loop
        ELSE:
            SELECT random response FROM list
            PRINT the random response.
END
