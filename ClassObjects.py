class Empty:
    def __init__(self, pos):
        self.pos = pos

        self.pos_one_conversion_dic = {
            "8": 0,
            "7": 1,
            "6": 2,
            "5": 3,
            "4": 4,
            "3": 5,
            "2": 6,
            "1": 7,
        }

        self.pos_two_conversion_dic = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
        }

        self.y = self.pos_one_conversion_dic[pos[0]]
        self.x = self.pos_two_conversion_dic[pos[1]]


class Piece(Empty):
    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        super().__init__(pos)


class Pawn(Piece):
    def __init__(self, color, pos):
        super().__init__("P", color, pos)

    def get_possible_moves(self, board):
        possibleMoves = []

        if self.color == "b":
            if self.y + 1 < 8:
                if type(board.squares[(self.y + 1)][(self.x)]) is Empty:
                    possibleMoves.append((self.y + 1, self.x))
        if self.color == "b":
            if self.y == 1:
                if type(board.squares[(self.y + 2)][(self.x)]) is Empty:
                    possibleMoves.append((self.y + 2, self.x))
        if self.color == "b":
            if self.y + 1 < 8 and self.x + 1 < 8:
                if type(board.squares[(self.y + 1)][(self.x + 1)]) is not Empty:
                    if board.squares[self.y + 1][self.x + 1].color != self.color:
                        possibleMoves.append((self.y + 1, self.x + 1))
        if self.color == "b":
            if self.y + 1 < 8 and self.x - 1 > -1:
                if type(board.squares[(self.y + 1)][(self.x - 1)]) is not Empty:
                    if board.squares[self.y + 1][self.x - 1].color != self.color:
                        possibleMoves.append((self.y + 1, self.x - 1))

        if self.color == "w":
            if self.y - 1 > -1:
                if type(board.squares[(self.y - 1)][(self.x)]) is Empty:
                    possibleMoves.append((self.y - 1, self.x))
        if self.color == "w":
            if self.y == 6:
                if type(board.squares[(self.y - 2)][(self.x)]) is Empty:
                    possibleMoves.append((self.y - 2, self.x))
        if self.color == "w":
            if self.y - 1 > -1 and self.x - 1 > -1:
                if type(board.squares[(self.y - 1)][(self.x - 1)]) is not Empty:
                    if board.squares[self.y - 1][self.x - 1].color != self.color:
                        possibleMoves.append((self.y - 1, self.x - 1))
        if self.color == "w":
            if self.y - 1 > -1 and self.x + 1 < 8:
                if type(board.squares[(self.y - 1)][(self.x + 1)]) is not Empty:
                    if board.squares[self.y - 1][self.x + 1].color != self.color:
                        possibleMoves.append((self.y - 1, self.x + 1))
        return possibleMoves


class Rook(Piece):
    def __init__(self, color, pos):
        super().__init__("R", color, pos)

    def get_possible_moves(self, board):
        possibleMoves = []

        if self.y + 1 < 8:
            if type(board.squares[(self.y + 1)][(self.x)]) is Empty:
                possibleMoves.append((self.y + 1, self.x))

            elif board.squares[self.y + 1][self.x].color != self.color:
                possibleMoves.append((self.y + 1, self.x))

        if self.y - 1 > -1:
            if type(board.squares[(self.y - 1)][self.x]) is Empty:
                possibleMoves.append((self.y - 1, self.x))

            elif board.squares[self.y - 1][self.x].color != self.color:
                possibleMoves.append((self.y - 1, self.x))

        if self.x + 1 < 8:
            if type(board.squares[(self.y)][self.x + 1]) is Empty:
                possibleMoves.append((self.y, self.x + 1))

            elif board.squares[self.y][self.x + 1].color != self.color:
                possibleMoves.append((self.y, self.x + 1))

        if self.x - 1 > -1:
            if type(board.squares[(self.y)][self.x - 1]) is Empty:
                possibleMoves.append((self.y, self.x - 1))

            elif board.squares[self.y][self.x - 1].color != self.color:
                possibleMoves.append((self.y, self.x - 1))

        if self.x + 2 < 8:
            if type(board.squares[(self.y)][(self.x + 2)]) is Empty:
                possibleMoves.append((self.y, self.x + 2))

            elif board.squares[self.y][self.x + 2].color != self.color:
                possibleMoves.append((self.y, self.x + 2))

        if self.x - 2 > -1:
            if type(board.squares[(self.y)][self.x - 2]) is Empty:
                possibleMoves.append((self.y, self.x - 2))

            elif board.squares[self.y][self.x - 2].color != self.color:
                possibleMoves.append((self.y, self.x - 2))

        if self.y + 2 < 8:
            if type(board.squares[(self.y + 2)][self.x]) is Empty:
                possibleMoves.append((self.y + 2, self.x))

            elif board.squares[self.y + 2][self.x].color != self.color:
                possibleMoves.append((self.y + 2, self.x))

        if self.y - 2 > -1:
            if type(board.squares[(self.y - 2)][self.x]) is Empty:
                possibleMoves.append((self.y - 2, self.x))

            elif board.squares[self.y - 2][self.x].color != self.color:
                possibleMoves.append((self.y - 2, self.x))

        if self.x + 3 < 8:
            if type(board.squares[(self.y)][(self.x + 3)]) is Empty:
                possibleMoves.append((self.y, self.x + 3))

            elif board.squares[self.y][self.x + 3].color != self.color:
                possibleMoves.append((self.y, self.x + 3))

        if self.x - 3 > -1:
            if type(board.squares[(self.y)][self.x - 3]) is Empty:
                possibleMoves.append((self.y, self.x - 3))

            elif board.squares[self.y][self.x - 3].color != self.color:
                possibleMoves.append((self.y, self.x - 3))

        if self.y + 3 < 8:
            if type(board.squares[(self.y + 3)][self.x]) is Empty:
                possibleMoves.append((self.y + 3, self.x))

            elif board.squares[self.y + 3][self.x].color != self.color:
                possibleMoves.append((self.y + 3, self.x))

        if self.y - 3 > -1:
            if type(board.squares[(self.y - 3)][self.x]) is Empty:
                possibleMoves.append((self.y - 3, self.x))

            elif board.squares[self.y - 3][self.x].color != self.color:
                possibleMoves.append((self.y - 3, self.x))

        if self.x + 4 < 8:
            if type(board.squares[(self.y)][(self.x + 4)]) is Empty:
                possibleMoves.append((self.y, self.x + 4))

            elif board.squares[self.y][self.x + 4].color != self.color:
                possibleMoves.append((self.y, self.x + 4))

        if self.x - 4 > -1:
            if type(board.squares[(self.y)][self.x - 4]) is Empty:
                possibleMoves.append((self.y, self.x - 4))

            elif board.squares[self.y][self.x - 4].color != self.color:
                possibleMoves.append((self.y, self.x - 4))

        if self.y + 4 < 8:
            if type(board.squares[(self.y + 4)][self.x]) is Empty:
                possibleMoves.append((self.y + 4, self.x))

            elif board.squares[self.y + 4][self.x].color != self.color:
                possibleMoves.append((self.y + 4, self.x))

        if self.y - 4 > -1:
            if type(board.squares[(self.y - 4)][self.x]) is Empty:
                possibleMoves.append((self.y - 4, self.x))

            elif board.squares[self.y - 4][self.x].color != self.color:
                possibleMoves.append((self.y - 4, self.x))

        if self.x + 5 < 8:
            if type(board.squares[(self.y)][(self.x + 5)]) is Empty:
                possibleMoves.append((self.y, self.x + 5))

            elif board.squares[self.y][self.x + 5].color != self.color:
                possibleMoves.append((self.y, self.x + 5))

        if self.x - 5 > -1:
            if type(board.squares[(self.y)][self.x - 5]) is Empty:
                possibleMoves.append((self.y, self.x - 5))

            elif board.squares[self.y][self.x - 5].color != self.color:
                possibleMoves.append((self.y, self.x - 5))

        if self.y + 5 < 8:
            if type(board.squares[(self.y + 5)][self.x]) is Empty:
                possibleMoves.append((self.y + 5, self.x))

            elif board.squares[self.y + 5][self.x].color != self.color:
                possibleMoves.append((self.y + 5, self.x))

        if self.y - 5 > -1:
            if type(board.squares[(self.y - 5)][self.x]) is Empty:
                possibleMoves.append((self.y - 5, self.x))

            elif board.squares[self.y - 5][self.x].color != self.color:
                possibleMoves.append((self.y - 5, self.x))

        if self.x + 6 < 8:
            if type(board.squares[(self.y)][(self.x + 6)]) is Empty:
                possibleMoves.append((self.y, self.x + 6))

            elif board.squares[self.y][self.x + 6].color != self.color:
                possibleMoves.append((self.y, self.x + 6))

        if self.x - 6 > -1:
            if type(board.squares[(self.y)][self.x - 6]) is Empty:
                possibleMoves.append((self.y, self.x - 6))

            elif board.squares[self.y][self.x - 6].color != self.color:
                possibleMoves.append((self.y, self.x - 6))

        if self.y + 6 < 8:
            if type(board.squares[(self.y + 6)][self.x]) is Empty:
                possibleMoves.append((self.y + 6, self.x))

            elif board.squares[self.y + 6][self.x].color != self.color:
                possibleMoves.append((self.y + 6, self.x))

        if self.y - 6 > -1:
            if type(board.squares[(self.y - 6)][self.x]) is Empty:
                possibleMoves.append((self.y - 6, self.x))

            elif board.squares[self.y - 6][self.x].color != self.color:
                possibleMoves.append((self.y - 6, self.x))

        if self.x + 7 < 8:
            if type(board.squares[(self.y)][(self.x + 7)]) is Empty:
                possibleMoves.append((self.y, self.x + 7))

            elif board.squares[self.y][self.x + 7].color != self.color:
                possibleMoves.append((self.y, self.x + 7))

        if self.x - 7 > -1:
            if type(board.squares[(self.y)][self.x - 7]) is Empty:
                possibleMoves.append((self.y, self.x - 7))

            elif board.squares[self.y][self.x - 7].color != self.color:
                possibleMoves.append((self.y, self.x - 7))

        if self.y + 7 < 8:
            if type(board.squares[(self.y + 7)][self.x]) is Empty:
                possibleMoves.append((self.y + 7, self.x))

            elif board.squares[self.y + 7][self.x].color != self.color:
                possibleMoves.append((self.y + 7, self.x))

        if self.y - 7 > -1:
            if type(board.squares[(self.y - 7)][self.x]) is Empty:
                possibleMoves.append((self.y - 7, self.x))

            elif board.squares[self.y - 7][self.x].color != self.color:
                possibleMoves.append((self.y - 7, self.x))

        return possibleMoves


