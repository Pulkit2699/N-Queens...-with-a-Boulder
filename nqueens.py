# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:37:37 2020

@author: pulkit
"""
import numpy as np
import random

def succ(state, boulderX, boulderY):
    succList = []
    for i in range(len(state)):
        for j in range(len(state)):
            succState = state.copy()
            succState[i] = (state[i] + j) % len(state)
            if((boulderY == i and boulderX == succState[i]) or succState[i] == state[i]):
                pass
            else:
                succList.append(succState)
    return succList

def getBoard(state, boulderX, boulderY):
    board = np.zeros((len(state), len(state)), dtype = int)
    for i in range(len(state)):
        board[state[i]][i] = 1
        board[boulderX][boulderY] = 10        
    return board
    

def f(state, boulderX, boulderY):
    conflictList = []
    board = getBoard(state, boulderX, boulderY)#boulder x and y can be changed
    for i in range(len(state)):
        
        #Check Left
        QueenRow = state[i]
        QueenCol = i - 1
        while(QueenCol >= 0):
            if(board[QueenRow][QueenCol] == 10):
                break
            elif(board[QueenRow][QueenCol] == 1):
                conflictList.append(QueenCol)
                break
            else:
                 QueenCol = QueenCol - 1
        #Check Right         
        QueenRow = state[i]
        QueenCol = i + 1
        while(QueenCol < len(state)):
            if(board[QueenRow][QueenCol] == 10):
                break
            elif(board[QueenRow][QueenCol] == 1):
                conflictList.append(QueenCol)
                break
            else:
                 QueenCol = QueenCol + 1
        
        #check upper left
        QueenRow = state[i] - 1
        QueenCol = i - 1
        while(QueenRow >= 0 and QueenCol >= 0):
            if(board[QueenRow][QueenCol] == 10):
                break
            elif(board[QueenRow][QueenCol] == 1):
                conflictList.append(QueenCol)
                break
            else:
                QueenCol = QueenCol - 1
                QueenRow = QueenRow - 1
                
        #check right down
        QueenRow = state[i] + 1
        QueenCol = i + 1
        while(QueenRow < len(state) and QueenCol < len(state)):
            if(board[QueenRow][QueenCol] == 10):
                break
            elif(board[QueenRow][QueenCol] == 1):
                conflictList.append(QueenCol)
                break
            else:
                QueenCol = QueenCol + 1
                QueenRow = QueenRow + 1
        
        #check upper right
        QueenRow = state[i] - 1
        QueenCol = i + 1
        while(QueenRow >= 0 and QueenCol < len(state)):
            if(board[QueenRow][QueenCol] == 10):
                break
            elif(board[QueenRow][QueenCol] == 1):
                conflictList.append(QueenCol)
                break
            else:
                QueenCol = QueenCol + 1
                QueenRow = QueenRow - 1
                
        #check left down
        QueenRow = state[i] + 1
        QueenCol = i - 1
        while(QueenRow < len(state) and QueenCol >= 0):
            if(board[QueenRow][QueenCol] == 10):
                break
            elif(board[QueenRow][QueenCol] == 1):
                conflictList.append(QueenCol)
                break
            else:
                QueenCol = QueenCol - 1
                QueenRow = QueenRow + 1
        
       
    conflictList = list(dict.fromkeys(conflictList))
    #print(board)
    #print(conflictList)
    return len(conflictList)

def choose_next(curr, boulderX, boulderY):
    succList = succ(curr, boulderX, boulderY)
    fsuccDict = []
    for i in range(len(succList)):
        Dict = dict({'state': succList[i], 'f':f(succList[i],boulderX, boulderY)})
        fsuccDict.append(Dict)
    fsuccDict.append(dict({'state': curr, 'f':f(curr,boulderX, boulderY)}))
    #Referred geeks for geeks for this sorting
    fsuccDict = sorted(fsuccDict, key = lambda i: (i['f'], i['state']))
    toReturn = fsuccDict[0]
    if(toReturn['state'] == curr):
        return None
    else:
        return toReturn['state']
    
  
def nqueens(initial_state, boulderX, boulderY):
    #Referred geeks for geeks for this + str to remove space
    print(initial_state, "- f=" + str(f(initial_state, boulderX, boulderY)))
    prevState = choose_next(initial_state, boulderX, boulderY)
    nextState = choose_next(initial_state, boulderX, boulderY)
    if(nextState == None):
        return initial_state
    while(nextState != None):
        print(nextState, "- f=" + str(f(nextState, boulderX, boulderY)))
        prevState = nextState
        nextState = choose_next(prevState, boulderX, boulderY)
        if(nextState == None):
            return prevState
            break
        
def generateRandom(n,boulderX, boulderY):
    a = np.random.randint(0,n,n)
    state = a.tolist()
    for i in range(n):
        if(boulderX == state[i] and boulderY == i):
            state = generateRandom(n,boulderX, boulderY)
    return state
            
            
def nqueens_restart(n, k, boulderX, boulderY):
    solList = []
    check = False
    for i in range(k):
        state = generateRandom(n,boulderX, boulderY)
        ret = nqueens(state, boulderX, boulderY)
        Dict = dict({'state': ret, 'f':f(ret,boulderX, boulderY)})
        solList.append(Dict)
        if(f(ret,boulderX, boulderY) == 0):
            print()
            print(ret)
            check = True
            break
        else:
            print()
    if not check:
        solList = sorted(solList, key = lambda i: (i['f'], i['state']))
        fval = solList[0]['f']
        for i in range(len(solList)):
            if (solList[i]['f'] == fval):
                print(solList[i]['state'])
            else:
                break
    
            
   

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    