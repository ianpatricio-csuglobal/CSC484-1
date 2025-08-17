"""
Module: Tic-Tac-Toe with NumPy (OOP Version)
Description: This module implements a 2-player Tic-Tac-Toe game using NumPy,
             object-oriented programming, inheritance, polymorphism, and
             operator overloading. It supports both human and AI players.
Author: Ian Patricio
Version: 1.0.0
"""

import numpy as np
import random


class Player:
    def __init__(self, symbol):
        self.symbol = symbol  # "X" or "O"

    def make_move(self, board):
        """Abstract method: implemented by subclasses"""
        raise NotImplementedError("Subclasses must override this method")


class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                row = int(input(f"Player {self.symbol}, enter row (0-2): "))
                col = int(input(f"Player {self.symbol}, enter col (0-2): "))

                if board[row, col] == " ":
                    board[row, col] = self.symbol
                    break
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter numbers between 0 and 2.")


class AIPlayer(Player):
    def make_move(self, board):
        print(f"AI {self.symbol} is making a move...")
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r, c] == " "]
        row, col = random.choice(empty_cells)
        board[row, col] = self.symbol


class TicTacToeBoard:
    def __init__(self):
        self.grid = np.full((3, 3), " ")

    # Operator overloading for indexing
    def __getitem__(self, index):
        return self.grid[index]

    def __setitem__(self, index, value):
        self.grid[index] = value

    def __str__(self):
        rows = []
        for row in self.grid:
            rows.append(" | ".join(row))
            rows.append("-" * 9)
        return "\n".join(rows)

    def is_full(self):
        return np.all(self.grid != " ")

    def check_winner(self, symbol):
        # Check rows & columns
        for i in range(3):
            if np.all(self.grid[i, :] == symbol) or np.all(self.grid[:, i] == symbol):
                return True
        # Check diagonals
        if np.all(np.diag(self.grid) == symbol) or np.all(np.diag(np.fliplr(self.grid)) == symbol):
            return True
        return False


class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = TicTacToeBoard()
        self.players = [player1, player2]

    def play(self):
        turn = 0
        while True:
            print(self.board)
            current_player = self.players[turn % 2]
            current_player.make_move(self.board)

            if self.board.check_winner(current_player.symbol):
                print(self.board)
                print(f"Player {current_player.symbol} wins!")
                break
            if self.board.is_full():
                print(self.board)
                print("It's a draw!")
                break

            turn += 1


# Run the game
if __name__ == "__main__":
    player1 = HumanPlayer("X")
    # You can choose HumanPlayer("O") or AIPlayer("O") for polymorphism demo
    player2 = AIPlayer("O")
    game = TicTacToeGame(player1, player2)
    game.play()
