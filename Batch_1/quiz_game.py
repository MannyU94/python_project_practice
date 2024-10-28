print("Welcome to my football quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play! :)")
score = 0

answer = input("Who won the Ballon d'Or in 2017? ")
if answer.lower() == "cristiano ronaldo":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What team shares the Merseyside Derby with Liverpool? ")
if answer.lower() == "everton":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What team competes with Borussia Dortmund in the \"Der Klassiker\" derby? ")
if answer.lower() == "bayern munich":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Who is the youngest goalscorer in the history of the FIFA World Cup? ")
if answer.lower() == "pele":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")