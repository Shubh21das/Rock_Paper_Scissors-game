import random

# This game is rock paper and scissors.
# computer chooses randomly and user chooses.
# 0 for rock, 1 for paper, 2 for scissors.
# rock beats scissors, scissors beats paper, paper beats rock.

t = int(input("Enter the number of rounds you want to play: "))
user_score = 0
computer_score = 0
for i in range(t):
    user = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
    computer = random.randint(0, 2)
    if user == 0 and computer == 2:
        print("User wins")
        user_score += 1
    elif user == 1 and computer == 0:
        print("User wins")
        user_score += 1
    elif user == 2 and computer == 1:
        print("User wins")
        user_score += 1
    elif user == computer:
        print("It's a tie")
        pass
    else:
        print("Computer wins")
        computer_score += 1
print("User score: ", user_score)
print("Computer score: ", computer_score)
if user_score > computer_score:
    print("User wins")
elif user_score < computer_score:
    print("Computer wins")
else:
    print("It's a tie")
