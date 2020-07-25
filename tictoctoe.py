import turtle
import tkinter
import random
from tkinter import messagebox
from turtle import*

s = 0
a = 1
m = 3
locx = 0
locy = 0
winner = "none"
windowOpen = True
isopen = True
turn = "x"
squareToClick = 9
isdone = False

board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]

locationX = {
    1 : 0,
    2 : 50,
    3 : 100,
    4 : 0, 
    5 : 50,
    6 : 100,
    7 : 0,
    8 : 50, 
    9 : 100 
    }
locationY = {
    1 : 100,
    2 : 100,
    3 : 100,
    4 : 50,
    5 : 50,
    6 : 50,
    7 : 0,
    8 : 0,
    9 : 0,
    }

def play_tic_tac_toe():
    while True:
        reset()
        drawTable(m)
        while winner == "none" or squareToClick != 0:
            if turn == "x":
                turn = "o"
            else:
                turn = "x"
            clicked()
            if winner == False:
                checkWinner()

def reset():
    global winner, windowOpen, isopen
    global turn, squareToClick
    clear()
    speed(10)
    left(90)
    color ("blue")
    winner = "none"
    goto(0, 0)
    squareToClick = 9
    turn = "x"
    hideturtle()
    board = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]

def drawTable(n):
    for i in range(1, n+1):
        for y in range(1, n+1):
            for x in range(1, 5):
                forward(50)
                right(90)
            forward(50)
        backward(n*50)
        right(90)
        forward(50)
        left(90)   

def getPos(x, y):
    global turn, squareToClick
    print(x, y)
    x = int(x)
    y = int(y)
    global locx, locy
    locx = "none"
    locy = "none"
    person = ""
    '''
    for i in range(x-50, x+1):
        if i in locationX:
            locx = locationX[i]
            break
    for j in range(y-50, y+1):
        if j in locationY:
            locy = locationY[j]
            break
    '''
    '''
    xMod = x%50
    yMod = y%50
    locx = locationX[(x-xMod)]
    locy = locationY[(y-yMod)]
    if locx == locy:
        person = locx
    print(locx, locy, xMod, yMod, x-xMod, y-yMod)
    locx = x
    locy = y
    '''
    if board[2-(int(y/50))][int(x/50)] == "-":
        board[2-(int(y/50))][int(x/50)] = turn
        # locate = calculate(x, y)
        # print_X_O(turn, locate)
        squareToClick = squareToClick - 1
        if turn == "x":
            turn = "o"
        else:
            turn = "x"
    elif board[2-(int(y/50))][int(x/50)] == "x" and turn == "x":
        run = tkinter.messagebox.showinfo("Wrong clicked", "Bạn đã ấn ô vuông đó")
    elif board[2-(int(y/50))][int(x/50)] == "o" and turn == "o":
        run = tkinter.messagebox.showinfo("Wrong Clicked", "Bạn đã ấn ô vuông đó")
    elif board[2-(int(y/50))][int(x/50)] == "x" and turn == "o":
        run = tkinter.messagebox.showinfo("Wrong Clicked", "Người chơi khác đã ấn ô vuông đó")
    elif board[2-(int(y/50))][int(x/50)] == "o" and turn == "x":
        run = tkinter.messagebox.showinfo("Wrong Clicked", "Người chơi khác đã ấn ô vuông đó")
    locate = calculate(x, y)
    print_X_O(turn, locate)
    printBoard(board)
    print  (winner)
    checkWinner()
    print(squareToClick)
    # changeBoard(board)

