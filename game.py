import numpy as np

class TicTacToe():
    def __init__(self, N):
        self.N = N
        self.board_state = np.arange(1, N ** 2 + 1).reshape(N,N)
        self.game_state = 0
        self.players = ['O','X']
    
    def generate_row(self, rw_ix):
        for i in range(self.N):
            val = self.board_state[rw_ix, i]
            if i != (self.N - 1) :
                print(f" {val} ", end='|')
            else:
                print(f" {val} ")
    
    def generate_board(self):
        for i in range(self.N):
            self.generate_row(i)
            print('-' * (self.N * 4 - 1)) if i != (self.N - 1) else print()
    
    def check_win(self):
        winning_arrays = np.array()

        #check diags
        winning_arrays.append(self.board_state.diagonal())
        winning_arrays.append(np.fliplr(self.board_state).diagonal())
        for i in range(self.N):
            #check cols
            winning_arrays.append(self.board_state[:, i])
            #check rows
            winning_arrays.append(self.board_state[i, :])
        winner = np.where(len(winning_arrays.unique()) == 1)
        if len(winner) != 0: return winner[0][0]
        else: return 0
    

tictactoe = TicTacToe(3)
tictactoe.generate_board()


