
import random

print("Welcome to rock, paper, scissors. You will play against the computer for three games. Whoever has the most points wins!")
menu = "Press 1 for Rock, 2 for paper, and 3 for scissors"
player_points = 0
computer_points = 0

def selection_process(selection):
    while selection > 3 or selection < 1:
        print("Invalid Choice!")
        print(menu)
        selection = int(input())
    computer = random.randint(1,3)
    if computer == selection:
        tie()
    if (selection == 1 and computer == 2) or (selection == 3 and computer == 1) or (selection == 2 and computer == 3): 
        lose()
    if (selection == 2 and computer == 1) or (selection == 1 and computer == 3) or (selection == 3 and computer == 2):
        win()


def tie():
    print("Computer and you selected the same thing!")
    print("Please select again")
    print(menu)
    selection_process(input())

def win():
    global player_points, computer_points
    print("You beat the computer!")
    player_points = player_points + 1
    print(player_points)
    if player_points == 3:
        print("Thanks for playing you win!")
        exit()
    else: 
        print(menu)
        selection_process(int(input()))

def lose():
    global player_points, computer_points
    print("The computer beat you!")
    computer_points = computer_points + 1
    print("Computer Points: %", computer_points)
    print("User points: % ", player_points)
    if computer_points == 3:
        print("You lose! To play again press 1. To quit press 2")
        play_again = input()
        play_again = int(play_again)
        if play_again == 1:
            player_points == 0
            computer_points == 0
            print("")
            print(menu)
            selection_process(input())
        if play_again == 2:
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid selection, automatically ending game!")
            exit()
    else:
        print(menu)
        selection_process(int(input()))


print("Rock Paper Scissors!")
print(menu)
selection_process(int(input()))