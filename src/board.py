import tkinter as tk


class Board(tk.Canvas):
    def __init__(self, board_size, root_widget):
        super().__init__(root_widget)

        self._cells = {}
        self._dark_color = '#0e140c'
        self._clear_color = '#a7ab90'
        self._piece_tag = 'knight'
        self._path_tag = 'path'
        self._background_tag = 'square'
        self._img = tk.PhotoImage(file="../assets/chess_knight.png")
        self._board_size = board_size
        self._cell_size = 45

        self.configure(
            bg='bisque',
            width=self._cell_size*board_size,
            height=self._cell_size*board_size,
            highlightthickness=0
        )

        self.pack(side="top", fill="both", expand=True)
        self.tag_raise(self._piece_tag)

    def generate(self):
        black = self._dark_color
        white = self._clear_color
        color = black

        for row in range(self._board_size):
            if self._board_size % 2 == 0:
                color = black if color is white else white

            for col in range(self._board_size):
                x1 = col * self._cell_size
                y1 = row * self._cell_size
                x2 = x1 + self._cell_size
                y2 = y1 + self._cell_size

                self.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tag=self._background_tag)
                self._cells[(row, col)] = (col * self._cell_size) + self._cell_size // 2, \
                                          (row * self._cell_size) + self._cell_size // 2

                color = black if color is white else white

    def get_cell(self, cell_x, cell_y):
        if cell_x < self._board_size and cell_y < self._board_size:
            return self._cells[(cell_x, cell_y)]
        else:
            print(f"Error for coordinates ({cell_x}, {cell_y}), cell out of board.")
            return None

    def print_cells(self):
        print(f"Cells: {len(self._cells)}")

        for cell_name in self._cells:
            print(cell_name)

    def create_knight(self, cell_x, cell_y):
        self.erase_knight()

        target_cell = self.get_cell(cell_x, cell_y)
        if target_cell:
            self.create_image((target_cell[0], target_cell[1]), image=self._img, tag=self._piece_tag)
        else:
            print(f"Cannot create piece at ({cell_x}, {cell_y}).")

    def draw_path(self, cell_1, cell_2):
        self.create_line(cell_1[0], cell_1[1], cell_2[0], cell_2[1], width=1.3, fill='red', tag=self._path_tag)

    def draw_point(self, cell):
        self.create_oval(cell[0]-3, cell[1]-3, cell[0]+3, cell[1]+3, fill='red', tag=self._path_tag)

    def erase_knight(self):
        self.delete(self._piece_tag)

    def erase_path(self):
        self.delete(self._path_tag)

    def erase_background(self):
        self.delete(self._background_tag)

    def mark_start(self, cell):
        self.create_oval(cell[0]-8, cell[1]-8, cell[0]+8, cell[1]+8, fill='blue', tag=self._path_tag)
