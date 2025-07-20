#####################################
## Alice Hsu
## Chapter 9: Programming Exercise
## HW Pg 574 #1, 2, 3, 7, 8
#####################################


## Course Information
courses_rooms={
    "CS101":"3004",
    "CS102":"4501",
    "CS103":"6755",
    "NT110":"1244",
    "CM241":"1411"
}
courses_instructors={
    "CS101":"Haynes",
    "CS102":"Alvarado",
    "CS103":"Rich",
    "NT110":"Burke",
    "CM241":"Lee"
}
courses_times={
    "CS101":"8:00 a.m.",
    "CS102":"9:00 a.m.",
    "CS103":"10:00 a.m.",
    "NT110":"11:00 a.m.",
    "CM241":"1:00 p.m."
}

course=input("Enter course number: ")
if course in courses_rooms:
    print(f"Room: {courses_rooms.get(course)}")
    print(f"Instructor: {courses_instructors.get(course)}")
    print(f"Meeting Time: {courses_times.get(course)}")
else:
    print("Course not found.")

## Pseudocode
START
DEFINE dictionary courses_rooms and course-room pairs
DEFINE dictionary courses_instructors and course-instructor pairs
DEFINE dictionary courses_times and course-time pairs
PRINT "Enter course number: "
GET input as course
IF course exists in courses_rooms THEN
    PRINT "Room: " + room for the course from courses_rooms
    PRINT "Instructor: " + instructor for the course from courses_instructors
    PRINT "Meeting Time: " + time for the course from courses_times
ELSE
    PRINT "Course not found."
END

## Capital Quiz
import random
us_states_capitals={
    "Alabama":"Montgomery",
    "Alaska":"Juneau",
    "Arizona":"Phoenix",
    "Arkansas":"Little Rock",
    "California":"Sacramento",
    "Colorado":"Denver",
    "Connecticut":"Hartford",
    "Delaware":"Dover",
    "Florida":"Tallahassee",
    "Georgia":"Atlanta",
    "Hawaii":"Honolulu",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Indiana":"Indianapolis",
    "Iowa":"Des Moines",
    "Kansas":"Topeka",
    "Kentucky":"Frankfort",
    "Louisiana":"Baton Rouge",
    "Maine":"Augusta",
    "Maryland":"Annapolis",
    "Massachusetts":"Boston",
    "Michigan":"Lansing",
    "Minnesota":"Saint Paul",
    "Mississippi":"Jackson",
    "Missouri":"Jefferson City",
    "Montana":"Helena",
    "Nebraska":"Lincoln",
    "Nevada":"Carson City",
    "New Hampshire":"Concord",
    "New Jersey":"Trenton",
    "New Mexico":"Santa Fe",
    "New York":"Albany",
    "North Carolina":"Raleigh",
    "North Dakota":"Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington":"Olympia",
    "West Virginia":"Charleston",
    "Wisconsin":"Madison",
    "Wyoming":"Cheyenne"
}

states=list(us_states_capitals.keys())
correct=0
incorrect=0
for i in range(5):
    state=random.choice(states)
    answer=input(f"What is the capital of {state}? ")
    if answer.strip().lower()==us_states_capitals.get(state).lower():
        print("Correct!")
        correct+=1
    else:
        print(f"Wrong! The correct answer is {us_states_capitals.get(state)}")
        incorrect+=1
print(f"Correct: {correct}\n"
      f"Incorrect: {incorrect}")

## File Encryption and Decryption
codes={ 'A':'1',  'B':'2',  'C':'3',  'D':'4',  'E':'5',  'F':'6',
          'G':'7',  'H':'8',  'I':'9',  'J':'0',  'K':'!',  'L':'@',
          'M':'#',  'N':'$',  'O':'%',  'P':'^',  'Q':'&',  'R':'*',
          'S':'(',  'T':')',  'U':'-',  'V':'_',  'W':'+',  'X':'=',
          'Y':'{',  'Z':'}',  'a':'[',  'b':']',  'c':':',  'd':';',
          'e':'"',  'f':"'",  'g':'<',  'h':'>',  'i':'?',  'j':'/',
          'k':'`',  'l':'~',  'm':'|',  'n':'\\', 'o':',',  'p':'.',
          'q':'a',  'r':'b',  's':'c',  't':'d',  'u':'e',  'v':'f',
          'w':'g',  'x':'h',  'y':'i',  'z':'j'
}
input_file="plain.txt"
output_file="encrypted.txt"
f=open("input_file","w")
f.write("Welcome Bronchos")
f.close()

