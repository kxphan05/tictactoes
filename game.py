import numpy as np

class TicTacToe():
    def __init__(self, N):
        self.N = N
        self.board_state = np.arange(1, N ** 2 + 1).reshape(N,N).astype(object)
        self.players = ['O','X']
    
    def generate_row(self, rw_ix):
        for i in range(self.N):
            val = self.board_state[rw_ix, i]
            if i != (self.N - 1) :
                print(f" {val} ", end='|')
            else:
                print(f" {val} ")
    
    def generate_board(self):
        print()
        for i in range(self.N):
            self.generate_row(i)
            print('-' * (self.N * 4 - 1)) if i != (self.N - 1) else print()
    
    def check_win(self):
        winning_arrays = []
        #check diags
        winning_arrays.append(self.board_state.diagonal().tolist())
        winning_arrays.append(np.fliplr(self.board_state).diagonal().tolist())
        for i in range(self.N):
            #check cols
            winning_arrays.append(self.board_state[:, i].tolist())
            #check rows
            winning_arrays.append(self.board_state[i, :].tolist())
        for i in self.players:
            for j in winning_arrays:
                if j == ([i] * (self.N)):
                    return i
        if set(self.board_state.reshape(-1).tolist()) == set(self.players):
            return 1
        else: return 0
    
    def init_game(self):
        while True:
            while True:
                #player 1's turn
                try:
                    pos = input("Player 1's Turn: ")
                    if pos == 'q':
                        print('Player 2 wins!')
                        return
                    pos = int(pos) - 1
                    #check if space is filled:
                    coord = pos//self.N, pos%self.N
                    if self.board_state[coord] in self.players:
                        print("invalid input, try again!")
                        continue
                    else:
                        self.board_state[coord] = self.players[0]
                        break
                except ValueError:
                    print('Enter a valid number!')
                    continue
                except IndexError:
                    print('Enter valid index!')
            
            self.generate_board()

            if self.check_win() == self.players[0]:
                print("Player 1 wins!")
                return
            elif self.check_win() == 1:
                print("DRAW!")
                return
            
            #Player 2's turn
            while True:
                #player 1's turn
                try:
                    pos = input("Player 2's Turn: ")
                    if pos == 'q':
                        print('Player 1 wins!')
                        return
                    pos = int(pos) - 1
                    #check if space is filled:
                    coord = pos//self.N, pos%self.N
                    if self.board_state[coord] in self.players:
                        print("invalid input, try again!")
                        continue
                    else:
                        self.board_state[coord] = self.players[1]
                        break
                except ValueError:
                    print('Enter a valid number!')
                    continue
                except IndexError:
                    print('Enter valid index!')
            
            self.generate_board()

            if self.check_win() == self.players[1]:
                print("Player 2 wins!")
                return
            elif self.check_win() == 1:
                print("DRAW!")
                return
            
def main():
    try:
        n = int(input("Board Size: "))
    except ValueError:
        print('Enter Valid Board Size')
    tictactoe = TicTacToe(n)
    tictactoe.generate_board()
    tictactoe.init_game()

if __name__ == '__main__':
    main()


