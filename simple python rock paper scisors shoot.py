import random
import time
player_win=0
player2win=0
playerstie=0
playeraitie=0
aiwin=0
x=2.5

a=int(input("how many rounds do you want to play:"))
aimove = random.randint(1, 3)

p2ai=int(input("""1:play with player2 
2:play with ai
:"""))
#to test who is the winner 
if p2ai == 2:
    for i in range(a):
    
        print("1:Rock")
        print("2:scisors")
        print("3:paper")
        player_move=int(input("chose your move:"))

        if aimove == 1:
            print("your opponent chose rock")
        elif aimove == 2:
            print("your opponent chose scissors")
        else:
            print("your opponent chose paper")

        if aimove == 1 and player_move ==3:
            print("you win")
            player_win=player_win+1
    
        elif aimove == 3 and player_move == 1:
            print("you lose")
            aiwin = aiwin+1
    
        elif player_move < aimove:
            print("you win")
            player_win = player_win + 1
    
        elif aimove == player_move:
            print("it is a tie")
            playeraitie= playeraitie + 1
        elif player_move > aimove:
            print("you lose")
            aiwin=aiwin+1
    
        aimove=random.randint(1, 3)
        time.sleep(x)
# to print the resaults outside the for loop
if p2ai == 2:
    print("ai won ", str(aiwin), " time/times player won ", str(player_win), "times there were ", str(playeraitie), "ties" ) 
#to test the resaults 
if p2ai == 1:
    for i in range(a):
    
        print("1:Rock")
        print("2:scisors")
        print("3:paper")
        player_move=int(input("player 1chose your move:"))
        player2_move=int(input("player 2 chose your move:"))
        if player2_move == 1:
            print(" player2 chose rock")
        elif player2_move == 2:
            print("player2 chose scissors")
        else:
            print("player2 chose paper")

    if player2_move == 1 and player_move ==3:
        print("player 1 wins")
        player_win=player_win+1

    
    elif player2_move == 3 and player_move == 1:
        print("player 2 wins")
        player2win=player2win+1
    
    elif player_move < player2_move:
        print("player 1 win")
        player_win=player_win+1
    elif player2_move == player_move:
        print("it is a tie")
        playerstie=playerstie+1
    elif player_move > player2_move:
        print("player 2 wins")
    time.sleep(x)
#to print the resaults outside the for loop
if p2ai == 1:
    print("player 1 won ", str(player_win), " time/times player2 won ", str(player2win), "times there were ", str(playerstie), "ties" )

#to wait and let the user see the results
time.sleep(x)