def encrypt_file(input_file_name,output_file_name):
    in_file=open(input_file_name,"r")
    out_file=open(output_file_name,"w")
    for line in in_file:
        for character in line:
            if character in codes:
                 out_file.write(codes.get(character))
            else:
                 out_file.write(character)
    in_file.close()
    out_file.close()
    print(f"File {input_file_name} encrypted to {output_file_name}.")
def decrypt_file(input_file_name):
    in_file=open(input_file_name,"r")
    reverse={v:k for k,v in codes.items()}
    decrypted_text=""
    for line in input_file_name:
        for character in line:
            decrypted_text+=reverse.get(character,character)
    in_file.close()
    print("Decrypted text:")
    print(decrypted_text)

encrypt_file(input_file,output_file)
decrypt_file(output_file)

# 7. World Series Winners
team_year= {
    1903:"Boston Americans",
    1905:"New York Giants",
    1906:"Chicago White Sox",
    1907:"Chicago Cubs",
    1908:"Chicago Cubs",
    1909:"Pittsburgh Pirates",
    1910:"Philadelphia Athletics",
    1911:"Philadelphia Athletics",
    1912:"Boston Red Sox",
    1913:"Philadelphia Athletics",
    1914:"Boston Braves",
    1915:"Boston Red Sox",
    1916:"Boston Red Sox",
    1917:"Chicago White Sox",
    1918:"Boston Red Sox",
    1919:"Cincinnati Reds",
    1920:"Cleveland Indians",
    1921:"New York Giants",
    1922:"New York Giants",
    1923:"New York Yankees",
    1924:"Washington Senators",
    1925:"Pittsburgh Pirates",
    1926:"St. Louis Cardinals",
    1927:"New York Yankees",
    1928:"New York Yankees",
    1929:"Philadelphia Athletics",
    1930:"Philadelphia Athletics",
    1931:"St. Louis Cardinals",
    1932:"New York Yankees",
    1933:"New York Giants",
    1934:"St. Louis Cardinals",
    1935:"Detroit Tigers",
    1936:"New York Yankees",
    1937:"New York Yankees",
    1938:"New York Yankees",
    1939:"New York Yankees",
    1940:"Cincinnati Reds",
    1941:"New York Yankees",
    1942:"St. Louis Cardinals",
    1943:"New York Yankees",
    1944:"St. Louis Cardinals",
    1945:"Detroit Tigers",
    1946:"St. Louis Cardinals",
    1947:"New York Yankees",
    1948:"Cleveland Indians",
    1949:"New York Yankees",
    1950:"New York Yankees",
    1951:"New York Yankees",
    1952:"New York Yankees",
    1953:"New York Yankees",
    1954:"New York Giants",
    1955:"Brooklyn Dodgers",
    1956:"New York Yankees",
    1957:"Milwaukee Braves",
    1958:"New York Yankees",
    1959:"Los Angeles Dodgers",
    1960:"Pittsburgh Pirates",
    1961:"New York Yankees",
    1962:"New York Yankees",
    1963:"Los Angeles Dodgers",
    1964:"St. Louis Cardinals",
    1965:"Los Angeles Dodgers",
    1966:"Baltimore Orioles",
    1967:"St. Louis Cardinals",
    1968:"Detroit Tigers",
    1969:"New York Mets",
    1970:"Baltimore Orioles",
    1971:"Pittsburgh Pirates",
    1972:"Oakland Athletics",
    1973:"Oakland Athletics",
    1974:"Oakland Athletics",
    1975:"Cincinnati Reds",
    1976:"Cincinnati Reds",
    1977:"New York Yankees",
    1978:"New York Yankees",
    1979:"Pittsburgh Pirates",
    1980:"Philadelphia Phillies",
    1981:"Los Angeles Dodgers",
    1982:"St. Louis Cardinals",
    1983:"Baltimore Orioles",
    1984:"Detroit Tigers",
    1985:"Kansas City Royals",
    1986:"New York Mets",
    1987:"Minnesota Twins",
    1988:"Los Angeles Dodgers",
    1989:"Oakland Athletics",
    1990:"Cincinnati Reds",
    1991:"Minnesota Twins",
    1992:"Toronto Blue Jays",
    1993:"Toronto Blue Jays",
    1995:"Atlanta Braves",
    1996:"New York Yankees",
    1997:"Florida Marlins",
    1998:"New York Yankees",
    1999:"New York Yankees",
    2000:"New York Yankees",
    2001:"Arizona Diamondbacks",
    2002:"Anaheim Angels",
    2003:"Florida Marlins",
    2004:"Boston Red Sox",
    2005:"Chicago White Sox",
    2006:"St. Louis Cardinals",
    2007:"Boston Red Sox",
    2008:"Philadelphia Phillies",
    2009:"New York Yankees"
}
team_wins= {
    "New York Yankees":27,
    "St. Louis Cardinals":10,
    "Boston Red Sox":6,
    "New York Giants":5,
    "Philadelphia Athletics":5,
    "Pittsburgh Pirates":5,
    "Cincinnati Reds":5,
    "Los Angeles Dodgers":5,
    "Detroit Tigers":4,
    "Oakland Athletics":4,
    "Baltimore Orioles":3,
    "Chicago White Sox":3,
    "Cleveland Indians":2,
    "New York Mets":2,
    "Philadelphia Phillies":2,
    "Minnesota Twins":2,
    "Toronto Blue Jays":2,
    "Florida Marlins":2,
    "Chicago Cubs":2,
    "Boston Americans":1,
    "Boston Braves":1,
    "Washington Senators":1,
    "Brooklyn Dodgers":1,
    "Milwaukee Braves":1,
    "Kansas City Royals":1,
    "Atlanta Braves":1,
    "Arizona Diamondbacks":1,
    "Anaheim Angels":1
}

