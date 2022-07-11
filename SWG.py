import random

list=["s","w","g"]



chance=10
no_of_chance=0
your_score=0
computer_score=0
print("Welcome to snake water gun game::")
print("Choose one of them::")
print(f"s,w==s  s,g==g  w,s==s  w,g==w  g,w==s  g,w==g")

while no_of_chance<chance:
    print("Snake,Water,Gun::")
    choice = random.choice(list)
    # print(choice)
    num=input()
    # print(num)

    if num=="s" and choice=="s":
        print("No one win")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    elif num=="s" and choice=="w":
        your_score=your_score+1
        print("You win")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    elif num=="s" and choice=="g":
        computer_score=computer_score+1
        print("You loss")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    elif num=="w" and choice=="w":
        print("No one win")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    elif num=="w" and choice=="s":
        computer_score=computer_score+1
        print("you loss")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    elif num=="w" and choice=="g":
        your_score=your_score+1
        print("You win")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    elif num=="g" and choice=="g":
        print("No one win")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    elif num=="g" and choice=="s":
        your_score=your_score+1
        print("You win")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    elif num=="g" and choice=="w":
        computer_score=computer_score+1
        print("You loss")
        print(f"your score:: {your_score} and computer score:: {computer_score}")
    else:
        print("You enter wrong key::")
        print("Try again::")
    no_of_chance = no_of_chance + 1
    print(f"No of chance left::{chance-no_of_chance} from {chance}")

print("Game over::")


if your_score>computer_score:
    print("You won the game")
elif your_score<computer_score:
    print("Computer won the game")
else:
    print("Draw")