class Knight(Piece):
    def __init__(self, color, pos):
        super().__init__("N", color, pos)

    def get_possible_moves(self, board):
        possibleMoves = []

        if self.y + 1 < 8 and self.x + 2 < 8:
            if type(board.squares[self.y + 1][self.x + 2]) is Empty:
                possibleMoves.append((self.y + 1, self.x + 2))

            elif board.squares[self.y + 1][self.x + 2].color != self.color:
                possibleMoves.append([self.y + 1][self.x + 2])

        if self.y + 2 < 8 and self.x + 1 < 8:
            if type(board.squares[self.y + 2][self.x + 1]) is Empty:
                possibleMoves.append((self.y + 2, self.x + 1))

            elif board.squares[self.y + 2][self.x + 1].color != self.color:
                possibleMoves.append([self.y + 2][self.x + 1])

        if self.y - 1 > -1 and self.x - 2 > -1:
            if type(board.squares[self.y - 1][self.x - 2]) is Empty:
                possibleMoves.append((self.y - 1, self.x - 2))

            elif board.squares[self.y - 1][self.x - 2].color != self.color:
                possibleMoves.append([self.y - 1][self.x - 2])

        if self.y - 2 > -1 and self.x - 1 > -1:
            if type(board.squares[self.y - 2][self.x - 1]) is Empty:
                possibleMoves.append((self.y - 2, self.x - 1))

            elif board.squares[self.y - 2][self.x - 1].color != self.color:
                possibleMoves.append([self.y - 2][self.x - 1])

        if self.y - 1 > -1 and self.x + 2 < 8:
            if type(board.squares[self.y - 1][self.x + 2]) is Empty:
                possibleMoves.append((self.y - 1, self.x + 2))

            elif board.squares[self.y - 1][self.x + 2].color != self.color:
                possibleMoves.append([self.y - 1][self.x + 2])

        if self.y - 2 > -1 and self.x + 1 < 8:
            if type(board.squares[self.y - 2][self.x + 1]) is Empty:
                possibleMoves.append((self.y - 2, self.x + 1))

            elif board.squares[self.y - 2][self.x + 1].color != self.color:
                possibleMoves.append([self.y - 2][self.x + 1])

        if self.y + 1 < 8 and self.x - 2 > -1:
            if type(board.squares[self.y + 1][self.x - 2]) is Empty:
                possibleMoves.append((self.y + 1, self.x - 2))

            elif board.squares[self.y + 1][self.x - 2].color != self.color:
                possibleMoves.append([self.y + 1][self.x - 2])

        if self.y + 2 < 8 and self.x - 1 > -1:
            if type(board.squares[self.y + 2][self.x - 1]) is Empty:
                possibleMoves.append((self.y + 2, self.x - 1))

            elif board.squares[self.y + 2][self.x + 1].color != self.color:
                possibleMoves.append([self.y + 2][self.x - 1])

        return possibleMoves


