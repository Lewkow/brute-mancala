import begin
import random


class Board:
    
    def __init__(self):
        self.global_pockets = {x: 0 for x in list(range(14))}
        self.player1_pockets_i = list(range(0, 6))
        self.player2_pockets_i = list(range(7, 13))
        self.player1_barn_i = 6
        self.player2_barn_i = 13
        for x in self.player1_pockets_i + self.player2_pockets_i:
            self.global_pockets[x] = 4

    def print_board(self):
        print(
            f"  | {self.global_pockets[12]} | {self.global_pockets[11]}" \
            f" | {self.global_pockets[10]} | {self.global_pockets[9]}" \
            f" | {self.global_pockets[8]} | {self.global_pockets[7]} |  "
            )
        print(
            f"{self.global_pockets[self.player2_barn_i]} ------------------------- " \
            f"{self.global_pockets[self.player1_barn_i]}"
            )
        print(
            f"  | {self.global_pockets[0]} | {self.global_pockets[1]}" \
            f" | {self.global_pockets[2]} | {self.global_pockets[3]}" \
            f" | {self.global_pockets[4]} | {self.global_pockets[5]} |  "
            )
        print("\n")
        
    def other_player(self, player_number):
        if player_number == 0:
            return 1
        else:
            return 0

    def execute_move(self, player_number, pocket):
        global_pocket_i = pocket
        current_value = self.global_pockets[global_pocket_i]
        if current_value > 0:
            self.global_pockets[global_pocket_i] = 0
            while current_value > 0:
                if global_pocket_i + 1 > (len(self.global_pockets) - 1):
                    self.global_pockets[0] += 1
                else:
                    self.global_pockets[global_pocket_i + 1] += 1
                current_value -= 1
                global_pocket_i += 1
        else:
            print(f"unable to make move on pocket with {self.player_pockets[player_number][pocket]} value")
        
    def finish_board(self):
        tot_player1_remaining = sum([self.global_pockets[x] for x in self.player1_pockets_i])
        tot_player2_remaining = sum([self.global_pockets[x] for x in self.player2_pockets_i])
        self.global_pockets[self.player1_barn_i] += tot_player1_remaining
        self.global_pockets[self.player2_barn_i] += tot_player2_remaining
        for x in self.player1_pockets_i:
            self.global_pockets[x] = 0
            
        for x in self.player2_pockets_i:
            self.global_pockets[x] = 0

class Player:
    
    def __init__(self, player_number):
        self.player_number = player_number
        
    def possible_pockets(self, board):
        player_indices = board.player1_pockets_i if self.player_number == 0 else board.player2_pockets_i
        player_pockets = [board.global_pockets[x] for x in player_indices]
        return [x for x in player_indices if board.global_pockets[x] > 0]
        
    def has_a_move(self, board):
        possible_pockets = self.possible_pockets(board)
        return True if len(possible_pockets) > 0 else False
    
    def make_move(self, board):
        possible_pockets = self.possible_pockets(board)
        # print(f"player {self.player_number} pockets {possible_pockets}")
        # print(f"board before: \n")
        # board.print_board()
        board.execute_move(self.player_number, random.choice(possible_pockets))
        # print(f"board after: \n")
        board.print_board()

    
class Rules:
    
    def __init__(self):
        pass



@begin.start
def run():
    print(f"mancala\n-------\n\n")
    board = Board()
    # board.print_board()
    player1 = Player(0)
    player2 = Player(1)
    play_on = True
    while play_on:
        if player1.has_a_move(board):
            player1.make_move(board)
        else:
            play_on = False
        
        if player2.has_a_move(board):
            player2.make_move(board)
        else:
            play_on = False
    
    board.finish_board()
    board.print_board()
    
