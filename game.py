class TicTacToe():
    def __init__(self, N):
        self.N = N
        self.board_state = [i for i in range(1, N ** 2 + 1)]
        self.game_state = 0
        self.players = ['O','X']
    
    def generate_row(self, rw_ix):
        for i in range(self.N):
            val = self.board_state[rw_ix * self.N + i]
            if i != (self.N - 1) :
                print(f" {val} ", end='|')
            else:
                print(f" {val} ")
    
    def generate_board(self):
        for i in range(self.N):
            self.generate_row(i)
            print('-' * (self.N * 4 - 1)) if i != (self.N - 1) else print()
    
    def check_win(self):
        #check diags
        for i in range(self.N):
            if self.board_state

tictactoe = TicTacToe(3)
tictactoe.generate_board()