class Bishop(Piece):
    def __init__(self, color, pos):
        super().__init__("B", color, pos)

    def get_possible_moves(self, board):
        possibleMoves = []

        if self.y + 1 < 8 and self.x + 1 < 8:
            if type(board.squares[self.y + 1][self.x + 1]) is Empty:
                possibleMoves.append((self.y + 1, self.x + 1))

            elif board.squares[self.y + 1][self.x + 1].color != self.color:
                possibleMoves.append((self.y + 1, self.x + 1))

        if self.y + 2 < 8 and self.x + 2 < 8:
            if type(board.squares[self.y + 2][self.x + 2]) is Empty:
                possibleMoves.append((self.y + 2, self.x + 2))

            elif board.squares[self.y + 2][self.x + 2].color != self.color:
                possibleMoves.append((self.y + 2, self.x + 2))

        if self.y + 3 < 8 and self.x + 3 < 8:
            if type(board.squares[self.y + 3][self.x + 3]) is Empty:
                possibleMoves.append((self.y + 3, self.x + 3))

            elif board.squares[self.y + 3][self.x + 3].color != self.color:
                possibleMoves.append((self.y + 3, self.x + 3))

        if self.y + 4 < 8 and self.x + 4 < 8:
            if type(board.squares[self.y + 4][self.x + 4]) is Empty:
                possibleMoves.append((self.y + 4, self.x + 4))

            elif board.squares[self.y + 4][self.x + 4].color != self.color:
                possibleMoves.append((self.y + 4, self.x + 4))

        if self.y + 5 < 8 and self.x + 5 < 8:
            if type(board.squares[self.y + 5][self.x + 5]) is Empty:
                possibleMoves.append((self.y + 5, self.x + 5))

            elif board.squares[self.y + 5][self.x + 5].color != self.color:
                possibleMoves.append((self.y + 5, self.x + 5))

        if self.y + 6 < 8 and self.x + 6 < 8:
            if type(board.squares[self.y + 6][self.x + 6]) is Empty:
                possibleMoves.append((self.y + 6, self.x + 6))

            elif board.squares[self.y + 6][self.x + 6].color != self.color:
                possibleMoves.append((self.y + 6, self.x + 6))

        if self.y + 7 < 8 and self.x + 7 < 8:
            if type(board.squares[self.y + 7][self.x + 7]) is Empty:
                possibleMoves.append((self.y + 7, self.x + 7))

            elif board.squares[self.y + 7][self.x + 7].color != self.color:
                possibleMoves.append((self.y + 7, self.x + 7))

        if self.y - 1 > -1 and self.x - 1 > -1:
            if type(board.squares[self.y - 1][self.x - 1]) is Empty:
                possibleMoves.append((self.y - 1, self.x - 1))

            elif board.squares[self.y - 1][self.x - 1].color != self.color:
                possibleMoves.append((self.y - 1, self.x - 1))

        if self.y - 2 > -1 and self.x - 2 > -1:
            if type(board.squares[self.y - 2][self.x - 2]) is Empty:
                possibleMoves.append((self.y - 2, self.x - 2))

            elif board.squares[self.y - 2][self.x - 2].color != self.color:
                possibleMoves.append((self.y - 2, self.x - 2))

        if self.y - 3 > -1 and self.x - 3 > -1:
            if type(board.squares[self.y - 3][self.x - 3]) is Empty:
                possibleMoves.append((self.y - 3, self.x - 3))

            elif board.squares[self.y - 3][self.x - 3].color != self.color:
                possibleMoves.append((self.y - 3, self.x - 3))

        if self.y - 4 > -1 and self.x - 4 > -1:
            if type(board.squares[self.y - 4][self.x - 4]) is Empty:
                possibleMoves.append((self.y - 4, self.x - 4))

            elif board.squares[self.y - 4][self.x - 4].color != self.color:
                possibleMoves.append((self.y - 4, self.x - 4))

        if self.y - 5 > -1 and self.x - 5 > -1:
            if type(board.squares[self.y - 5][self.x - 5]) is Empty:
                possibleMoves.append((self.y - 5, self.x - 5))

            elif board.squares[self.y - 5][self.x - 5].color != self.color:
                possibleMoves.append((self.y - 5, self.x - 5))

        if self.y - 6 > -1 and self.x - 6 > -1:
            if type(board.squares[self.y - 6][self.x - 6]) is Empty:
                possibleMoves.append((self.y - 6, self.x - 6))

            elif board.squares[self.y - 6][self.x - 6].color != self.color:
                possibleMoves.append((self.y - 6, self.x - 6))

        if self.y - 7 > -1 and self.x - 7 > -1:
            if type(board.squares[self.y - 7][self.x - 7]) is Empty:
                possibleMoves.append((self.y - 7, self.x - 7))

            elif board.squares[self.y - 7][self.x - 7].color != self.color:
                possibleMoves.append((self.y - 7, self.x - 7))

        if self.y + 1 < 8 and self.x - 1 > -1:
            if type(board.squares[self.y + 1][self.x - 1]) is Empty:
                possibleMoves.append((self.y + 1, self.x - 1))

            elif board.squares[self.y + 1][self.x - 1].color != self.color:
                possibleMoves.append((self.y + 1, self.x - 1))

        if self.y + 2 < 8 and self.x - 2 > -1:
            if type(board.squares[self.y + 2][self.x - 2]) is Empty:
                possibleMoves.append((self.y + 2, self.x - 2))

            elif board.squares[self.y + 2][self.x - 2].color != self.color:
                possibleMoves.append((self.y + 2, self.x - 2))

        if self.y + 3 < 8 and self.x - 3 > -1:
            if type(board.squares[self.y + 3][self.x - 3]) is Empty:
                possibleMoves.append((self.y + 3, self.x - 3))

            elif board.squares[self.y + 3][self.x - 3].color != self.color:
                possibleMoves.append((self.y + 3, self.x - 3))

        if self.y + 4 < 8 and self.x - 4 > -1:
            if type(board.squares[self.y + 4][self.x - 4]) is Empty:
                possibleMoves.append((self.y + 4, self.x - 4))

            elif board.squares[self.y + 4][self.x - 4].color != self.color:
                possibleMoves.append((self.y + 4, self.x - 4))

        if self.y + 5 < 8 and self.x - 5 > -1:
            if type(board.squares[self.y + 5][self.x - 5]) is Empty:
                possibleMoves.append((self.y + 5, self.x - 5))

            elif board.squares[self.y + 5][self.x - 5].color != self.color:
                possibleMoves.append((self.y + 5, self.x - 5))

        if self.y + 6 < 8 and self.x - 6 > -1:
            if type(board.squares[self.y + 6][self.x - 6]) is Empty:
                possibleMoves.append((self.y + 6, self.x - 6))

            elif board.squares[self.y + 6][self.x - 6].color != self.color:
                possibleMoves.append((self.y + 6, self.x - 6))

        if self.y + 7 < 8 and self.x - 7 > -1:
            if type(board.squares[self.y + 7][self.x - 7]) is Empty:
                possibleMoves.append((self.y + 7, self.x - 7))

            elif board.squares[self.y + 7][self.x - 7].color != self.color:
                possibleMoves.append((self.y + 7, self.x - 7))

        if self.y - 1 > -1 and self.x + 1 < 8:
            if type(board.squares[self.y - 1][self.x + 1]) is Empty:
                possibleMoves.append((self.y - 1, self.x + 1))

            elif board.squares[self.y - 1][self.x + 1].color != self.color:
                possibleMoves.append((self.y - 1, self.x + 1))

        if self.y - 2 > -1 and self.x + 2 < 8:
            if type(board.squares[self.y - 2][self.x + 2]) is Empty:
                possibleMoves.append((self.y - 2, self.x + 2))

            elif board.squares[self.y - 2][self.x + 2].color != self.color:
                possibleMoves.append((self.y - 2, self.x + 2))

        if self.y - 3 > -1 and self.x + 3 < 8:
            if type(board.squares[self.y - 3][self.x + 3]) is Empty:
                possibleMoves.append((self.y - 3, self.x + 3))

            elif board.squares[self.y - 3][self.x + 3].color != self.color:
                possibleMoves.append((self.y - 3, self.x + 3))

        if self.y - 4 > -1 and self.x + 4 < 8:
            if type(board.squares[self.y - 4][self.x + 4]) is Empty:
                possibleMoves.append((self.y - 4, self.x + 4))

            elif board.squares[self.y - 4][self.x + 4].color != self.color:
                possibleMoves.append((self.y - 4, self.x + 4))

        if self.y - 5 > -1 and self.x + 5 < 8:
            if type(board.squares[self.y - 5][self.x + 5]) is Empty:
                possibleMoves.append((self.y - 5, self.x + 5))

            elif board.squares[self.y - 5][self.x + 5].color != self.color:
                possibleMoves.append((self.y - 5, self.x + 5))

        if self.y - 6 > -1 and self.x + 6 < 8:
            if type(board.squares[self.y - 6][self.x + 6]) is Empty:
                possibleMoves.append((self.y - 6, self.x + 6))

            elif board.squares[self.y - 6][self.x + 6].color != self.color:
                possibleMoves.append((self.y - 6, self.x + 6))

        if self.y - 7 > -1 and self.x + 7 < 8:
            if type(board.squares[self.y - 7][self.x + 7]) is Empty:
                possibleMoves.append((self.y - 7, self.x + 7))

            elif board.squares[self.y - 7][self.x + 7].color != self.color:
                possibleMoves.append((self.y - 7, self.x + 7))

        return possibleMoves


