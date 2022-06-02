from abc import ABC, abstractmethod

class PathFinder(ABC):
    def __init__(self, name, board_size, start_point, max_size):
        self.name = name
        self.max_size = max_size
        self.board_size = board_size
        self.start_point = start_point

    @abstractmethod
    def get_movements(self):
        raise NotImplementedError
