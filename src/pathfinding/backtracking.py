from src.pathfinding.path_finder import PathFinder

class Backtracking(PathFinder):
    def __init__(self, board_size, start_point):
        super().__init__('Backtracking', board_size, start_point, 9)

    def get_movements(self):

        # Initialization of Board matrix
        board = [[-1 for i in range(self.board_size)]for i in range(self.board_size)]

        # move_x and move_y define next move of Knight.
        # move_x is for next value of x coordinate
        # move_y is for next value of y coordinate
        move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        move_y = [1, 2, 2, 1, -1, -2, -2, -1]

        # Since the Knight is initially at the first block
        board[self.start_point[0]][self.start_point[1]] = 0

        # Step counter for knight's position
        pos = 1

        # Checking if solution exists or not
        if not self.__solve_kt_util(board, 0, 0, move_x, move_y, pos):
            return []
        else:
            # self.__print_solution(board)
            return self.__get_path(board)

    def __is_safe(self, x, y, board):
        """
            A utility function to check if i,j are valid indexes
            for N*N chessboard
        """
        if 0 <= x < self.board_size and 0 <= y < self.board_size and board[x][y] == -1:
            return True
        return False

    def __print_solution(self, board):
        """
            A utility function to print Chessboard matrix
        """
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(board[i][j], end=' ')
            print()

    def __solve_kt_util(self, board, curr_x, curr_y, move_x, move_y, pos):
        """
            A recursive utility function to solve Knight Tour
            problem
        """

        if pos == self.board_size**2:
            return True

        # Try all next moves from the current coordinate x, y

        for i in range(8):
            new_x = curr_x + move_x[i]
            new_y = curr_y + move_y[i]
            if self.__is_safe(new_x, new_y, board):
                board[new_x][new_y] = pos
                if self.__solve_kt_util(board, new_x, new_y, move_x, move_y, pos + 1):
                    return True

                # Backtracking
                board[new_x][new_y] = -1
        return False

    def __get_path(self, board):
        """
        This function returns the path that the graphical interface will use,
        it represents the solution of the current problem.
            :param board: Game board representation with the correct moves
            :return: list that contains the path to be consumed
        """

        # Initialize a list of tuples to be the size of the board representation
        solution_list = [(0, 0)] * (self.board_size ** 2)

        # Iterate through the board, since the board cells contain the move order,
        # that move order is the position in the solution list, and the value is
        # set to be the coordinates of that cell
        for i in range(self.board_size):
            for j in range(self.board_size):
                solution_list[board[i][j]] = (i, j)

        return solution_list