class Queen(Piece):
    def __init__(self, color, pos):
        super().__init__("Q", color, pos)

    def get_possible_moves(self, board):
        possibleMoves = []

        if self.y + 1 < 8:
            if type(board.squares[(self.y + 1)][(self.x)]) is Empty:
                possibleMoves.append((self.y + 1, self.x))

            elif board.squares[self.y + 1][self.x].color != self.color:
                possibleMoves.append((self.y + 1, self.x))

        if self.y - 1 > -1:
            if type(board.squares[(self.y - 1)][self.x]) is Empty:
                possibleMoves.append((self.y - 1, self.x))

            elif board.squares[self.y - 1][self.x].color != self.color:
                possibleMoves.append((self.y - 1, self.x))

        if self.x + 1 < 8:
            if type(board.squares[(self.y)][self.x + 1]) is Empty:
                possibleMoves.append((self.y, self.x + 1))

            elif board.squares[self.y][self.x + 1].color != self.color:
                possibleMoves.append((self.y, self.x + 1))

        if self.x - 1 > -1:
            if type(board.squares[(self.y)][self.x - 1]) is Empty:
                possibleMoves.append((self.y, self.x - 1))

            elif board.squares[self.y][self.x - 1].color != self.color:
                possibleMoves.append((self.y, self.x - 1))

        if self.x + 2 < 8:
            if type(board.squares[(self.y)][(self.x + 2)]) is Empty:
                possibleMoves.append((self.y, self.x + 2))

            elif board.squares[self.y][self.x + 2].color != self.color:
                possibleMoves.append((self.y, self.x + 2))

        if self.x - 2 > -1:
            if type(board.squares[(self.y)][self.x - 2]) is Empty:
                possibleMoves.append((self.y, self.x - 2))

            elif board.squares[self.y][self.x - 2].color != self.color:
                possibleMoves.append((self.y, self.x - 2))

        if self.y + 2 < 8:
            if type(board.squares[(self.y + 2)][self.x]) is Empty:
                possibleMoves.append((self.y + 2, self.x))

            elif board.squares[self.y + 2][self.x].color != self.color:
                possibleMoves.append((self.y + 2, self.x))

        if self.y - 2 > -1:
            if type(board.squares[(self.y - 2)][self.x]) is Empty:
                possibleMoves.append((self.y - 2, self.x))

            elif board.squares[self.y - 2][self.x].color != self.color:
                possibleMoves.append((self.y - 2, self.x))

        if self.x + 3 < 8:
            if type(board.squares[(self.y)][(self.x + 3)]) is Empty:
                possibleMoves.append((self.y, self.x + 3))

            elif board.squares[self.y][self.x + 3].color != self.color:
                possibleMoves.append((self.y, self.x + 3))

        if self.x - 3 > -1:
            if type(board.squares[(self.y)][self.x - 3]) is Empty:
                possibleMoves.append((self.y, self.x - 3))

            elif board.squares[self.y][self.x - 3].color != self.color:
                possibleMoves.append((self.y, self.x - 3))

        if self.y + 3 < 8:
            if type(board.squares[(self.y + 3)][self.x]) is Empty:
                possibleMoves.append((self.y + 3, self.x))

            elif board.squares[self.y + 3][self.x].color != self.color:
                possibleMoves.append((self.y + 3, self.x))

        if self.y - 3 > -1:
            if type(board.squares[(self.y - 3)][self.x]) is Empty:
                possibleMoves.append((self.y - 3, self.x))

            elif board.squares[self.y - 3][self.x].color != self.color:
                possibleMoves.append((self.y - 3, self.x))

        if self.x + 4 < 8:
            if type(board.squares[(self.y)][(self.x + 4)]) is Empty:
                possibleMoves.append((self.y, self.x + 4))

            elif board.squares[self.y][self.x + 4].color != self.color:
                possibleMoves.append((self.y, self.x + 4))

        if self.x - 4 > -1:
            if type(board.squares[(self.y)][self.x - 4]) is Empty:
                possibleMoves.append((self.y, self.x - 4))

            elif board.squares[self.y][self.x - 4].color != self.color:
                possibleMoves.append((self.y, self.x - 4))

        if self.y + 4 < 8:
            if type(board.squares[(self.y + 4)][self.x]) is Empty:
                possibleMoves.append((self.y + 4, self.x))

            elif board.squares[self.y + 4][self.x].color != self.color:
                possibleMoves.append((self.y + 4, self.x))

        if self.y - 4 > -1:
            if type(board.squares[(self.y - 4)][self.x]) is Empty:
                possibleMoves.append((self.y - 4, self.x))

            elif board.squares[self.y - 4][self.x].color != self.color:
                possibleMoves.append((self.y - 4, self.x))

        if self.x + 5 < 8:
            if type(board.squares[(self.y)][(self.x + 5)]) is Empty:
                possibleMoves.append((self.y, self.x + 5))

            elif board.squares[self.y][self.x + 5].color != self.color:
                possibleMoves.append((self.y, self.x + 5))

        if self.x - 5 > -1:
            if type(board.squares[(self.y)][self.x - 5]) is Empty:
                possibleMoves.append((self.y, self.x - 5))

            elif board.squares[self.y][self.x - 5].color != self.color:
                possibleMoves.append((self.y, self.x - 5))

        if self.y + 5 < 8:
            if type(board.squares[(self.y + 5)][self.x]) is Empty:
                possibleMoves.append((self.y + 5, self.x))

            elif board.squares[self.y + 5][self.x].color != self.color:
                possibleMoves.append((self.y + 5, self.x))

        if self.y - 5 > -1:
            if type(board.squares[(self.y - 5)][self.x]) is Empty:
                possibleMoves.append((self.y - 5, self.x))

            elif board.squares[self.y - 5][self.x].color != self.color:
                possibleMoves.append((self.y - 5, self.x))

        if self.x + 6 < 8:
            if type(board.squares[(self.y)][(self.x + 6)]) is Empty:
                possibleMoves.append((self.y, self.x + 6))

            elif board.squares[self.y][self.x + 6].color != self.color:
                possibleMoves.append((self.y, self.x + 6))

        if self.x - 6 > -1:
            if type(board.squares[(self.y)][self.x - 6]) is Empty:
                possibleMoves.append((self.y, self.x - 6))

            elif board.squares[self.y][self.x - 6].color != self.color:
                possibleMoves.append((self.y, self.x - 6))

        if self.y + 6 < 8:
            if type(board.squares[(self.y + 6)][self.x]) is Empty:
                possibleMoves.append((self.y + 6, self.x))

            elif board.squares[self.y + 6][self.x].color != self.color:
                possibleMoves.append((self.y + 6, self.x))

        if self.y - 6 > -1:
            if type(board.squares[(self.y - 6)][self.x]) is Empty:
                possibleMoves.append((self.y - 6, self.x))

            elif board.squares[self.y - 6][self.x].color != self.color:
                possibleMoves.append((self.y - 6, self.x))

        if self.x + 7 < 8:
            if type(board.squares[(self.y)][(self.x + 7)]) is Empty:
                possibleMoves.append((self.y, self.x + 7))

            elif board.squares[self.y][self.x + 7].color != self.color:
                possibleMoves.append((self.y, self.x + 7))

        if self.x - 7 > -1:
            if type(board.squares[(self.y)][self.x - 7]) is Empty:
                possibleMoves.append((self.y, self.x - 7))

            elif board.squares[self.y][self.x - 7].color != self.color:
                possibleMoves.append((self.y, self.x - 7))

        if self.y + 7 < 8:
            if type(board.squares[(self.y + 7)][self.x]) is Empty:
                possibleMoves.append((self.y + 7, self.x))

            elif board.squares[self.y + 7][self.x].color != self.color:
                possibleMoves.append((self.y + 7, self.x))

        if self.y - 7 > -1:
            if type(board.squares[(self.y - 7)][self.x]) is Empty:
                possibleMoves.append((self.y - 7, self.x))

            elif board.squares[self.y - 7][self.x].color != self.color:
                possibleMoves.append((self.y - 7, self.x))

        if self.y + 1 < 8 and self.x + 1 < 8:
            if type(board.squares[self.y + 1][self.x + 1]) is Empty:
                possibleMoves.append((self.y + 1, self.x + 1))

            elif board.squares[self.y + 1][self.x + 1].color != self.color:
                possibleMoves.append((self.y + 1, self.x + 1))

        if self.y + 2 < 8 and self.x + 2 < 8:
            if type(board.squares[self.y + 2][self.x + 2]) is Empty:
                possibleMoves.append((self.y + 2, self.x + 2))

            elif board.squares[self.y + 2][self.x + 2].color != self.color:
                possibleMoves.append((self.y + 2, self.x + 2))

        if self.y + 3 < 8 and self.x + 3 < 8:
            if type(board.squares[self.y + 3][self.x + 3]) is Empty:
                possibleMoves.append((self.y + 3, self.x + 3))

            elif board.squares[self.y + 3][self.x + 3].color != self.color:
                possibleMoves.append((self.y + 3, self.x + 3))

        if self.y + 4 < 8 and self.x + 4 < 8:
            if type(board.squares[self.y + 4][self.x + 4]) is Empty:
                possibleMoves.append((self.y + 4, self.x + 4))

            elif board.squares[self.y + 4][self.x + 4].color != self.color:
                possibleMoves.append((self.y + 4, self.x + 4))

        if self.y + 5 < 8 and self.x + 5 < 8:
            if type(board.squares[self.y + 5][self.x + 5]) is Empty:
                possibleMoves.append((self.y + 5, self.x + 5))

            elif board.squares[self.y + 5][self.x + 5].color != self.color:
                possibleMoves.append((self.y + 5, self.x + 5))

        if self.y + 6 < 8 and self.x + 6 < 8:
            if type(board.squares[self.y + 6][self.x + 6]) is Empty:
                possibleMoves.append((self.y + 6, self.x + 6))

            elif board.squares[self.y + 6][self.x + 6].color != self.color:
                possibleMoves.append((self.y + 6, self.x + 6))

        if self.y + 7 < 8 and self.x + 7 < 8:
            if type(board.squares[self.y + 7][self.x + 7]) is Empty:
                possibleMoves.append((self.y + 7, self.x + 7))

            elif board.squares[self.y + 7][self.x + 7].color != self.color:
                possibleMoves.append((self.y + 7, self.x + 7))

        if self.y - 1 > -1 and self.x - 1 > -1:
            if type(board.squares[self.y - 1][self.x - 1]) is Empty:
                possibleMoves.append((self.y - 1, self.x - 1))

            elif board.squares[self.y - 1][self.x - 1].color != self.color:
                possibleMoves.append((self.y - 1, self.x - 1))

        if self.y - 2 > -1 and self.x - 2 > -1:
            if type(board.squares[self.y - 2][self.x - 2]) is Empty:
                possibleMoves.append((self.y - 2, self.x - 2))

            elif board.squares[self.y - 2][self.x - 2].color != self.color:
                possibleMoves.append((self.y - 2, self.x - 2))

        if self.y - 3 > -1 and self.x - 3 > -1:
            if type(board.squares[self.y - 3][self.x - 3]) is Empty:
                possibleMoves.append((self.y - 3, self.x - 3))

            elif board.squares[self.y - 3][self.x - 3].color != self.color:
                possibleMoves.append((self.y - 3, self.x - 3))

        if self.y - 4 > -1 and self.x - 4 > -1:
            if type(board.squares[self.y - 4][self.x - 4]) is Empty:
                possibleMoves.append((self.y - 4, self.x - 4))

            elif board.squares[self.y - 4][self.x - 4].color != self.color:
                possibleMoves.append((self.y - 4, self.x - 4))

        if self.y - 5 > -1 and self.x - 5 > -1:
            if type(board.squares[self.y - 5][self.x - 5]) is Empty:
                possibleMoves.append((self.y - 5, self.x - 5))

            elif board.squares[self.y - 5][self.x - 5].color != self.color:
                possibleMoves.append((self.y - 5, self.x - 5))

        if self.y - 6 > -1 and self.x - 6 > -1:
            if type(board.squares[self.y - 6][self.x - 6]) is Empty:
                possibleMoves.append((self.y - 6, self.x - 6))

            elif board.squares[self.y - 6][self.x - 6].color != self.color:
                possibleMoves.append((self.y - 6, self.x - 6))

        if self.y - 7 > -1 and self.x - 7 > -1:
            if type(board.squares[self.y - 7][self.x - 7]) is Empty:
                possibleMoves.append((self.y - 7, self.x - 7))

            elif board.squares[self.y - 7][self.x - 7].color != self.color:
                possibleMoves.append((self.y - 7, self.x - 7))

        if self.y + 1 < 8 and self.x - 1 > -1:
            if type(board.squares[self.y + 1][self.x - 1]) is Empty:
                possibleMoves.append((self.y + 1, self.x - 1))

            elif board.squares[self.y + 1][self.x - 1].color != self.color:
                possibleMoves.append((self.y + 1, self.x - 1))

        if self.y + 2 < 8 and self.x - 2 > -1:
            if type(board.squares[self.y + 2][self.x - 2]) is Empty:
                possibleMoves.append((self.y + 2, self.x - 2))

            elif board.squares[self.y + 2][self.x - 2].color != self.color:
                possibleMoves.append((self.y + 2, self.x - 2))

        if self.y + 3 < 8 and self.x - 3 > -1:
            if type(board.squares[self.y + 3][self.x - 3]) is Empty:
                possibleMoves.append((self.y + 3, self.x - 3))

            elif board.squares[self.y + 3][self.x - 3].color != self.color:
                possibleMoves.append((self.y + 3, self.x - 3))

        if self.y + 4 < 8 and self.x - 4 > -1:
            if type(board.squares[self.y + 4][self.x - 4]) is Empty:
                possibleMoves.append((self.y + 4, self.x - 4))

            elif board.squares[self.y + 4][self.x - 4].color != self.color:
                possibleMoves.append((self.y + 4, self.x - 4))

        if self.y + 5 < 8 and self.x - 5 > -1:
            if type(board.squares[self.y + 5][self.x - 5]) is Empty:
                possibleMoves.append((self.y + 5, self.x - 5))

            elif board.squares[self.y + 5][self.x - 5].color != self.color:
                possibleMoves.append((self.y + 5, self.x - 5))

        if self.y + 6 < 8 and self.x - 6 > -1:
            if type(board.squares[self.y + 6][self.x - 6]) is Empty:
                possibleMoves.append((self.y + 6, self.x - 6))

            elif board.squares[self.y + 6][self.x - 6].color != self.color:
                possibleMoves.append((self.y + 6, self.x - 6))

        if self.y + 7 < 8 and self.x - 7 > -1:
            if type(board.squares[self.y + 7][self.x - 7]) is Empty:
                possibleMoves.append((self.y + 7, self.x - 7))

            elif board.squares[self.y + 7][self.x - 7].color != self.color:
                possibleMoves.append((self.y + 7, self.x - 7))

        if self.y - 1 > -1 and self.x + 1 < 8:
            if type(board.squares[self.y - 1][self.x + 1]) is Empty:
                possibleMoves.append((self.y - 1, self.x + 1))

            elif board.squares[self.y - 1][self.x + 1].color != self.color:
                possibleMoves.append((self.y - 1, self.x + 1))

        if self.y - 2 > -1 and self.x + 2 < 8:
            if type(board.squares[self.y - 2][self.x + 2]) is Empty:
                possibleMoves.append((self.y - 2, self.x + 2))

            elif board.squares[self.y - 2][self.x + 2].color != self.color:
                possibleMoves.append((self.y - 2, self.x + 2))

        if self.y - 3 > -1 and self.x + 3 < 8:
            if type(board.squares[self.y - 3][self.x + 3]) is Empty:
                possibleMoves.append((self.y - 3, self.x + 3))

            elif board.squares[self.y - 3][self.x + 3].color != self.color:
                possibleMoves.append((self.y - 3, self.x + 3))

        if self.y - 4 > -1 and self.x + 4 < 8:
            if type(board.squares[self.y - 4][self.x + 4]) is Empty:
                possibleMoves.append((self.y - 4, self.x + 4))

            elif board.squares[self.y - 4][self.x + 4].color != self.color:
                possibleMoves.append((self.y - 4, self.x + 4))

        if self.y - 5 > -1 and self.x + 5 < 8:
            if type(board.squares[self.y - 5][self.x + 5]) is Empty:
                possibleMoves.append((self.y - 5, self.x + 5))

            elif board.squares[self.y - 5][self.x + 5].color != self.color:
                possibleMoves.append((self.y - 5, self.x + 5))

        if self.y - 6 > -1 and self.x + 6 < 8:
            if type(board.squares[self.y - 6][self.x + 6]) is Empty:
                possibleMoves.append((self.y - 6, self.x + 6))

            elif board.squares[self.y - 6][self.x + 6].color != self.color:
                possibleMoves.append((self.y - 6, self.x + 6))

        if self.y - 7 > -1 and self.x + 7 < 8:
            if type(board.squares[self.y - 7][self.x + 7]) is Empty:
                possibleMoves.append((self.y - 7, self.x + 7))

            elif board.squares[self.y - 7][self.x + 7].color != self.color:
                possibleMoves.append((self.y - 7, self.x + 7))

        return possibleMoves


