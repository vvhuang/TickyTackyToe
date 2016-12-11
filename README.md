# TickyTackyToe

Written in Python, a variation of a variation of the classic tic-tac-toe game, modified from http://blog.computationalcomplexity.org/2002/11/tic-tac-toe-variation.html

Assignment prompt written by Daniel Gusfield: http://web.cs.ucdavis.edu/~gusfield/cs10f13/assignment5.txt

Take a 4 x 4 board and randomly give each square a different number between 2 and 32. There are 
two players X and O. Play goes as follows:

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

Here is an example:

| 12 |  5 |  7 |  2 |
| 14 | 11 |  3 |  8 |
|  4 | 13 |  9 | 30 |
| 24 | 16 | 31 | 21 |

X: calls out 1, O: calls out 3 (to make 4), X: 8 (11), O: 4 (12), X: 3 (7), O: 6 (9). At the point the board looks like:

 O |  5 | X | 2
----------------
14 |  X | O | 8
----------------
 O | 13 | O | 30
----------------
24 | 16 |31| 21
