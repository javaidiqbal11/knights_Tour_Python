from src.knights_tour import KnightsTour
from src.pathfinding.backtracking import Backtracking

if __name__ == '__main__':
    size = 8
    start_point = (0, 0)
    algorithm = Backtracking

    app = KnightsTour(size, algorithm, start_point, False)
