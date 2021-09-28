class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def get_board(self):
        return self.board

    def print_board(self):
        print(self.board[0][0] + " | " + self.board[0]
              [1] + " | " + self.board[0][2])
        print(self.board[1][0] + " | " + self.board[1]
              [1] + " | " + self.board[1][2])
        print(self.board[2][0] + " | " + self.board[2]
              [1] + " | " + self.board[2][2])

    def set_new_mark(self, mark, pos):
        if pos < 10 and pos > 0:
            if self.board[(pos - 1)//3][(pos - 1) % 3] == " ":
                self.board[(pos - 1)//3][(pos - 1) % 3] = mark
                return True
            else:
                print("This position is taken, choose another postion")
                return False
        else:
            print('not a valid position')
            return False

    def check_col_win(self, col_num):
        if self.board[col_num][0] != ' ' and self.board[col_num][0] == self.board[col_num][1] and self.board[col_num][0] == self.board[col_num][2]:
            return True
        else:
            return False

    def check_row_win(self, row_num):
        if self.board[0][row_num] != ' ' and self.board[0][row_num] == self.board[1][row_num] and self.board[0][row_num] == self.board[2][row_num]:
            return True
        else:
            return False

    def check_diagonal_win(self):
        return (self.board[0][0] != " " and self.board[1][1] == self.board[0][0] and self.board[2][2] == self.board[0][0]) or (self.board[0][2] != " " and self.board[1][1] == self.board[0][2] and self.board[2][0] == self.board[0][2])

    def check_win(self):
        if self.check_col_win(0) or self.check_col_win(1) or self.check_col_win(2) or self.check_row_win(0) or self.check_row_win(1) or self.check_row_win(2) or self.check_diagonal_win():
            return True
        else:
            return False


class Game:
    def __init__(self):
        self.board = Board()
        self.turns = 0
        self.is_over = False

    def get_board(self):
        return self.board

    def get_turns(self):
        return self.turns

    def set_turns(self, val):
        self.turns = val

    def anounce_winner(self, player):
        print("and the winner is player " + player)

    def start_game(self):
        print("Instructions: you will be playing in turns, x goes first, o goes second.")
        print("Your goal is to put 3 marks in a row on the board before the other player does so.")
        print("choose a number between 1 and 9 to put a mark on the board. good luck!")
        print("")
        self.board.print_board()
        print("")

        while self.is_over == False or self.turns > 9:

            self.turns = self.turns + 1
            approved_pos = False

            while approved_pos == False:
                pos = input("player x, choose a position ")
                approved_pos = self.board.set_new_mark("x", int(pos))

            self.board.print_board()
            print("")

            if self.board.check_win() == True:
                self.anounce_winner('x')
                self.is_over = True

            elif self.turns == 9:
                print("game is tied!")
                self.is_over = True
            else:
                self.turns = self.turns + 1
                approved_pos = False

                while approved_pos == False:
                    pos = input("player o, choose a position ")
                    approved_pos = self.board.set_new_mark("o", int(pos))

                self.board.print_board()
                print("")

                if self.board.check_win() == True:
                    self.anounce_winner('o')
                    self.is_over = True


g = Game()
g.start_game()
