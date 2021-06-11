from tkinter import *
from tkinter import messagebox
import tkinter


def check():
    if((board["00"] == board["01"] == board["02"] == "X") or (board["00"] == board["10"] == board["20"] == "X") or (board["00"] == board["11"] == board["22"] == "X") or (board["01"] == board["11"] == board["21"] == "X") or (board["20"] == board["21"] == board["22"] == "X") or (board["10"] == board["11"] == board["12"] == "X") or (board["20"] == board["21"] == board["22"] == "X") or (board["02"] == board["11"] == board["20"] == "X")):
        winner = "player1"
        return winner
    elif((board["00"] == board["01"] == board["02"] == "O") or (board["00"] == board["10"] == board["20"] == "O") or (board["00"] == board["11"] == board["22"] == "O") or (board["01"] == board["11"] == board["21"] == "O") or (board["20"] == board["21"] == board["22"] == "O") or (board["10"] == board["11"] == board["12"] == "O") or (board["20"] == board["21"] == board["22"] == "O") or (board["02"] == board["11"] == board["20"] == "O")):
        winner = "player2"
        return winner
    elif((board["00"] == "X" or board["00"] == "O") and (board["01"] == "X" or board["01"] == "O") and (board["02"] == "X" or board["02"] == "O") and (board["10"] == "X" or board["10"] == "O") and (board["11"] == "X" or board["11"] == "O") and (board["12"] == "X" or board["12"] == "O") and (board["20"] == "X" or board["20"] == "O") and (board["21"] == "X" or board["21"] == "O") and (board["22"] == "X" or board["22"] == "O")):
        winner = "tie"
        return winner
    else:
        return False


def press(num):
    global player2, player1, window
    if(player1 == True):
        Label(window, font='arial 12 bold',
              text='Player 2 trun').grid(row=1, sticky='nesw')
    if(player2 == True):
        Label(window, font='arial 12 bold',
              text='Player 1 turn').grid(row=1, sticky='nesw')
    if player1 == True:
        text = "X"
    if player2 == True:
        text = "O"
    if(board[num] == "1" or board[num] == "0"):
        board[num] = text
        row = int(num[0])+3
        column = int(num[1])
        Button(window, text=text, font='arial 13 bold', width=6,
               bg='LimeGreen', padx=13, pady=13).grid(row=row, column=column, sticky='nesw')
        player1 = not(player1)
        player2 = not(player2)
        ch = check()
        if(ch == "player1"):
            window.destroy()
            messagebox.showinfo(title="Game Over", message="Player 1 Wins ")

        if(ch == "player2"):
            window.destroy()
            messagebox.showinfo(title="Game Over", message="Player 2 Wins")
        if(ch == "tie"):
            window.destroy()
            messagebox.showinfo(title="Game Over", message="Tie")
    else:
        return


game = True
if __name__ == "__main__":

    window = Tk()
    window.geometry("300x250")
    window.title("Tic-Tac-toe")
    window.resizable(0, 0)
    player1 = True
    player2 = False

    board = {"00": "0", "01": "1", "02": "0", "10": "1",
             "11": "0", "12": "1", "20": "0", "21": "1", "22": "0"}

    Label(window, font='arial 12 bold',
          text='TIC-TAC-TOE').grid(row=0, sticky='nesw')

    btn00 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("00"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=3, column=0, sticky='nesw')
    btn01 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("01"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=3, column=1, sticky='nesw')
    btn02 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("02"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=3, column=2, sticky='nesw')

    btn10 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("10"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=4, column=0, sticky='nesw')
    btn11 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("11"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=4, column=1, sticky='nesw')
    btn12 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("12"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=4, column=2, sticky='nesw')

    btn20 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("20"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=5, column=0, sticky='nesw')
    btn21 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("21"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=5, column=1, sticky='nesw')
    btn22 = Button(window, text='', font='arial 13 bold', width=6, command=lambda: press("22"),
                   bg='LimeGreen', padx=13, pady=13).grid(row=5, column=2, sticky='nesw')

    window.mainloop()
