class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' '] * width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''  # de string om terug te geven
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2 * self.width + 1) * '-'  # onderkant van het bord
        s += "\n"
        # hier moeten de nummers nog onder gezet worden
        for x in range(0, self.width):
            s += "|" + str(x)
        s += "|"
        return s  # het bord is compleet, geef het terug

    def add_move(self, col, ox):
        for i in range(self.height - 1, -1, -1):
            if self.data[i][col] == " ":
                self.data[i][col] = ox
                break

    def clear(self):
        self.data = [[' '] * self.width for row in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.set_board('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.set_board('000000') to
           see them alternate in the left column.

           move_string must be a string of one-digit integers.
        """
        next_checker = 'X'  # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allows_move(self, col):
        if col < 0 or col > self.width:
            return False
        else:
            if self.data[0][col] != " ":
                return False
        return True

    def del_move(self, col):
        for i in range(self.height):
            if self.data[i][col] != " ":
                self.data[i][col] = " "
                break

    def is_full(self):
        for i in range(self.height):
            if " " in self.data[i]:
                return False
        else:
            return True

    def wins_for(self, ox):
        for row in range(0, self.height):
            for col in range(0, self.width - 3):
                if self.data[row][col] == ox and \
                        self.data[row][col + 1] == ox and \
                        self.data[row][col + 2] == ox and \
                        self.data[row][col + 3] == ox:
                    return True
                if self.data[row][col] == ox and \
                        self.data[row - 1][col] == ox and \
                        self.data[row - 2][col] == ox and \
                        self.data[row - 3][col] == ox:
                    return True
                if self.data[row][col] == ox and \
                        self.data[row - 1][col - 1] == ox and \
                        self.data[row - 2][col - 2] == ox and \
                        self.data[row - 3][col - 3] == ox:
                    return True
                if self.data[row][col] == ox and \
                        self.data[row - 1][col + 1] == ox and \
                        self.data[row - 2][col + 2] == ox and \
                        self.data[row - 3][col + 3] == ox:
                    return True
        return False

    def host_game(self):
        x = 0
        print("Welkom bij vier op een rij!")
        while True:
            print(self)
            if x == 0:
                col = int(input("Keuze van X: "))
                if self.allows_move(col) is True:
                    self.add_move(col, "X")
                    if self.wins_for("X") is True:
                        print("X wint! -- Gefeliciteerd!")
                        print(self)
                        break
                    print(self)
                    x = 1 - x
                else:
                    print("Ongeldige keuze")
            if x == 1:
                col = int(input("Keuze van O: "))
                if self.allows_move(col) is True:
                    self.add_move(col, "O")
                    if self.wins_for("O") is True:
                        print("O wint! -- Gefeliciteerd!")
                        print(self)
                        break
                    print(self)
                    x = 1 - x
                else:
                    print("Ongeldige keuze")


b = Board(7, 6)

b.host_game()
