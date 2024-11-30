from ClassObjects import Board
from ClassObjects import Empty
from ClassObjects import Pawn
from ClassObjects import Knight
from ClassObjects import Bishop
from ClassObjects import Rook
from ClassObjects import Queen
from ClassObjects import King


def get_class(user_input):
    if len(user_input) == 2 or user_input.isalpha():
        return Pawn
    if user_input[0] == "N":
        return Knight
    if user_input[0] == "B":
        return Bishop
    if user_input[0] == "R":
        return Rook
    if user_input[0] == "Q":
        return Queen
    if user_input[0] == "K":
        return King


def slice_input(user_input, piece_type):
    if piece_type == Pawn:
        if len(user_input) == 2:
            return user_input
        elif len(user_input) == 3:
            pass
    if piece_type != Pawn and len(user_input) == 3:
        return user_input[1] + user_input[2]
    if piece_type != Pawn and len(user_input) == 4:
        return user_input[2] + user_input[3]
    raise Exception("zeekoe")


def get_piece(position, piece_type, move_numeric, turn):
    for y in position.squares:
        for x in y:
            if isinstance(x, piece_type) and x.color == turn:
                for tupl in x.get_possible_moves(position):
                    if str(tupl[0]) + str(tupl[1]) == move_numeric:
                        return x


def move_piece(position, move_numeric):
    position.squares[int(move_numeric[0])][int(move_numeric[1])] = piece


def place_empty(position, position_piece, piece):
    position.squares[int(position_piece[0])][(int(position_piece[1]))] = Empty(
        piece.pos
    )


game_over = False
turn_couter = 0
position = Board()
position.set_new_board()

while not game_over:
    turn = "w" if turn_couter % 2 == 0 else "b"
    user_input = input("please type in a chess notation ")
    piece_type = get_class(user_input)
    move_algebraic = slice_input(user_input, piece_type)[::-1]
    move_numeric = str(Empty(move_algebraic).y) + str(Empty(move_algebraic).x)
    piece = get_piece(position, piece_type, move_numeric, turn)
    position_piece = str(piece.y) + str(piece.x)
    move_piece(position, move_numeric)
    place_empty(position, position_piece, piece)
    piece.pos = move_algebraic
    piece.y = int(move_numeric[0])
    piece.x = int(move_numeric[1])
    turn_couter += 1
    position.print_position()
