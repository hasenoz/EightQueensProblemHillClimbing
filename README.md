# EightQueensProblemHillClimbing
This program is solving the eight queens problem using hill climbing algorithm.
This algorithm is not best solution method for this problem

The algorithm steps i used:
1- Generate a random chess_board, a queen for each column.
2- Calculate number of threatening for each queen and calculate sum of all threatenings.
3- Find the queen has maximum number of threatening.
4- Find best position for this queen in its own column.
5- If sum of threatening is not lower than before do step 4-5 for next queen that has maximum number of threatening after this queen.
 - If no better solution found go to step 1
6- Do step 2-6 until  sum of all threatenings equals to zero

I solved nine different times but you can rearrange the code for any number.(You must rearrange the matrix to)