class Knight(Piece):
    def __init__(self, color, pos):
        super().__init__("N", color, pos)

    def get_possible_moves(self, board):
        possibleMoves = []

        if self.y + 1 < 8 and self.x + 2 < 8:
            if type(board.squares[self.y + 1][self.x + 2]) is Empty:
                possibleMoves.append((self.y + 1, self.x + 2))

            elif board.squares[self.y + 1][self.x + 2].color != self.color:
                possibleMoves.append((self.y + 1, self.x + 2))

        if self.y + 2 < 8 and self.x + 1 < 8:
            if type(board.squares[self.y + 2][self.x + 1]) is Empty:
                possibleMoves.append((self.y + 2, self.x + 1))

            elif board.squares[self.y + 2][self.x + 1].color != self.color:
                possibleMoves.append((self.y + 2, self.x + 1))

        if self.y - 1 > -1 and self.x - 2 > -1:
            if type(board.squares[self.y - 1][self.x - 2]) is Empty:
                possibleMoves.append((self.y - 1, self.x - 2))

            elif board.squares[self.y - 1][self.x - 2].color != self.color:
                possibleMoves.append((self.y - 1, self.x - 2))

        if self.y - 2 > -1 and self.x - 1 > -1:
            if type(board.squares[self.y - 2][self.x - 1]) is Empty:
                possibleMoves.append((self.y - 2, self.x - 1))

            elif board.squares[self.y - 2][self.x - 1].color != self.color:
                possibleMoves.append((self.y - 2, self.x - 1))

        if self.y - 1 > -1 and self.x + 2 < 8:
            if type(board.squares[self.y - 1][self.x + 2]) is Empty:
                possibleMoves.append((self.y - 1, self.x + 2))

            elif board.squares[self.y - 1][self.x + 2].color != self.color:
                possibleMoves.append((self.y - 1, self.x + 2))

        if self.y - 2 > -1 and self.x + 1 < 8:
            if type(board.squares[self.y - 2][self.x + 1]) is Empty:
                possibleMoves.append((self.y - 2, self.x + 1))

            elif board.squares[self.y - 2][self.x + 1].color != self.color:
                possibleMoves.append((self.y - 2, self.x + 1))

        if self.y + 1 < 8 and self.x - 2 > -1:
            if type(board.squares[self.y + 1][self.x - 2]) is Empty:
                possibleMoves.append((self.y + 1, self.x - 2))

            elif board.squares[self.y + 1][self.x - 2].color != self.color:
                possibleMoves.append((self.y + 1, self.x - 2))

        if self.y + 2 < 8 and self.x - 1 > -1:
            if type(board.squares[self.y + 2][self.x - 1]) is Empty:
                possibleMoves.append((self.y + 2, self.x - 1))

            elif board.squares[self.y + 2][self.x - 1].color != self.color:
                possibleMoves.append((self.y + 2, self.x - 1))

        return possibleMoves


