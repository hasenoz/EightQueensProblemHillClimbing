import random
import time

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
    # for calculating how many times a queen has been moved at final
    sum_of_fitness, fitness_values = calculate_fitness(chess_board)
    sorted_fitness_values_index = sorted_index_list(fitness_values)
    max_fitness_index = sorted_fitness_values_index[start_index]
    min_fitness_position = find_min_fitness_position(chess_board, max_fitness_index)
    new_chess_board = chess_board.copy()
    new_chess_board[max_fitness_index] = min_fitness_position
    new_sum_of_fitness, new_fitness_values = calculate_fitness(new_chess_board)
    if new_sum_of_fitness < sum_of_fitness:
        sum_of_fitness = new_sum_of_fitness
        fitness_values = new_fitness_values
        chess_board = new_chess_board
        # here we succeeded better board with one arranged queen, we must increase rearranged_queen_count by 1

    else:
        if start_index >= 7:
            return -1, [], []
        sum_of_fitness, fitness_values, chess_board = solve_for_one_queen(chess_board, start_index + 1)

    return sum_of_fitness, fitness_values, chess_board


# solving the board (all queens if possible else restarting in main()
def solve():
    rearranged_queen_count = 1
    chess_board = random_queen_per_column()
    sum_of_fitness, fitness_values, chess_board = solve_for_one_queen(chess_board, 0)

    while sum_of_fitness > 0:
        sum_of_fitness, fitness_values, chess_board = solve_for_one_queen(chess_board, 0)
        rearranged_queen_count += 1
    if sum_of_fitness == -1:
        return True, rearranged_queen_count
    else:
        print("chess board as a list:", chess_board)
        print()
        print_board(chess_board)
        print("rearranged queen count for this chess board: " + str(rearranged_queen_count))
        return False, rearranged_queen_count


def print_board(chess_board):
    for i in range(8):
        for j in range(8):
            if chess_board[j] == i + 1:
                print("Q", end=" ")
            else:
                print("*", end=" ")
        print()


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(str(element), end=" ")
        print()


def main():
    final_values_matrix = []
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


if __name__ == '__main__':
    main()

