# N-Queens...-with-a-Boulder

Recall that in the game of chess, queens attack any piece they can "see" (i.e., there is nothing between the queen and the attacked piece) in the same row, column, or diagonal.

In this assignment, you will generalize this problem to a board of arbitrary (square) size and equivalent number of queens, and add a "boulder" to the board. This boulder has the following properties:

It blocks the space -- no queen may occupy the same space as the boulder
It blocks queen attacks -- two queens on opposite sides of the boulder are not considered to be attacking each other
Given the size of the board (N > 0) and location of the boulder (0 <= boulderX < N and 0 <= boulderY < N), you will implement a hill-climbing algorithm to attempt to solve the problem.

Goal State
There are multiple possible configurations for a goal state, defined only as a state in which no queen is attacking any other queen per the rules above. One of your tasks will be to define an evaluation function for the states such that the goal state has the highest value when the function is applied to it.

Functions
For this program you should write N (n) Python functions:

succ(state, boulderX, boulderY) -- given a state of the board, return a list of all valid successor states
f(state, boulderX, boulderY) -- given a state of the board, return an integer score such that the goal state scores 0
choose_next(curr, boulderX, boulderY) -- given the current state, use succ() to generate the successors and return the selected next state
nqueens(initial_state, boulderX, boulderY) -- run the hill-climbing algorithm from a given initial state, return the convergence state
nqueens_restart(n, k, boulderX, boulderY) -- run the hill-climbing algorithm on an n*n board with random restarts
