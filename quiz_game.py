print("Welcome to my fish quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play!")
score = 0

answer = input("Many fish give birth by laying eggs. (True/False) ").lower()
if answer == "true":
    print('Correct! Most fish lay thousands of eggs.')
    score += 1
else: 
    print("Incorrect!")

answer = input("A group of fish is called a shoal. (True/False) ").lower()
if answer == "true":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("Coral reefs are made from fish scales. (True/False) ").lower()
if answer == "false":
    print('Correct! Coral is made from the skeletons of tiny sea animals.')
    score += 1
else: 
    print("Incorrect!")

answer = input("Fish were the first animals with backbones to evolve. (True/False) ").lower()
if answer == "true":
    print('Correct! The first fish evolved over 500 million years ago.')
    score += 1
else: 
    print("Incorrect!")

print("You got " + str(score) + " correct! Great job!")
print("You got " + str((score /4) * 100) + "%!")