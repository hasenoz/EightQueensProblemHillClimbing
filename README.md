# EightQueensProblemHillClimbing
This program is solving the eight queens problem using hill climbing algorithm.
This algorithm is not best solution method for this problem

The algorithm steps i used:
 - Generate a random chess_board, a queen for each column.
 - Calculate number of threatening for each queen and calculate sum of all threatenings.
 - Find the queen has maximum number of threatening.
 - Find best position for this queen in its own column.
 - If sum of threatening is not lower than before do step 4-5 for next queen that has maximum number of threatening after this queen.
 - If no better solution found go to step 1
 - Do step 2-6 until  sum of all threatenings equals to zero

I solved nine different times but you can rearrange the code for any number.(You must also rearrange the matrix)
