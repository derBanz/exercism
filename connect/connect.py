"""
Set task: Compute the result for a game of Hex / Polygon.
Method:
* On init, the board is translated into a list.
* On get_winner(), we run check() for both "X" and "O" and return the winner
  depending on the results.
* On check(), if the player given is "O", the board is turned so we can
  calculate both players as playing from left to right.
  We start in the first column and look for a match. Once we find one, we look
  for other matches around it. Every match is saved into history (list).
  If a new match is found we look around that one until either all neighbour-
  tiles are checked and negative, in which case we go back a step, or we reach
  the end of the board, in which case the player is deemed the winner.
Example:
* game = ConnectGame(
    '''. O . .
        O X X X
         O X O .
          X X O X
           . O X .'''
  )
  game.get_winner() -> "X"
"""


class ConnectGame:
    def __init__(self, board):
        self.board = [[]]
        for char in board:
            if char == "\n":
                self.board.append([])
            elif char != " ":
                self.board[-1].append(char)

    def check(self, player):
        if player == "X":
            board = self.board
        else:
            board = list()
            for i in range(len(self.board[0])):
                board.append([])
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    board[j].append(self.board[i][j])
        x = 0
        y = 0
        history = list()
        while x < len(board):
            if not len(history):
                if self.check_tile(board, x, y) == player:
                    history.append([x, y, 0])
                else:
                    x += 1
            elif history[-1][1] == len(board[0]) - 1:
                return True
            elif history[-1][2] == 0:
                history[-1][2] = 1
                x_temp = history[-1][0] - 1
                y_temp = history[-1][1] + 1
                if history[-1][0] > 0:
                    if self.check_tile(
                        board,
                        x_temp,
                        y_temp
                    ) == player and not any(
                        x in history for x in [
                            [x_temp, y_temp, o] for o in range(7)
                        ]
                    ):
                        history.append([
                            history[-1][0] - 1,
                            history[-1][1] + 1,
                            0
                        ])
            elif history[-1][2] == 1:
                history[-1][2] = 2
                x_temp = history[-1][0]
                y_temp = history[-1][1] + 1
                if self.check_tile(
                    board,
                    x_temp,
                    y_temp
                ) == player and not any(
                    x in history for x in [
                        [x_temp, y_temp, o] for o in range(7)
                    ]
                ):
                    history.append([
                        history[-1][0],
                        history[-1][1] + 1,
                        0
                    ])
            elif history[-1][2] == 2:
                history[-1][2] = 3
                x_temp = history[-1][0] + 1
                y_temp = history[-1][1]
                if history[-1][0] < len(board) - 1:
                    if self.check_tile(
                        board,
                        x_temp,
                        y_temp
                    ) == player and not any(
                        x in history for x in [
                            [x_temp, y_temp, o] for o in range(7)
                        ]
                    ):
                        history.append([
                            x_temp,
                            y_temp,
                            0
                        ])
            elif history[-1][2] == 3:
                history[-1][2] = 4
                x_temp = history[-1][0] + 1
                y_temp = history[-1][1] - 1
                if history[-1][0] < len(board) - 1 and history[-1][1] > 0:
                    if self.check_tile(
                        board,
                        x_temp,
                        y_temp
                    ) == player and not any(
                        x in history for x in [
                            [x_temp, y_temp, o] for o in range(7)
                        ]
                    ):
                        history.append([
                            x_temp,
                            y_temp,
                            0
                        ])
            elif history[-1][2] == 4:
                history[-1][2] = 5
                x_temp = history[-1][0]
                y_temp = history[-1][1] - 1
                if history[-1][1] > 0:
                    if self.check_tile(
                        board,
                        x_temp,
                        y_temp
                    ) == player and not any(
                        x in history for x in [
                            [x_temp, y_temp, o] for o in range(7)
                        ]
                    ):
                        history.append([
                            x_temp,
                            y_temp,
                            0
                        ])
            elif history[-1][2] == 5:
                history[-1][2] = 6
                x_temp = history[-1][0] - 1
                y_temp = history[-1][1]
                if history[-1][0] > 0:
                    if self.check_tile(
                        board,
                        x_temp,
                        y_temp
                    ) == player and not any(
                        x in history for x in [
                            [x_temp, y_temp, o] for o in range(7)
                        ]
                    ):
                        history.append([
                            x_temp,
                            y_temp,
                            0
                        ])
            elif len(history) > 1:
                history.pop(-1)
            else:
                history.pop(-1)
                x += 1
        return False

    def check_tile(self, board, x, y):
        return board[x][y]

    def get_winner(self):
        x = self.check("X")
        o = self.check("O")
        if x and o:
            return "Tie."
        elif x:
            return "X"
        elif o:
            return "O"
        else:
            return ""