class Bishop(Piece):
    def __init__(self, color, pos):
        super().__init__("B", color, pos)

    def get_possible_moves(self, board):
        possibleMoves = []

        if self.y + 1 < 8 and self.x + 1 < 8:
            if type(board.squares[self.y + 1][self.x + 1]) is Empty:
                possibleMoves.append((self.y + 1, self.x + 1))

            elif board.squares[self.y + 1][self.x + 1].color != self.color:
                possibleMoves.append((self.y + 1, self.x + 1))

        if self.y + 2 < 8 and self.x + 2 < 8:
            if type(board.squares[self.y + 2][self.x + 2]) is Empty:
                possibleMoves.append((self.y + 2, self.x + 2))

            elif board.squares[self.y + 2][self.x + 2].color != self.color:
                possibleMoves.append((self.y + 2, self.x + 2))

        if self.y + 3 < 8 and self.x + 3 < 8:
            if type(board.squares[self.y + 3][self.x + 3]) is Empty:
                possibleMoves.append((self.y + 3, self.x + 3))

            elif board.squares[self.y + 3][self.x + 3].color != self.color:
                possibleMoves.append((self.y + 3, self.x + 3))

        if self.y + 4 < 8 and self.x + 4 < 8:
            if type(board.squares[self.y + 4][self.x + 4]) is Empty:
                possibleMoves.append((self.y + 4, self.x + 4))

            elif board.squares[self.y + 4][self.x + 4].color != self.color:
                possibleMoves.append((self.y + 4, self.x + 4))

        if self.y + 5 < 8 and self.x + 5 < 8:
            if type(board.squares[self.y + 5][self.x + 5]) is Empty:
                possibleMoves.append((self.y + 5, self.x + 5))

            elif board.squares[self.y + 5][self.x + 5].color != self.color:
                possibleMoves.append((self.y + 5, self.x + 5))

        if self.y + 6 < 8 and self.x + 6 < 8:
            if type(board.squares[self.y + 6][self.x + 6]) is Empty:
                possibleMoves.append((self.y + 6, self.x + 6))

            elif board.squares[self.y + 6][self.x + 6].color != self.color:
                possibleMoves.append((self.y + 6, self.x + 6))

        if self.y + 7 < 8 and self.x + 7 < 8:
            if type(board.squares[self.y + 7][self.x + 7]) is Empty:
                possibleMoves.append((self.y + 7, self.x + 7))

            elif board.squares[self.y + 7][self.x + 7].color != self.color:
                possibleMoves.append((self.y + 7, self.x + 7))

        if self.y - 1 > -1 and self.x - 1 > -1:
            if type(board.squares[self.y - 1][self.x - 1]) is Empty:
                possibleMoves.append((self.y - 1, self.x - 1))

            elif board.squares[self.y - 1][self.x - 1].color != self.color:
                possibleMoves.append((self.y - 1, self.x - 1))

        if self.y - 2 > -1 and self.x - 2 > -1:
            if type(board.squares[self.y - 2][self.x - 2]) is Empty:
                possibleMoves.append((self.y - 2, self.x - 2))

            elif board.squares[self.y - 2][self.x - 2].color != self.color:
                possibleMoves.append((self.y - 2, self.x - 2))

        if self.y - 3 > -1 and self.x - 3 > -1:
            if type(board.squares[self.y - 3][self.x - 3]) is Empty:
                possibleMoves.append((self.y - 3, self.x - 3))

            elif board.squares[self.y - 3][self.x - 3].color != self.color:
                possibleMoves.append((self.y - 3, self.x - 3))

        if self.y - 4 > -1 and self.x - 4 > -1:
            if type(board.squares[self.y - 4][self.x - 4]) is Empty:
                possibleMoves.append((self.y - 4, self.x - 4))

            elif board.squares[self.y - 4][self.x - 4].color != self.color:
                possibleMoves.append((self.y - 4, self.x - 4))

        if self.y - 5 > -1 and self.x - 5 > -1:
            if type(board.squares[self.y - 5][self.x - 5]) is Empty:
                possibleMoves.append((self.y - 5, self.x - 5))

            elif board.squares[self.y - 5][self.x - 5].color != self.color:
                possibleMoves.append((self.y - 5, self.x - 5))

        if self.y - 6 > -1 and self.x - 6 > -1:
            if type(board.squares[self.y - 6][self.x - 6]) is Empty:
                possibleMoves.append((self.y - 6, self.x - 6))

            elif board.squares[self.y - 6][self.x - 6].color != self.color:
                possibleMoves.append((self.y - 6, self.x - 6))

        if self.y - 7 > -1 and self.x - 7 > -1:
            if type(board.squares[self.y - 7][self.x - 7]) is Empty:
                possibleMoves.append((self.y - 7, self.x - 7))

            elif board.squares[self.y - 7][self.x - 7].color != self.color:
                possibleMoves.append((self.y - 7, self.x - 7))

        if self.y + 1 < 8 and self.x - 1 > -1:
            if type(board.squares[self.y + 1][self.x - 1]) is Empty:
                possibleMoves.append((self.y + 1, self.x - 1))

            elif board.squares[self.y + 1][self.x - 1].color != self.color:
                possibleMoves.append((self.y + 1, self.x - 1))

        if self.y + 2 < 8 and self.x - 2 > -1:
            if type(board.squares[self.y + 2][self.x - 2]) is Empty:
                possibleMoves.append((self.y + 2, self.x - 2))

            elif board.squares[self.y + 2][self.x - 2].color != self.color:
                possibleMoves.append((self.y + 2, self.x - 2))

        if self.y + 3 < 8 and self.x - 3 > -1:
            if type(board.squares[self.y + 3][self.x - 3]) is Empty:
                possibleMoves.append((self.y + 3, self.x - 3))

            elif board.squares[self.y + 3][self.x - 3].color != self.color:
                possibleMoves.append((self.y + 3, self.x - 3))

        if self.y + 4 < 8 and self.x - 4 > -1:
            if type(board.squares[self.y + 4][self.x - 4]) is Empty:
                possibleMoves.append((self.y + 4, self.x - 4))

            elif board.squares[self.y + 4][self.x - 4].color != self.color:
                possibleMoves.append((self.y + 4, self.x - 4))

        if self.y + 5 < 8 and self.x - 5 > -1:
            if type(board.squares[self.y + 5][self.x - 5]) is Empty:
                possibleMoves.append((self.y + 5, self.x - 5))

            elif board.squares[self.y + 5][self.x - 5].color != self.color:
                possibleMoves.append((self.y + 5, self.x - 5))

        if self.y + 6 < 8 and self.x - 6 > -1:
            if type(board.squares[self.y + 6][self.x - 6]) is Empty:
                possibleMoves.append((self.y + 6, self.x - 6))

            elif board.squares[self.y + 6][self.x - 6].color != self.color:
                possibleMoves.append((self.y + 6, self.x - 6))

        if self.y + 7 < 8 and self.x - 7 > -1:
            if type(board.squares[self.y + 7][self.x - 7]) is Empty:
                possibleMoves.append((self.y + 7, self.x - 7))

            elif board.squares[self.y + 7][self.x - 7].color != self.color:
                possibleMoves.append((self.y + 7, self.x - 7))

        if self.y - 1 > -1 and self.x + 1 < 8:
            if type(board.squares[self.y - 1][self.x + 1]) is Empty:
                possibleMoves.append((self.y - 1, self.x + 1))

            elif board.squares[self.y - 1][self.x + 1].color != self.color:
                possibleMoves.append((self.y - 1, self.x + 1))

        if self.y - 2 > -1 and self.x + 2 < 8:
            if type(board.squares[self.y - 2][self.x + 2]) is Empty:
                possibleMoves.append((self.y - 2, self.x + 2))

            elif board.squares[self.y - 2][self.x + 2].color != self.color:
                possibleMoves.append((self.y - 2, self.x + 2))

        if self.y - 3 > -1 and self.x + 3 < 8:
            if type(board.squares[self.y - 3][self.x + 3]) is Empty:
                possibleMoves.append((self.y - 3, self.x + 3))

            elif board.squares[self.y - 3][self.x + 3].color != self.color:
                possibleMoves.append((self.y - 3, self.x + 3))

        if self.y - 4 > -1 and self.x + 4 < 8:
            if type(board.squares[self.y - 4][self.x + 4]) is Empty:
                possibleMoves.append((self.y - 4, self.x + 4))

            elif board.squares[self.y - 4][self.x + 4].color != self.color:
                possibleMoves.append((self.y - 4, self.x + 4))

        if self.y - 5 > -1 and self.x + 5 < 8:
            if type(board.squares[self.y - 5][self.x + 5]) is Empty:
                possibleMoves.append((self.y - 5, self.x + 5))

            elif board.squares[self.y - 5][self.x + 5].color != self.color:
                possibleMoves.append((self.y - 5, self.x + 5))

        if self.y - 6 > -1 and self.x + 6 < 8:
            if type(board.squares[self.y - 6][self.x + 6]) is Empty:
                possibleMoves.append((self.y - 6, self.x + 6))

            elif board.squares[self.y - 6][self.x + 6].color != self.color:
                possibleMoves.append((self.y - 6, self.x + 6))

        if self.y - 7 > -1 and self.x + 7 < 8:
            if type(board.squares[self.y - 7][self.x + 7]) is Empty:
                possibleMoves.append((self.y - 7, self.x + 7))

            elif board.squares[self.y - 7][self.x + 7].color != self.color:
                possibleMoves.append((self.y - 7, self.x + 7))

        return possibleMoves