year=int(input("Enter a year between 1903 and 2009: "))
if year == 1904 or year == 1994:
    print(f"No World Series was held in {year}.")
elif year in team_year:
    team=team_year[year]
    wins=team_wins.get(team,0)
    print(f"The {team} won in {year} and have won {wins} times.")
else:
    print("Year out of range or invalid.")

## Name and Email Addresses
import pickle
filename = "email_dict.pkl"
email_dict = {}

exists=input("Does the email data file exist? (yes/no): ").lower()
if exists=="yes":
    file=open(filename,"rb")
    email_dict=pickle.load(file)
    file.close()
else:
    email_dict={}
    
def show_menu():
    print("\nMenu:")
    print("1. Look up email address")
    print("2. Add new name and email")
    print("3. Change existing email")
    print("4. Delete name and email")
    print("5. Exit")
while True:
    show_menu()
    choice=input("Enter choice (1-5): ")
    if choice=="1":
        name=input("Enter name to look up: ")
        if name in email_dict:
            print(f"Email for {name} is {email_dict[name]}")
        else:
            print(f"{name} not found.")
    elif choice=="2":
        name=input("Enter new name: ")
        email=input("Enter email address: ")
        if name in email_dict:
            print(f"{name} already exists.")
        else:
            email_dict[name]=email
            print(f"Added {name}.")
    elif choice=="3":
        name=input("Enter name to change email: ")
        if name in email_dict:
            email=input("Enter new email address: ")
            email_dict[name]=email
            print(f"Email updated for {name}.")
        else:
            print(f"{name} not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in email_dict:
            del email_dict[name]
            print(f"Deleted {name}.")
        else:
            print(f"{name} not found.")
    elif choice=="5":
        file=open(filename, "wb")
        pickle.dump(email_dict, file)
        file.close()
        print("Data saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")
