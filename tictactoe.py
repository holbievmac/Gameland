import tkinter as tk
import tkinter.messagebox as tkMessageBox
import random


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe: Humano vs Máquina")
        self.buttons = {}
        self.setup_ui()
        self.new_game()

    def setup_ui(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 20), height=3, width=6,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[(i, j)] = button

    def new_game(self):
        for button in self.buttons.values():
            button.config(text='', bg='SystemButtonFace', state=tk.NORMAL)
        self.turn = 'X'  # Humano inicia

    def on_button_click(self, row, col):
        if self.buttons[(row, col)]['text'] == '' and self.turn == 'X':
            self.make_move(row, col, 'X')
            if not self.check_for_winner('X'):
                self.ai_move()

    def make_move(self, row, col, player):
        self.buttons[(row, col)]['text'] = player
        self.buttons[(row, col)]['fg'] = 'red' if player == 'X' else 'blue'
        if self.check_for_winner(player):
            self.end_game(player)
        elif all(button['text'] != '' for button in self.buttons.values()):
            self.end_game(None)

    def check_for_winner(self, player):
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]
        ]
        for condition in win_conditions:
            if all(self.buttons[coord]['text'] == player for coord in condition):
                for coord in condition:
                    self.buttons[coord]['bg'] = 'green'
                return True
        return False

    def end_game(self, winner):
        if winner:
            tkMessageBox.showinfo("Fin del juego", f"El jugador {winner} ha ganado!")
        else:
            tkMessageBox.showinfo("Empate", "Ha sido un empate!")
        for coords in self.buttons:
            self.buttons[coords].config(state=tk.DISABLED)
        self.root.after(2000, self.new_game)

    def ai_move(self):
        empty_buttons = [coords for coords, button in self.buttons.items() if button['text'] == '']
        if empty_buttons:
            move = self.find_best_move(empty_buttons)
            self.make_move(move[0], move[1], 'O')

    def find_best_move(self, empty_buttons):
        # Estrategia básica: primero intenta ganar, luego bloquea, sino elige al azar
        for player in ['O', 'X']:  # Primero revisa si 'O' puede ganar, luego bloquea 'X'
            for coords in empty_buttons:
                row, col = coords
                self.buttons[(row, col)]['text'] = player
                if self.check_for_winner(player):
                    self.buttons[(row, col)]['text'] = ''
                    return coords
                self.buttons[(row, col)]['text'] = ''
        return random.choice(empty_buttons)


def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