def changeBoard(board):
    penup()
    # goto(locx, locy)
    pendown()
    '''
    global sprite
    if turn == "x":
        write("x")
        if sprite == "s1" and board[0[0]] == "0":
            board[0[0]] = "x"
            squareToClick = squareToClick - 1
        elif sprite == "s2" and board[0[1]] == "0":
            board[0[1]] = "x"
            squareToClick = squareToClick - 1
        elif sprite == "s3" and board[0[2]] == "0":
            board[0[2]] = "x"
            squareToClick = squareToClick - 1
        elif sprite == "s4" and board[1[0]] == "0":
            board[1[0]] = "x"
            squareToClick = squareToClick - 1
        elif sprite == "s5" and board[1[1]] == "0":
            board[1[1]] = "x"
            squareToClick = squareToClick - 1
        elif sprite == "s6" and board[1[2]] == "0":
            board[1[2]] = "x"
            squareToClick = squareToClick - 1
        elif sprite == "s7" and board[2[0]] == "0":
            board[2[0]] = "x"
            squareToClick = squareToClick - 1
        elif sprite == "s8" and board[2[1]] == "0":
            board[2[1]] = "x"
            squareToClick = squareToClick - 1
        elif sprite == "s9" and board[2[2]] == "0":
            board[2[2]] = "x"
            squareToClick = squareToClick - 1
    else:
        write("o")
        if sprite == "s1" and board[0[0]] == "0":
            board[0[0]] = "o"
            squareToClick = squareToClick - 1
        elif sprite == "s2" and board[0[1]] == "0":
            board[0[1]] = "o"
            squareToClick = squareToClick - 1
        elif sprite == "s3" and board[0[2]] == "0":
            board[0[2]] = "o"
            squareToClick = squareToClick - 1
        elif sprite == "s4" and board[1[0]] == "0":
            board[1[0]] = "o"
            squareToClick = squareToClick - 1
        elif sprite == "s5" and board[1[1]] == "0":
            board[1[1]] = "o"
            squareToClick = squareToClick - 1
        elif sprite == "s6" and board[1[2]] == "0":
            board[1[2]] = "o"
            squareToClick = squareToClick - 1
        elif sprite == "s7" and board[2[0]] == "0":
            board[2[0]] = "o"
            squareToClick = squareToClick - 1
        elif sprite == "s8" and board[2[1]] == "0":
            board[2[1]] = "o"
            squareToClick = squareToClick - 1
        elif sprite == "s9" and board[2[2]] == "0":
            board[2[2]] = "o"
            squareToClick = squareToClick - 1

    '''

'''
def clicked():
    draw = turtle.Screen()
    sprite = draw.onclick(getPos)
    draw.mainloop()
'''

def checkWinner():
    global isdone
    ifGameOver(1, 2, 3, "x")
    ifGameOver(4, 5, 6, "x")
    ifGameOver(7, 8, 9, "x")
    ifGameOver(1, 4, 7, "x")
    ifGameOver(2, 5, 8, "x")
    ifGameOver(3, 6, 9, "x")
    ifGameOver(1, 5, 9, "x")
    ifGameOver(3, 5, 7, "x")
    ifGameOver(1, 2, 3, "o")
    ifGameOver(4, 5, 6, "o")
    ifGameOver(7, 8, 9, "o")
    ifGameOver(1, 4, 7, "o")
    ifGameOver(2, 5, 8, "o")
    ifGameOver(3, 6, 9, "o")
    ifGameOver(1, 5, 9, "o")
    ifGameOver(3, 5, 7, "o")
    if squareToClick == 0:
        winner = "draw"

def ifGameOver(s1, s2, s3, tick):
    isdone = False
    sq1 = s1 - 1
    sq2 = s2 - 1
    sq3 = s3 - 1
    if sq1 <= 2:
        if board[0][sq1] == tick:
            isdone = True
        else:
            isdone = False
    elif sq1 <= 5 and sq1 >=  3:
        if board[1][sq1 - 3] == tick:
            isdone = True
        else:
            isdone = False
    elif sq1 <= 8 and sq1 >= 6:
        if board[2][sq1 - 6] == tick:
            isdone = True
        else:
            isdone = False
    if sq2 <= 2:
        if board[0][sq2] == tick:
            isdone = True
        else:
            isdone = False
    elif sq2 <= 5 and sq2 >= 3:
        if board[1][sq2-3] == tick:
            isdone = True
        else:
            isdone = False
    elif sq2 <= 8 and sq2 >=  6:
        if board[2][sq2-6] == tick:
            isdone = True
        else:
            isdone = False
    if sq3 <= 2:
        if board[0][sq3] == tick:
            isdone = True
        else:
            isdone = False
    elif sq3 <= 5  and sq3 >=  3:
        if board[1][sq3-3] == tick:
            isdone = True
        else:
            isdone = False
    elif sq3 <= 8 and sq3 >= 6:  
        if board[2][sq3-6] == tick:
            isdone = True
        else:
            isdone = False
    if isdone == True:
        winner = tick

