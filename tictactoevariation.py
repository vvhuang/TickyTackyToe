# tictactoevariation.py
# by: Wei Huang

# global constants
num_square=16
O="O"
X="X"
EMPTY=" "
TIE="TIE"
callnum=18
from random import randrange
import math
lastcall=""

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

"""
def make_board():
    random_board=[]
    for x in range(num_square):
        random=randrange(2,2*num_square+1)
        random_board.append(random)
    print(random_board)
    
    #for a in range(num_square):
        #checkrandom(a,random_board)
    
    for num in range(num_square):
        j=0
        while j<number:
            while random_board[num]==random_board[j] and num!=j:
                random_board[num]=randrange(2,2*num_square+1)
                j=0
            j=j+1
        
    print(random_board)
    return random_board
"""

def make_board():
    random_board=[]
    for i in range(num_square):
        r=randrange(2,2*num_square+1)
        while r in random_board:
            r=randrange(2,2*num_square+1)
        random_board.append(r)
    print(random_board)
    return random_board
random_board=make_board()

"""
def alternate_display_board(random_board):
        print("")
        for i in range(number):
           # if len(str(random_board[i]))==1:
 #               random_board[i]=" "+str(+random_board[i])
            if (i%4)==0:
                if len(str(random_board[i]))==1:
                    print('\t'+" "+str(random_board[i]),end=" ")
                else:
                    print("\t"+str(random_board[i]),end=" ")
            else:
                if len(str(random_board[i]))==1:
                    if i%4==2:
                        print(str(random_board[i])+" ",end=" ")
                    elif i%4==3:
                        print(str(random_board[i]),end=" ")
                    else:
                        print(" "+str(random_board[i]),end=" ")                
                else:
                    print (random_board[i], end = " ")
           
            if  (i +1  <  16):
                if(((i+1) % 4 )== 0):
                    print("\n\t-----------------")
                else:
                    print("|", end=" ")
        print("\n")
"""

def alternate_display_board(random_board):
        print("")
        for i in range(num_square):
            if (i%4)==0:
                if len(str(random_board[i]))==1:
                    print('\t'+" "+str(random_board[i]),end=" ")
                else:
                    print("\t"+str(random_board[i]),end=" ")
            else:
                if len(str(random_board[i]))==1:
                    print(" "+str(random_board[i]),end=" ")                
                else:
                    print (random_board[i], end = " ")
           
            if  (i +1  <  16):
                if(((i+1) % 4 )== 0):
                    print("\n\t-----------------")
                else:
                    print("|", end=" ")
        print("\n")

