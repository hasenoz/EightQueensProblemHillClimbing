import random
import time

# number of total fitness value if all queens are in same row
MAX_FITNESS_VALUE = 56


# this function returns random queens for per column
def random_queen_per_column():
    # chess board has numbers that represent every column's queen's row number
    chess_board = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        # this random int number is first queens row number
        column_queen = random.randint(1, 8)
        # chess_board[0] -> first queens row number = random int row number
        chess_board[i] = column_queen
    return chess_board


# türkçesi uygunluk değeri, this functions calculates total fitness value
def calculate_fitness(chess_board):
    # for finding the max fitness valued queen's column number
    fitness_values = [0, 0, 0, 0, 0, 0, 0, 0]
    sum_of_fitness = 0

    for column_num in range(8):
        queen_row_number = chess_board[column_num]
        fitness = (vertical_threatening(queen_row_number, chess_board, column_num) + cross_threatening(
            queen_row_number,
            chess_board, column_num))
        fitness_values[column_num] = fitness
        sum_of_fitness += fitness
    return sum_of_fitness, fitness_values


# this is impossible because we put one queen for per column
def horizontal_threatening(queen_row_number, chess_board, column_num):
    pass


# sum of all queen's threatening vertically for this particular queen
def vertical_threatening(queen_row_number, chess_board, column_num):
    fitness = 0
    for i in range(8):
        # if its own column continue
        if column_num == i:
            continue
        else:
            if queen_row_number == chess_board[i]:
                fitness += 1
    return fitness


# sum of all queen's threatening cross for this particular queen
def cross_threatening(queen_row_number, chess_board, column_num):
    fitness = 0
    for i in range(8):
        # if its own column continue
        if column_num == i:
            continue
        if abs(i - column_num) == abs(queen_row_number - chess_board[i]):
            fitness += 1
    return fitness


# putting column numbered queen to best position
def rearrange_queen(chess_board, column_num):
    chess_board[column_num] = find_min_fitness_position(chess_board, column_num)


# returns best position for given column_numbered queen
def find_min_fitness_position(chess_board, column_num):
    chess_board_coppy = list(chess_board).copy()
    min_fitness_value = MAX_FITNESS_VALUE
    min_fitness_value_position = 0
    for i in range(8):
        chess_board_coppy[column_num] = i + 1
        fitness_value = calculate_fitness(chess_board_coppy)[0]
        if min_fitness_value > fitness_value:
            min_fitness_value = fitness_value
            min_fitness_value_position = i + 1
    return min_fitness_value_position


def sorted_index_list(list_of_values):
    sorted_values = []
    sorted_index = []
    for i in range(len(list_of_values)):
        sorted_values.append([i, list_of_values[i]])
    sorted_values = sorted(sorted_values, key=lambda l: l[1], reverse=True)
    for i in range(len(sorted_values)):
        sorted_index.append(sorted_values[i][0])
    return sorted_index


# solving for only one queen
def solve_for_one_queen(chess_board, start_index):
    # calculated fitness
    sum_of_fitness, fitness_values = calculate_fitness(chess_board)
    # sorted fitness values list by value but with stored index as keys
    sorted_fitness_values_index = sorted_index_list(fitness_values)
    # finding the max fitness value
    max_fitness_index = sorted_fitness_values_index[start_index]
    # finding the best position for all seven possible squares for this particular queen
    min_fitness_position = find_min_fitness_position(chess_board, max_fitness_index)
    # we need a new copied chess board for not changing anything before checking if it is better than before
    new_chess_board = chess_board.copy()
    new_chess_board[max_fitness_index] = min_fitness_position
    # calculating total fitness value for new rearranged chess_board
    new_sum_of_fitness, new_fitness_values = calculate_fitness(new_chess_board)
    # checking it if it is better than before: if it is than assign copied board as real one
    if new_sum_of_fitness < sum_of_fitness:
        sum_of_fitness = new_sum_of_fitness
        fitness_values = new_fitness_values
        chess_board = new_chess_board
    # if there is no better solution for max fitness valued queen than continue with second max valued queen
    else:
        # if there is no better solution for all queens than it is a local max issue return -1 and use this -1 for restarting
        # this solving is better than using a local issue limit(like do 100 loop; if not found restart)
        # the limit can interrupt the solution; we must look all possible queens
        if start_index >= 7:
            return -1, [], []
        # calculate next max valued queen recursively
        sum_of_fitness, fitness_values, chess_board = solve_for_one_queen(chess_board, start_index + 1)

    return sum_of_fitness, fitness_values, chess_board


# solving the board for all queens if possible else restarting in main()
def solve():
    # for finding how many times a queen moved in this process(but only for this board,not restarts include)
    # if the restarts will be calculated than sum all values in main()
    rearranged_queen_count = 1
    chess_board = random_queen_per_column()
    # we started with max fitness valued because of sorted_fitness_values[0] -> max fitness valued queen
    sum_of_fitness, fitness_values, chess_board = solve_for_one_queen(chess_board, 0)
    # if sum of fitness not zero problem not solved
    while sum_of_fitness > 0:
        sum_of_fitness, fitness_values, chess_board = solve_for_one_queen(chess_board, 0)
        # if solve for one queen works and not returns -1 than a queen has been arranged
        rearranged_queen_count += 1
    if sum_of_fitness == -1:
        return True, rearranged_queen_count
    else:
        print("chess board as a list:", chess_board)
        print()
        print_board(chess_board)
        print("rearranged queen count for this chess board: " + str(rearranged_queen_count))
        # returning rearranged_queen_count for calculating the sum of all in main()
        return False, rearranged_queen_count


# for visual chess board
def print_board(chess_board):
    for i in range(8):
        for j in range(8):
            if chess_board[j] == i + 1:
                print("Q", end=" ")
            else:
                print("*", end=" ")
        print()


# easy printing method for final values matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(str(element), end=" ")
        print()


def main():
    # this will hold the values of all 9 solved problems
    final_values_matrix = []
    # range is 9 because we must solve the problem 9 different times
    for i in range(9):
        # for all rearranged queens count for this particular solution
        total_rearranged_queen_count = 0
        start_time = time.time()
        restart_count = -1
        is_local_maximum = True
        while is_local_maximum:
            is_local_maximum, rearranged_queen_count = solve()
            total_rearranged_queen_count += rearranged_queen_count
            restart_count += 1
        print("restarted " + str(restart_count) + " times")
        end_time = time.time()
        time_length = end_time - start_time
        time_length_formatted = "{:.4f}".format(time_length)
        print("worked " + str(time_length_formatted) + " seconds")
        final_values_matrix.append([total_rearranged_queen_count, restart_count, time_length_formatted])
        print()
        print("-------------------------------------")
        print()
    print_matrix(final_values_matrix)


# run
if __name__ == '__main__':
    main()
