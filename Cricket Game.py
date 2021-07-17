
info="""
Hi, I am Ritik Verma 
I am from Delhi, India
I proudly present My game.

Title:
Old School Cricket

The Game of Cricket by Hand !

This is one of my favourite School game  "

The Game:
There are two teams, with same number of players.
Each team has N_PLAYER (3 to 10 players per team) in a team.
Each player choose a move from the choices below based on runs scored by cricketer in a cricket match:
One, two , three , four , five or six. 
The AI choose randomly from one to six.
If they chose the same move, the player is out. Otherwise:
runs are collected on the scoreboard.

The game runs in two innings :-
Inning 1
where team A Batting and second is team B which is bowling.
Inning 2
where team B Batting and second is team A which is bowling.


In this program a human plays against an AI. 
The game is series N_GAMES times .
#Best of 3
    OR
#Best of 5

Note: This is my first Game in python. with code line of count= 300
.Thanks Stanford And Code in Place.

The winning conditions:-
The team make the most wins in the series.

******* GOOD LUCK ********
"""
import random

N_GAMES = 3
N_PLAYER = 5

inning1=[]
inning2=[]

def main():

    result=toss()
    # 1 for batting or  2 for bowling
    if result == 1:
        for i in range(N_PLAYER):
            player_number= i+1
            batting(player_number)
            print("score = ("+str(sum(inning1))+"/"+str(i+1)+")" )
        print("Total Runs Scored by team "+str(yourteam)+ " is " + str(sum(inning1)) +" .")
        print("Pyhton bots needed target of "+ str(sum(inning1)+1) +" runs.")
        for i in range(N_PLAYER):
            player_number = i+1
            bowling(player_number)
            print("score = (" + str(sum(inning2)) + "/" + str(i + 1) + ")")
            if sum(inning1) < sum(inning2):
                print(""+ str(yourteam) + " Lost the Game")
                h=0
                break

        if sum(inning1) > sum(inning2):
            print("Congratulations "+str(yourteam)+" wins the game .")
        h=1
        ###########
    else:
        for i in range(N_PLAYER):
            player_number = i+1
            bowling(player_number)
            print("score = (" + str(sum(inning2)) + "/" + str(i + 1) + ")")
        print("Total Runs Scored by Python Bots is " + str(sum(inning2)) + " .")
        print(""+str(yourteam)+" needs "+ str(sum(inning2)+1) +" runs to win.")
        for i in range(N_PLAYER):
            player_number = i+1
            batting(player_number)
            print("score = (" + str(sum(inning1)) + "/" + str(i + 1) + ")")
            if sum(inning1) > sum(inning2):
                print("Congratulations "+str(yourteam)+" wins the game .")
                h=1
                break
        if sum(inning2) < sum(inning1):
            print(" "+str(yourteam)+" Lost the Game.")
        h=0
        ###############
    if h == 1:
        return 1
    else:
        return 0


"""
innings 1 append score X 5times
innings 2 append score X 5times
"""
def batting(player_number):
    print("Player "+str(player_number)+" is batting.")
    run=scorehuman(player_number)
    inning1.append(run)

def bowling(player_number):
    print("Player " +str(player_number) + " is batting.")
    run=scoreai(player_number)
    inning2.append(run)

def welcome():
    print('')
    print('...The Next cricket match Begins...')
    print('****## GOOD LUCK ##****')
def print_welcome2():
    print('Welcome to The Game of Cricket')
    print('You will play ' + str(N_GAMES) + ' games against the AI')
    print('There are ' + str(N_PLAYER) + ' players In a Team ')
    yourteam = input('Name Your team: ')
    print('')
    print('...The cricket match Begins...')
    print('Team ' + str(yourteam) + ' VS Team Python Bots')
    print("")

    return (yourteam)


def toss():
    """
    Choose head or tails
    """
    print('The coin toss')
    print('Choose heads or tails')
    human_toss = get_human_toss()
    ai_choose = coin_output()
    print("You choose " + str(human_toss) + " .")
    result = get_toss_result(human_toss, ai_choose)
    return result
def get_human_toss():
    while True:
        human_toss = input('what do you Choose:')
        if is_valid_choose(human_toss):
            return human_toss
        print("invalid choose,Choose heads or tails")