class King(Piece):
    def __init__(self, color, pos):
        super().__init__("K", color, pos)

    def get_possible_moves(self, board):
        possibleMoves = []

        if self.y + 1 < 8:
            if type(board.squares[(self.y + 1)][(self.x)]) is Empty:
                possibleMoves.append((self.y + 1, self.x))

            elif board.squares[self.y + 1][self.x].color != self.color:
                possibleMoves.append((self.y + 1, self.x))

        if self.y - 1 > -1:
            if type(board.squares[(self.y - 1)][self.x]) is Empty:
                possibleMoves.append((self.y - 1, self.x))

            elif board.squares[self.y - 1][self.x].color != self.color:
                possibleMoves.append((self.y - 1, self.x))

        if self.x + 1 < 8:
            if type(board.squares[(self.y)][self.x + 1]) is Empty:
                possibleMoves.append((self.y, self.x + 1))

            elif board.squares[self.y][self.x + 1].color != self.color:
                possibleMoves.append((self.y, self.x + 1))

        if self.x - 1 > -1:
            if type(board.squares[(self.y)][self.x - 1]) is Empty:
                possibleMoves.append((self.y, self.x - 1))

            elif board.squares[self.y][self.x - 1].color != self.color:
                possibleMoves.append((self.y, self.x - 1))

        return possibleMoves


