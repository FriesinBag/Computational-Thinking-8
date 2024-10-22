# Intro 
Basketball_IQ_Points = 2
No_Basketball_IQ_Points = 0
Some_Basketball_IQ_Points = 1


# Middle
# question 1:
answer = input("How many different team did Derrick Rose play for? A:5 B:6 C:4")
if answer == "B":
    Basketball_IQ_Points += 2
elif answer in ["A","C"]:
    No_Basketball_IQ_Points += 2
elif answer in ["A", "B", "C"]:
    Some_Basketball_IQ_Points += 1

# question 2:
answer = input("How many days was Lonzo Ball injured? A:1006 B:986 C:1046")
if answer == "A":
    Basketball_IQ_Points += 2
elif answer in ["B","C"]:
    No_Basketball_IQ_Points += 2
elif answer in ["A","B"",C"]:
    Some_Basketball_IQ_Points += 1


# question 3:
answer = input("What was Jimmy Butler draft pick? A:30 B:15 C:25")
if answer == "A":
    Basketball_IQ_Points += 2
elif answer in ["B","C"]:
    No_Basketball_IQ_Points += 2
elif answer in ["A","B","C"]:
    Some_Basketball_IQ_Points += 1


# question 4:
answer = input("Who won the NBA MVP in 2015? A: LeKing James B: Kevin Durant C: Stephen Curry")
if answer == "C":
    Basketball_IQ_Points += 2
elif answer in ["B","A"]:
    No_Basketball_IQ_Points += 2
elif answer in ["A","B","C"]:
    Some_Basketball_IQ_Points += 1

# question 5:
answer = input("Who won the NBA championship in 2006? A: Spurs B: Celtics C: Heat")
if answer == "C":
    Basketball_IQ_Points += 2
elif answer in ["A","B"]:
    No_Basketball_IQ_Points += 2
elif answer in ["A","B","C"]:
    Some_Basketball_IQ_Points += 1

# End
print(f"Basketball_IQ_Points = {Basketball_IQ_Points}")
print(f"Some_Basketball_IQ_Points = {Some_Basketball_IQ_Points}")
print(f"No_Basketball_IQ_Points = {No_Basketball_IQ_Points}")
if Basketball_IQ_Points > No_Basketball_IQ_Points and Basketball_IQ_Points > Some_Basketball_IQ_Points:
    print("You have GOOD NBA IQ!!!")
elif No_Basketball_IQ_Points > Basketball_IQ_Points and No_Basketball_IQ_Points > Some_Basketball_IQ_Points:
    print("you have NO NBA IQ !")
elif Some_Basketball_IQ_Points > No_Basketball_IQ_Points and Some_Basketball_IQ_Points > Basketball_IQ_Points:
    print("You Have MID NBA IQ!")

