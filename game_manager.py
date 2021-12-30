from random import randint, choice


class GameManager:

    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        self.player_positions = []
        self.computer_positions = []

        self.winning_combos = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        # This will be used for the basic AI
        self.strategy_options = [i for i in range(len(self.winning_combos))]
        self.strategy = choice(self.strategy_options)

        self.player = None
        self.computer = None
        self.players_turn = False
        self.winner = None
        self.tie = False

    def print_board(self):
        print(f' {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} \n'
              f'-----------\n'
              f' {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} \n'
              f'-----------\n'
              f' {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} \n')

    def select_character(self):
        selected = False
        while not selected:
            player_choice = input('Will you be X or O? (X goes first): ').upper().strip()
            if player_choice == 'X':
                self.player = 'X'
                self.computer = 'O'
                self.players_turn = True
                selected = True
            elif player_choice == 'O':
                self.player = 'O'
                self.computer = 'X'
                selected = True
            else:
                print('Sorry, that was not a valid entry.')

    def player_move(self):
        move_in_progress = True
        while move_in_progress:

            row_input = input("Enter row for your move (0-2): ")
            col_input = input("Enter column for your move (0-2): ")

            if not row_input.isdigit() or not col_input.isdigit():
                print('Sorry, that is not a valid entry.')
                continue

            row = int(row_input)
            column = int(col_input)

            if row < 0 or row > 2 or column < 0 or column > 2:
                print('Sorry, that is not a valid entry.')
                continue

            position = (row, column)
            if position in self.player_positions or position in self.computer_positions:
                print('Sorry, that space is already taken on the board.')
                continue

            self.player_positions.append(position)
            self.board[row][column] = self.player
            move_in_progress = False

    def select_new_strategy(self):
        self.strategy_options.remove(self.strategy)
        self.strategy = choice(self.strategy_options)

    def strategy_still_valid(self):
        for position in self.winning_combos[self.strategy]:
            if position in self.player_positions:
                return False
        return True

    def computer_move(self):
        move_in_progress = True
        while move_in_progress:
            if not self.strategy_still_valid():
                self.select_new_strategy()
                continue
            position = choice(self.winning_combos[self.strategy])
            if position in self.computer_positions:
                continue

            self.computer_positions.append(position)
            print(f"Computer moves to ({position[0]}, {position[1]})")
            self.board[position[0]][position[1]] = self.computer
            move_in_progress = False

    def check_score(self):
        for combo in self.winning_combos:
            if all(position in self.player_positions for position in combo):
                self.winner = 'Player'
                return
            if all(position in self.computer_positions for position in combo):
                self.winner = 'Computer'
                return
        if len(self.player_positions) + len(self.computer_positions) == 9:
            self.tie = True

    def play_game(self):
        self.select_character()
        game_in_progress = True
        while game_in_progress:
            if self.players_turn:
                self.player_move()
                self.players_turn = False
            else:
                self.computer_move()
                self.players_turn = True
            self.print_board()
            self.check_score()
            if self.winner:
                print(f"{self.winner} wins!")
                game_in_progress = False
            elif self.tie:
                print("It's a tie!")
                game_in_progress = False
