#!/usr/bin/env python

import random

COOP = False
DEFECT = True

def tournment(player1, player2, Name1, Name2):
    turn =0
    result1 =0 #score of player 1
    result2 =0 #score of player 1
    data1=[] #array from player1 moves
    data2=[] #array from player2 moves
    not_finish=True; #boolean for game extension
    
    while(not_finish):
        data1.append(player1(data1, data2))
        data2.append(player2(data2, data1))

        # values from payoff matrix 
        if((data1[-1]==COOP) and (data2[-1]==COOP)):
            result1 = result1 + 5
            result2 = result2 + 5
        elif((data1[-1]==COOP) and (data2[-1]==DEFECT)):
            result2= result2 + 9
        elif((data1[-1]==DEFECT) and (data2[-1]==COOP)):
            result1= result1 + 9
        else:
            result1= result1 + 1
            result2= result2 + 1
            
        #preparing next move
        turn+=1
        if(turn >50): #when the turn is >50, we will introduce the odds of finishing
            if(random.uniform(0, 1) <0.00346):
                not_finish=False
    
    score1=float(result1)/turn
    score2=float(result2)/turn
        
    #print("number of turns: "+ str(turn))
    #print( "     " + Name1  + " result is = " + str(result1) + " achieving a score of: " + str(score1))
    #print( "     " + Name2  + " result is = " + str(result2) + " achieving a score of: " + str(score2))

    return [score1, score2]


def Coop10(own, oth):
    if(len(own)<10):
        return COOP;
    for i in oth[-10:]: 
        if(i==COOP):
            return COOP
    return DEFECT


def Defect10(own, oth):
    if(len(own)<10):
        return DEFECT;
    for i in oth[-9:]:
        if(i==DEFECT):
            return DEFECT
    return COOP


def Random(own, oth): 
    if(random.uniform(0, 1)<0.5):
        return COOP
    else:
        return DEFECT


def TFT(own, oth):
    if len(own) == 0 or oth[-1] == COOP:
        return COOP
    else:
        return DEFECT

def Strats(own, oth): #RandomPunish
    j = 0
    if len(own) == 0:
        return COOP
    
    for i in oth:
        if i == DEFECT:
            j+=1
        
    if i == len(own):
        return DEFECT
    
    for i in own:
        if i == DEFECT:
            j-=1

    if j > 1:
        return DEFECT

    return COOP

def Strats2(own, oth): #fudido
    size= len(own)
    if size == 0:
        return COOP
    flag = 0
    
    for i in own:
        if own[-1] == DEFECT:
            flag = 0
    
    if(size > 50) and flag == 0:
        if(random.uniform(0, 1) <0.00001*size):
            return DEFECT

    if oth[-1]==COOP and own[-1]==COOP:
        return COOP
    if oth[-1]==COOP and own[-1]==DEFECT:
        return COOP
    elif(size<3):
        return COOP
    elif oth[-2]==COOP and own[-2]==DEFECT and oth[-1]==COOP:
        return DEFECT
    else:
        return DEFECT

def niceguy(own,oth):
    return COOP
def madguy(own,oth):
    return DEFECT
        
def GTFT(own,oth):
    if(len(own)==0 or oth[-1]==COOP):
        return COOP
    else:
        if(random.uniform(0,1)<0,4):
            return DEFECT
        return COOP

def CTFT(own,oth):
    if(len(own)<3 or oth[-2]==COOP):
        return COOP
    else:
        return DEFECT

def pavlov(own,oth):
    if(len(own)==0):
        return COOP
    elif(oth[-1]==COOP): #sucessfull
        return own[-1]
    else:
        return DEFECT

def Game(Player1, Player2, Score1, Score2, Name1, Name2):
    [S1, S2]=tournment(Player1, Player2, Name1, Name2)
    if(Name1==Name2):
        Score2+=(S1+S2)
        return [Score2, Score2]
    Score1+=S1
    Score2+=S2
    return [Score1, Score2]
    
def Strats3(own, oth):
    if(len(own)==0):
        return COOP
    elif(oth[-1]==COOP):
        return own[-1]
    else:
        if(random.uniform(0, 1)<0, 1):
            return COOP
        return DEFECT


if __name__ == "__main__":

    Score, Name, Strat = [], [], []
    
    for i in range(5): #number players = k*strats (k=2)
        Name.append("Coop10")
        Name.append("Defect10")
        Name.append("Random")
        Name.append("Tit-For-Tat")
        Name.append("Strats")
        Name.append("Starts2")
        Name.append("nice guy")
        Name.append("mad guy")
        Name.append('GTFT')
        Name.append('CTFT')
        Name.append('pavlov')
        Name.append('Strats3')
        
        Strat.append(Coop10)
        Strat.append(Defect10)
        Strat.append(Random)
        Strat.append(TFT)
        Strat.append(Strats)
        Strat.append(Strats2)
        Strat.append(niceguy)
        Strat.append(madguy)
        Strat.append(GTFT)
        Strat.append(CTFT)
        Strat.append(pavlov)
        Strat.append(Strats3)

    
    n_players = len(Name)
    for i in range(0, n_players):
        Score.append(float(0))

    cont = 0

    for iteration in range(100):
        if(iteration!=0): # update starts used
            aux=[]
            for i in range(0,n_players): # for each player
                a = random.uniform(0,scoresum)
                temp=0
                for j in range(0,n_players): #find new strat
                    temp+=board[j][0] #score from previus iteration
                    if(temp >= a):
                        aux.append([Strat[j],Name[j]]) 
                        break

            for i in range(0,n_players):  # update players        
                Score[i]=0
                Strat[i]=aux[i][0]
                Name[i]=aux[i][1]

        for i in range(0,n_players): # make the games for each iteraction
            for j in range(i):
                [Score[i], Score[j]] = Game(Strat[i], Strat[j], Score[i], Score[j], Name[i], Name[j])
                cont+=1

        board = []
        scoresum=0
        for i in range(0, n_players):
            board.append([Score[i], Name[i]])
            scoresum+=Score[i]

        print ("Iteration: "  +  str(iteration))     
        for i in range(0, n_players):
            print ("       " +  str(board[i][1]) + ":" +  str(board[i][0]))