class Board:
    def __init__(self):
        self.squares: list[list[Piece | None]] = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

    def CoordToAlgebraic(self, y, x):
        return chr(ord("1") + (7 - x)) + chr(ord("a") + y)

    def AddPiece(self, piece):
        self.squares[piece.x][piece.y] = piece

    def set_new_board(self):
        for y in range(0, 8):
            for x in range(0, 8):
                if self.squares[y][x] == None:
                    pos = self.CoordToAlgebraic(y, x)
                    self.squares[y][x] = Empty(pos)

        self.squares[0][0] = Rook("b", "8a")
        self.squares[0][1] = Knight("b", "8b")
        self.squares[0][2] = Bishop("b", "8c")
        self.squares[0][3] = Queen("b", "8d")
        self.squares[0][4] = King("b", "8e")
        self.squares[0][5] = Bishop("b", "8f")
        self.squares[0][6] = Knight("b", "8g")
        self.squares[0][7] = Rook("b", "8h")
        self.squares[1][0] = Pawn("b", "7a")
        self.squares[1][1] = Pawn("b", "7b")
        self.squares[1][2] = Pawn("b", "7c")
        self.squares[1][3] = Pawn("b", "7d")
        self.squares[1][4] = Pawn("b", "7e")
        self.squares[1][5] = Pawn("b", "7f")
        self.squares[1][6] = Pawn("b", "7g")
        self.squares[1][7] = Pawn("b", "7h")
        self.squares[6][0] = Pawn("w", "2a")
        self.squares[6][1] = Pawn("w", "2b")
        self.squares[6][2] = Pawn("w", "2c")
        self.squares[6][3] = Pawn("w", "2d")
        self.squares[6][4] = Pawn("w", "2e")
        self.squares[6][5] = Pawn("w", "2f")
        self.squares[6][6] = Pawn("w", "2g")
        self.squares[6][7] = Pawn("w", "2h")
        self.squares[7][0] = Rook("w", "1a")
        self.squares[7][1] = Knight("w", "1b")
        self.squares[7][2] = Bishop("w", "1c")
        self.squares[7][3] = Queen("w", "1d")
        self.squares[7][4] = King("w", "1e")
        self.squares[7][5] = Bishop("w", "1f")
        self.squares[7][6] = Knight("w", "1g")
        self.squares[7][7] = Rook("w", "1h")

    def print_position(self):
        for y in range(0, 8):
            line = str(8 - y) + " "
            for x in range(0, 8):
                if self.squares[y][x] is not None:
                    if type(self.squares[y][x]) is Empty:
                        line += "   "
                    else:
                        figuur = self.squares[y][x]
                        naam = figuur.name
                        color = figuur.color
                        line += naam + color + " "
            print(line)
        print("  a  b  c  d  e  f  g  h")