def is_valid_choose(human_toss):
    if human_toss == "heads":
        return True
    if human_toss == "tails":
        return True
    return False
def coin_output():
    ai = random.randint(1, 2)
    if ai == 1:
        return "tails"
    else:
        return "heads"
def get_toss_result(human_toss, ai_choose):
    if human_toss == ai_choose:
        print("Congratulations You Won the toss.")
        while True:
            bat_or_bowl = input("For Batting enter : 1 \n For Bowling enter : 2 \n")

            if bat_or_bowl == "1":
                print("You choose Batting.\n")
                return 1
            elif bat_or_bowl == "2":
                print("You choose Bowling.\n")
                return 2
            else:
                print("invalid choose.")
    else:
        print("you loose the toss.\n")
        print("Team python choose to Bat first\n")

def get_ai_move():
    """
    for now the AI plays randomly. But the optimal strategy is:
    If you lose, switch to the thing that beats the thing your opponent just played.
    If you win, switch to the thing that would beat the thing that you just played.
    """
    value = random.randint(1, 6)
    if value == 1:
        return 1
    if value == 2:
        return 2
    if value == 3:
        return 3
    if value == 4:
        return 4
    if value == 5:
        return 5
    if value == 6:
        return 6
def get_human_move():
    """
    make sure the human play (1 to 6)
    """
    while True:
        choice = input('What you hit : ')
        if is_valid_choice(choice):
            return int(choice)
        print('Invalid Run')
def get_human_movebowling():
    """
    make sure the human play (1 to 6)
    """
    while True:
        choice = input('What you bowl : ')
        if is_valid_choice(choice):
            return int(choice)
        print('Invalid ball')
def is_valid_choice(choice):
    """
    >>> is_valid_choice('1,2,3,4,5,6')
    True

    >>> is_valid_choice('xyz,22,11,7,0.6')
    False
    """
    if choice == "1":
        return True
    if choice == "2":
        return True
    if choice == "3":
        return True
    if choice == "4":
        return True
    if choice == "5":
        return True
    if choice == "6":
        return True
    return False
def scorehuman(player_number):
    score = 0
    pn=player_number
    while True:
        ai_move = get_ai_move()
        human_move = get_human_move()
        print("The Ai bowled "+str(ai_move)+".")
        if ai_move == human_move:
            if score == 0:
                print("Duck Out \U0001F425")
            if human_move > 4:
                print('Catch out \U0001F606')
            elif human_move < 2:
                print("Run out \U0001F624")
            else:
                print("Wicket out \U0001F92F")
            print("Total runs scored by player number "+str(pn)+ " are :"+str(score)+".")
            return score
        else:
            score += human_move

def scoreai(player_number):
    score = 0
    pn=player_number
    while True:
        ai_move = get_ai_move()
        human_move = get_human_movebowling()
        print(" The Ai Hit "+str(ai_move)+".")
        if ai_move == human_move:
            if score == 0:
                print("Duck Out \U0001F425")
            if ai_move > 4:
                print('Catch out \U0001F603')
            elif ai_move < 3:
                print("Run out \U0001F61C")
            else:
                print("Wicket out \U0001F923")
            print("Total runs scored by player number "+str(pn)+ " are :"+str(score)+".")
            return score
        else:
            score += ai_move


settings=input("Welcome to the Game of Cricket.\n"
                   "To SKIP press any key and enter.\n"
                   "For instructions press 0. \nFor settings press 9. \n")
if settings == "9":
    N_GAMES=int(input("What are the number of matches in the series?"))
    N_PLAYER=int(input("How many players are there in one team?"))
    print("*******Good Luck*******")

if settings == "0":
    print(info)

yourteam = print_welcome2()
wins = 0
for i in range (N_GAMES):

    win_count=main()

    wins += win_count
    print("\n"
          "Summary:\n"
          "Team " +str(yourteam)+ " wins " +str(wins)+" matches out of "+str(i + 1)+" matches.\n"
                                                                                    "")
    if i > N_GAMES-1:
        welcome()

if wins > 0.5*N_GAMES:
    print("Congratulations,"+str(yourteam)+ " won The "+str(N_GAMES)+ " matches series")
elif wins == 0.5*N_GAMES:
    print("The series is draw.")
else:
    print("Team "+str(yourteam)+" lost the Series.")

