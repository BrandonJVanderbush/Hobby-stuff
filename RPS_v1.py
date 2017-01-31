import random
def Rock_paper_scissors():
    print("Would you like to play a game of Rock paper scissors?")
    input1 = input()
    yea = ["yes", "Yes", "y", "y"]
    com_options = [3, 2 , 4]
    com_options_explicit = ["a", "scissors", "rock", "paper"]
	# rock = 3 scissors = 2 paper = 4
    yea1 = input1 in yea
    if yea1 == 1:
        print("What would you like the game to be best of?")
        input2 = int(input())
        i = 0
        while i*2 < input2:
            i+=1
        if input2 % 2 ==0:
            i+=1
        print("Okay, the game will be best of " + str(input2) + " " + str(i) + " rounds will be needed to win the game")
        print("The round will start on your shoot")
        user_points = 0
        comp_points = 0
        while user_points < i and comp_points < i:
                user_shot = input()
                num = random.randint(0,len(com_options) - 1)
                if user_shot == "rock":
                    usv = 3
                elif user_shot == "paper":
                    usv = 4
                else:
                     usv = 2
                round_win = usv - int(com_options[num])
                if round_win <= -1:
                    comp_points+=1
                    print("Sorry computer shot " + com_options_explicit[com_options[num]-1] + " which wins against " + user_shot +" :(" )
                    print("Current score is: You: " + str(user_points) + " Opponent: " + str(comp_points) + " Shoot again when ready" )
                elif round_win == 0:
                    print("You tied with your opponent, you both shot " + com_options_explicit[com_options[num]-1] )
                    print("Current score is: You: " + str(user_points) + " Opponent: " + str(comp_points) + " Shoot again when ready" )
                elif round_win >= 1:
                    user_points+=1
                    print("You won the round, you shot " + user_shot + " which beats " + com_options_explicit[com_options[num]-1])
                    print("Current score is: You: " + str(user_points) + " Opponent: " + str(comp_points) + " Shoot again when ready" )
        if user_points == i:
            print("You won!!!")
        else:
            print("Sorry, you lost")
					 

Rock_paper_scissors()