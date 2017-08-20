import random

def Strats3(own, oth):
    if(len(own)==0):
        return "C"
    elif(oth[-1]=="C"):
        return own[-1]
    else:
        if(random.uniform(0, 1)<0.1):
            return "C"
        return "D"
