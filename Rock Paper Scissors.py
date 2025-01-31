import random

# Rock
rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice_List = ("Rock", "Paper", "Scissors")
#put human choice here
human_Choice = input("Choose Rock Paper or Scissors :")
if human_Choice == "Rock":
    print("player chooses " + human_Choice)
    print(rock)
elif human_Choice == "Paper":
    print("Player Chooses " + human_Choice)
    print(paper)
else:
    print("Player Chooses " + human_Choice)
    print(scissors)

cpu_Choice = (random.choice(choice_List))
if cpu_Choice == "Rock":
    print("Computer chooses Rock")
    print(rock)
elif cpu_Choice == "Paper":
    print("Computer Chooses Paper")
    print(paper)
elif cpu_Choice == "Scissors":
    print("Computer Chooses Scissors")
    print(scissors)


if human_Choice == "Rock" and cpu_Choice == "Scissors":
    print("Human Wins")
elif cpu_Choice == "Rock" and human_Choice == "Scissors":
    print("Computer Wins")
elif human_Choice == "Paper" and cpu_Choice == "Rock":
    print("Human Wins")
elif cpu_Choice == "Paper" and human_Choice == "Rock":
    print("Computer Wins")
elif human_Choice == "Scissors" and cpu_Choice == "Paper":
    print("Human Wins")
elif cpu_Choice == "Scissors" and human_Choice == "Paper":
    print("Computer Wins")
else:
    print("YOU TIE")