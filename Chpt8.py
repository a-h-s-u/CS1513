#####################################
## Alice Hsu
## Chapter 8: Programming Exercise
## HW Pg 516   #1, 5, 8, 12, 13
#####################################


## Initials
full_name=input("Enter your first, middle, last name: ")
name=full_name.split()
first_initial=name[0][0]
middle_initial=name[1][0]
last_initial=name[2][0]

print(first_initial+"."+middle_initial+"."+last_initial+".")


## Alphabetic Telephone Number Translator
letter_number={
    "A":"2","B":"2","C":"2","D":"3","E":"3","F":"3",
    "G":"4","H":"4","I":"4","J":"5","K":"5","L":"5",
    "M":"6","N":"6","O":"6","P":"7","Q":"7","R":"7",
    "S":"7","T":"8","U":"8","V":"8","W":"9","X":"9",
    "Y":"9","Z":"9"
}

phone=input("Enter a telephone number in the format XXX-XXX-XXXX: ")
converted_phone=""
for num in phone:
    upper_num=num.upper()
    if upper_num in letter_number:
        converted_phone+=letter_number[upper_num]
    else:
        converted_phone+=num
print("Converted phone number:",converted_phone)


## Sentence Capitalizer
def capitalize(text):
    result=""
    capitalize_next=True
    for character in text:
        if capitalize_next and character.isalpha():
            result+=character.upper()
            capitalize_next=False
        else:
            result+=character
        if character==".":
            capitalize_next=True
    return result

sentence=input("Enter a sentence: ")

modified=capitalize(sentence)
print("Modified sentence:")
print(modified)


## Pig Latin
def pig_latin(sentence):
    words=sentence.split()
    pig_latin_words=[]
    for word in words:
        if len(word)>1:
            pig_word=word[1:]+word[0]+"AY"
        else:
            pig_word=word+"AY"
        pig_latin_words.append(pig_word)
    return " ".join(pig_latin_words)

sentence=str(input("Enter a sentence: "))
pig_latin_sentence=pig_latin(sentence.upper())
print("Pig Latin:",pig_latin_sentence)

##Psuedocode
#START
#DEFINE pig_latin(sentence)
#    SPLIT  sentence into a list
#    CREATE empty list called pig_latin_words
#    FOR each word in list of words:
#        IF word > 1 letter:
#            TAKE word without first letter
#            ADD first letter to end
#            ADD "AY" at the end
#            STORE as pig_word
#       ELSE:
#            ADD "AY" to end of word
#            STORE as pig_word
#        ADD pig_word to pig_latin_words list
#    JOIN all pig_latin_words into a single string with spaces
#    RETURN result
#
#ASK the user to enter a sentence
#CONVERT sentence to uppercase
#CALL the pig_latin function with the sentence
#DISPLAY result
#END


## Powerball Lottery
data = [
    [17,22,36,37,52,24],
    [10,15,25,34,43,18],
    [17,22,30,35,52,24],
    [6,22,36,45,49,13],
    [17,20,36,37,52,9],
    [1,17,36,40,50,24],
    [3,5,36,37,52,14],
    [17,36,37,50,55,24],
    [11,12,17,36,44,24],
    [17,36,41,42,60,26],
]

main={}
powerball={}
last_seen={}

i=1
while i<=69:
    main[i]=0
    last_seen[i]=-1
    i+=1
i=1
while i<=26:
    powerball[i]=0
    i+=1

draw_num = 0
for line in data:
    j = 0
    while j < 5:
        num=line[j]
        main[num]=main[num]+1
        last_seen[num]=draw_num
        j+=1
    pb=line[5]
    powerball[pb]=powerball[pb] + 1
    draw_num+=1

# Get most common and least common (manual sort)
main_items=[]
for number in main:
    main_items.append([number, main[number]])

i=0
while i<len(main_items):
    j=i+1
    while j<len(main_items):
        if main_items[j][1]>main_items[i][1]:
            temp=main_items[i]
            main_items[i]=main_items[j]
            main_items[j]=temp
        j+=1
    i+=1

print("10 Most Common Main Numbers:")
count=0
while count<10:
    print(f"Number {main_items[count][0]}: {main_items[count][1]} times")
    count+=1

overdue=[]
for number in last_seen:
    overdue.append([number,last_seen[number]])
i=0
while i<len(overdue):
    j = i + 1
    while j < len(overdue):
        if overdue[j][1]<overdue[i][1]:
            temp=overdue[i]
            overdue[i]=overdue[j]
            overdue[j]=temp
        j+=1
    i+=1

print("\n10 Most Overdue Numbers:")
count=0
while count<10:
    print(f"Number {overdue[count][0]}: Last seen on draw {overdue[count][1] + 1}")
    count+=1

print("\nMain Number Frequencies (1–69):")
i=1
while i<=69:
    print(str(i)+":"+str(main[i]),end="  ")
    if i%10==0:
        print()
    i+=1

print("\n\nPowerBall Number Frequencies (1–26):")
i=1
while i<=26:
    print(str(i)+":"+str(powerball[i]),end="  ")
    if i%10==0:
        print()
    i+=1
