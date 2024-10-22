cat_points = 0
dog_points = 0

# question 1:
answer = input("On a weekend would you rather A) Sleep all day cause your lazy, or B) go to the  mall?")
if answer == "A":
	cat_points +=999
elif answer == "B":
	dog_points +=0.1

# question 2:
answer = input("do you like A) fresh meat, or B) I prefer to sleep than eat?")
if answer == "A":
	dog_points +=0.1
elif answer == "B":
	cat_points +=999

# question 3:
answer = input("Would you rather eat lunch A) I would actually sleep because I don't eat lunch, or B) Eat lunch in the middle of the super bowl field")
if answer == "A":
	cat_points +=999
elif answer == "B":
	dog_points +=0.1

# end of quiz:
if cat_points > dog_points:
	print("You are a sleepy cat person!")
elif dog_points > cat_points:
	print("You are a dog person!")