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
        
  #  print("number of turns: "+ str(turn))
   # print( "     " + Name1  + " result is = " + str(result1) + " achieving a score of: " + str(score1))
   # print( "     " + Name2  + " result is = " + str(result2) + " achieving a score of: " + str(score2))

    return [score1, score2]

def Coop10(own, oth):
    if(len(own)<11):
        return COOP;
    for i in oth[-10:]: 
        if(i==COOP):
            return COOP
    return DEFECT

def Defect10(own, oth):
    if(len(own)<11):
        return DEFECT;
    for i in oth[-10:]:
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
        
def Strats(own, oth):
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

def Strats2(own, oth):
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

def Strats3(own, oth):
    if(len(own)==0):
        return COOP
    elif(oth[-1]==COOP):
        return own[-1]
    else:
        if(random.uniform(0, 1)<0, 1):
            return COOP
        return DEFECT


def Game(Player1, Player2, Score1, Score2, Name1, Name2):
    [S1, S2]=tournment(Player1, Player2, Name1, Name2)
    if(Name1==Name2):
        Score1+=(Score1+S1+S2)
        return [Score1, Score1]
    Score1+=S1
    Score2+=S2
    return [Score1, Score2]


def t2ft(own, oth):
    if(len(own)<2):
        return COOP
    elif(oth[-1]==DEFECT and oth[-2]==DEFECT):
        return DEFECT
    else:
        return COOP




if __name__ == "__main__":

    Score, Name, Strat = [], [], []

    Name.append("Coop10")
    Name.append("Defect10")
    Name.append("Random")
    Name.append("Tit-For-Tat")
    Name.append("Strats")
    Name.append("Strats2")
    Name.append("nice guy")
    Name.append("mad guy")
    #Name.append('GTFT')
   # Name.append('CTFT')
    #Name.append('pavlov')
    #Name.append('Two-Tit-For-Tat')
    Name.append('Strats3')
    
    Strat.append(Coop10)
    Strat.append(Defect10)
    Strat.append(Random)
    Strat.append(TFT)
    Strat.append(Strats)
    Strat.append(Strats2)
    Strat.append(niceguy)
    Strat.append(madguy)
    #Strat.append(GTFT)
    #Strat.append(CTFT)
    #Strat.append(pavlov)
    #Strat.append(t2ft)
    Strat.append(Strats3)
    
    
    n_strats = len(Name)
    for i in range(0,n_strats):
        Score.append(float(0))

    cont = 0
    current=[]
    final=[]
    for i in range(4):
        current.append([Name[i],Strat[i],Score[i]]);
    for k in range(4,n_strats):          
        current.append([Name[k],Strat[k],Score[i]])
        for i in range(5):
            for j in range(i):
                [current[i][2], current[j][2]] = Game(current[i][1], current[j][1], current[i][2], current[j][2], current[i][0], current[j][0])
                cont+=1

        board = []
        final.append(current[4])
        for i in range(5):
            board.append([current[i][2], current[i][0]])
        
        board.sort()
        
        for i in range(5):
            print (str(i+1) +  " lugar : " +  board[4-i][1] + ":" +  str(board[4-i][0]) + " average is :" + str(board[4-i][0] / 4))
        print ("  ")
        current.pop()
        current[0][2]=0
        current[1][2]=0
        current[2][2]=0
        current[3][2]=0
    print ("Final Scores Are:")
    final = sorted(final,key=lambda x:float(x[2]))
    size=len(final)-1
    for i in range(0, size+1):
        print (final[size- i][0] + " " + str(final[size - i][2]) + "average is : " + str(final[size - i][2]/5))
        