def display_instruct():
    """Display game instructions."""  
    print (
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe variation.  
    This will be a showdown between your human brain and my silicon processor.  

    Here is a 4 x 4 board with each square randomly given a different number between 
    2 and 32. You will make your move known by entering a number, 1 - 18.
    """)
    alternate_display_board(random_board)
    print(
    """
    There are two players X and O. Play goes as follows:

    step 1:    Player X calls out a number from 1 to 18.
    step 2:    Player O calls out a number from 1 to 18 that player O has not called out before.
    step 3:    Player O adds that number to the last number called out by 
               X, and if that square is on the board and unmarked, that square is marked O.
    step 4:    Player X calls out a number from 1 to 18 that player X has not called out before.
    step 5:    Player X adds that number to the last number called out by 
           O, and if that square is on the board and unmarked, that square is marked X.
    step 6:    Repeat from step 2. 

    Play ends when either X or O has four in a row, or a column, or a diagonal, 
    and is declared a winner; or when no more moves are possible by either player.
    
    Prepare yourself, human.  The ultimate battle is about to begin.
    """)
display_instruct()

def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first call? (y/n): ")
    if go_first == "y":
        print ("\nThen call the first number.")
        hum = O
        com = X
        foundit=1

    else:
        print ("\nI will call first.")
        com = O
        hum = X
        foundit=0
    return com, hum,foundit
computer,human,foundit=pieces()

def record_board():
    """Create new game board."""
    OXboard = []
    for square in range(num_square):
        OXboard.append(EMPTY)
###    print("record_board OXboard:",OXboard)
    return OXboard
OXboard=record_board()

  
def legal_move(proposecall,alreadycall,lastcall,random_board):
    #OXboard and random_board can be together

    if proposecall in range(1,callnum+1):
        a=True
    else:
        a=False
    if proposecall not in alreadycall[:-1]:
        b=True
    else:
        b=False
    if (proposecall+lastcall) in random_board:
        c=True
    else:
        c=False
    if a==b==c==True:
        legal=True
    else:
        legal=False
    return legal
    
def findsquarenum(move):
    for i in range(num_square):
        if random_board[i]==move:
            return i

num_row=int(math.sqrt(num_square))
def winner(board,OXboard,lastcall,already):
    ylist=[]
    # get coordinates of each square
    for y in range(num_row):
        ylist.append([])
        for x in range(num_row):
            ylist[y].append(x+y*num_row)
#    print(ylist)

    
    for j in range(num_row):
        i=0
        # check each colomn
#        print("j",j)
        while (i <= num_row-2) and (board[ylist[i][j]]==board[ylist[i+1][j]]!=EMPTY):
#            print("colomn i",i)
            i=i+1
#            print("colomn i:",i)
        
            if i==num_row-1:
                winner=board[ylist[i][j]]
#####                print(winner)
                return winner
            
    for j in range(num_row):            
        # check each row
        i=0
#        print("j",j)
        while (i<=num_row-2) and board[ylist[j][i]]==board[ylist[j][i+1]]!=EMPTY:
#            print("row i",i)
            i=i+1
#            print("row i:",i)

            if i==num_row-1:
                winner=board[ylist[j][i]]
#####               print(winner)
                return winner
            
    #check each diagonal
    i=0
    while (i<=num_row-2) and board[ylist[i][i]]==board[ylist[i+1][i+1]]!=EMPTY:
#        print("diagonal(1) i",i)
        i=i+1
#        print("diagonal(1) i:",i)
        
        if i==num_row-1:
            winner=board[ylist[i][i]]
#####            print(winner)
            return winner


    i=0
    while (i<=num_row-2) and board[ylist[i][num_row-1-i]]==board[ylist[i+1][num_row-1-(i+1)]]!=EMPTY:
#        print("diagonal(2) i",i)
        i=i+1
#        print("diagonal(2) i:",i)

        if i==num_row-1:
            winner=board[ylist[i][num_row-1-i]]
#####            print(winner)
            return winner

    if EMPTY not in OXboard:       
        return TIE

    for k in range(1,callnum+1):
        if k not in already:
            if k+lastcall in board:
                break
            else:
                if k==callnum:
                    return TIE

    return None
   

lastcall=0
pick=[]        
comalready=[]
humalready=[]
check=0
def human_move(human,foundit,lastcall):

    """Get human move."""
    propose=""
    
    while propose not in range(1,callnum+1):
        propose = ask_number("Call out a number from 1 to 18: ", 1, callnum+1)
        
    humalready.append(propose)
###    print("humalready:",humalready)
    if foundit==1:
        lastcall=propose
#        print("lastcall:",lastcall)
        foundit=2
        legal=False
        print("You called out",propose)
        check=1
        return(lastcall,propose+0,foundit,legal,check)
    

    if foundit==2:
        move=lastcall+propose
#        print("move:",move)
        legal=legal_move(propose,humalready,lastcall,random_board)
#        print("legal:",legal)
        lastcall=propose
#        print("lastcall:",lastcall)
        check=0
        
        return (lastcall,move,foundit,legal,check)


def computer_move(OXboard, computer, human,foundit,comalready,lastcall):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    tryboard = OXboard[:]

    print ("I shall call out number",)
    # computer makes the first move. Choose a random number(1-18), no need to check
    if foundit==0:
        lastcall=0
        foundit=2

        notapplicable="madeuptofillthespot"
        propose=randrange(1,callnum+1)
        print ("\t\t\t",propose,"!!!!!!")
        comalready.append(propose)
###        print("comalready",comalready)
        lastcall=propose
#        print("lastcall",lastcall)
        
        legal=False
        return (notapplicable,lastcall,foundit,legal,comalready)

    # not the first move
    if foundit==2:
        
    # if computer can win, take that move
        pick=[]
        for j in range(num_square):
            
#            print("OXboard:",OXboard)
#            print("OXboard[j]:",OXboard[j])
            
            if OXboard[j]==EMPTY:
#                print("j:",j,"OXboard[j]:",OXboard[j])
                pick.append(j)
#                print("pick",pick)
        for square in pick:
            tryboard[square] = computer
#            print("tryboard:",tryboard)
            if winner(tryboard,OXboard,lastcall,comalready) == computer:
                propose=random_board[square]-lastcall
                if propose in range(1,callnum+1):
                    print("\t\t\t",propose,"!!!!!!")
                    comalready.append(propose)
###                    print("comalready",comalready)
                    lastcall=propose
#                print("lastcall",lastcall)
                
                    legal=True
                
                    return (random_board[square],lastcall,foundit,legal,comalready)
        # done checking this move, undo it
            tryboard[square]=EMPTY
   
    

    # if human can win, block that move       
            tryboard[square] = human
#            print("tryboard: ",tryboard)
            if winner(tryboard,OXboard,lastcall,comalready) == human:
                propose=random_board[square]-lastcall
                if propose in range(1,callnum+1):
                    print("\t\t\t",propose,"!!!!!!")
                    lastcall=propose
#                print ("lastcall",lastcall)
                    comalready.append(lastcall)
###                    print("comalready",comalready)
                    legal=True
                    return (random_board[square],lastcall,foundit,legal,comalready)
        # done checkin this move, undo it
            tryboard[square] = EMPTY

    # since no one can win on next move, pick best open square
        propose=randrange(1,callnum+1)
        legal=legal_move(propose,comalready,lastcall,random_board)
        while legal==False:
            propose=randrange(1,callnum+1)
            legal=legal_move(propose,comalready,lastcall,random_board)
#            print("propose,legal",propose,legal)
        print("\t\t\t",propose,"!!!!!!")
        comalready.append(propose)
###        print("comalready: ",comalready)
        move=propose+lastcall
#        print ("propose: ",propose)
        lastcall=propose

        return (move,lastcall,foundit,legal,comalready)



def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X


#main


turn=O
lastcall=0
propose=0
already=[]
notonboard=0
while not winner(random_board,OXboard,lastcall,already):
    print("turn:",turn)
    if turn == human:
        print("Oh it's your turn! Go ahead!")
        propose,move,foundit,legal,check = human_move(OXboard, foundit,lastcall)
###        print(propose,move,foundit,legal)
        if foundit!=1:
            if legal==True:
                squarenum=findsquarenum(move)
#                print("squarenum:",squarenum)
                random_board[squarenum]=human
####                print(random_board)
                OXboard[squarenum] = human
####                print("OXboard:",OXboard)
                print("You called out",propose,"! And that will make a",move)
               
        if foundit==2:
            if legal==False:
                move=lastcall+propose
                if move not in random_board:
                    notonboard=1
                if propose in humalready[:-1]:
                    notonboard=0 
                    while propose in humalready[:-1]:
                        print("Foolish human! You have already called",propose)
                        print("Here're all the numbers you have called out:")
                        print(humalready[:-1])
                        print("I'll give you another chance to call out a legal number.")
                        propose = ask_number("Call out a number from 1 to 18: ", 1, callnum+1)
                    move=lastcall+propose
                    squarenum=findsquarenum(move)
                    if squarenum!=None:
                        random_board[squarenum]=human
####                        print(random_board)
                        OXboard[squarenum]=human
####                        print("OXboard:",OXboard)
                    else:
                        notonboard=1
                if check!=1:
                    print("You called out",propose,"! And that will make a",move)
                if notonboard==1 and check!=1:
                    print("And",move,"is not on board! HAHA foolish human!")                       
        already=comalready
####        print(already)
    lastcall=propose

            
    if turn == computer:
        print("Oh it's my turn! Sorry!")
        move,propose,foundit,legal,notreallyuseful=computer_move(OXboard, computer, human,foundit,comalready,lastcall)
###        print(move,propose,foundit,legal,notreallyuseful)
        if foundit!=0:
            if legal==True:
                squarenum=findsquarenum(move)
#                print("squarenum: ",squarenum)
                random_board[squarenum]=computer
                print("And that will make a",move)
####                print(random_board)
                OXboard[squarenum] = computer
####                print("OXboard: ",OXboard)
        already=humalready
####        print(already)
    lastcall=propose

            
    alternate_display_board(random_board)        
    turn=next_turn(turn)
the_winner = winner(random_board,OXboard,lastcall,already)

if the_winner==TIE:
    if EMPTY in OXboard:
        print("Turn:",turn)
        if turn==human:
            print("Because there does not exist a number from 1-18 that has not been")
            print("called by you that can make a legal move on the board")
            print("(The human has called out:",humalready,")")
        if turn==computer:
            print("Because there does not exist a number from 1-18 that has not been")
            print("called by me that can make a legal move on the board")
            print("(The computer has called out:",comalready,")")

def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print (the_winner, "won!\n" )
    else:
        print ("It's a tie!\n")

    if the_winner == computer:
        print ("As I predicted, human, I am triumphant once more.  \n" \
              "Proof that computers are superior to humans in all regards.")

    elif the_winner == human:
        print ("No, no!  It cannot be!  Somehow you tricked me, human. \n" \
              "But never again!  I, the computer, so swears it!")

    elif the_winner == TIE:
        print ("You were most lucky, human, and somehow managed to tie me.  \n" \
              "Celebrate today... for this is the best you will ever achieve.")


congrat_winner(the_winner, computer, human)