def printBoard(board):
    for item in board:
        print(item)
s
def print_X_O(thing, square):
    placeX = locationX[square]
    placeY = locationY[square]
    placeX = placeX + 25
    placeY = placeY + 25 
    penup()
    goto(placeX, placeY)
    pendown()
    if thing == "x":
        write("x", move = False, align = "center", font = ("Arial", 16, "normal"))
    elif thing == "o":
        write("o", move = False, align = "center", font = ("Arial", 16, "normal"))

def calculate(x, y):
    yloc = 2-(int(y/50))
    xloc = int(x/50)
    location = 0
    xlist = []
    ylist = []
    if yloc <= 3:
        for i in range(1, 4):
            ylist.append(i)
    if yloc <= 6:
        for j in range(4, 7):
            ylist.append(j)
    if yloc <= 9:
        for k in range(7, 10):
            ylist.append(k)   
    if xloc <= 3:
        for l in range(1, 4):
            xlist.append(l)
    if xloc <= 6:
        for o in range(4, 7):
            xlist.append(o)
    if xloc <= 9:
        for p in range(7, 10):
            xlist.append(p)
    for q in xlist:
        for r in ylist:
            if q == r:
                location =  q
    return location

def gameEnd(s1, s2, s3):
    speed(5)
    if s1 == 1 and s2 == 2 and s3 == 3:
        penup()
        goto(0, 125)
        pendown()
        goto(100, 125)
    elif s1 == 4 and s2 == 5 and s3 == 6:
        penup()
        goto(0, 75)
        pendown()
        goto(100, 75)
    elif s1 == 7 and s2 == 8 and s3 == 9:
        penup()
        goto(0, 25)
        pendown()
        goto(100, 25)
    elif s1 == 1 and s2 == 4 and s3 == 7:
        penup()
        goto(25, 100)
        pendown()
        goto(25, 0)
    elif s1 == 2 and s2 == 5 and s3 == 8:
        penup()
        goto(75, 100)
        pendown()
        goto(75, 0)
    elif s1 == 3 and s2 == 6 and s3 == 9:
        penup()
        goto(125, 100)
        pendown()
        goto(125, 0)
    elif s1 == 1 and s2 == 5 and s3 == 9:
        penup()
        goto(0, 100)
        pendown()
        goto(100, 0)
    elif s1 == 3 and s2 == 5 and s3 == 7:
        penup()
        goto(100, 100)
        pendown()
        goto(0, 0)
    speed(10)

def endGame(person):
    if person == "x":
        tkinter.messagebox.showinfo("End Game", "Game Over!, Người chơi x thắng")
    elif person == "o":
        tkinter.messagebox.showinfo("End Game", "Game Over!, Người chơi o thắng")
    elif person == "draw":
        tkinter.messagebox.showinfo("End Game", "Game Over!, Hòa")
    playAgain = tkinter.messagebox.askyesno(message = "Bạn có muốn chơi lại")
    if playAgain == True:
        reset()
    else:
        isopen = False
        close()

def close():
    if isopen == True:
        sure = tkinter.messagebox.askyesno(message = "Trò chơi đang tiếp tục, thoát?")
        if sure == False:
            windowOpen = False
    else:
        windowOpen = False

#  play_tic_tac_toe()

def playtictactoe2():
    global squareToClick
    reset()
    drawTable(m)
    draw = turtle.Screen()
    draw.onclick(getPos)
    # endGame(winner)

playtictactoe2()
