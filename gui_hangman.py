from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Hangman Game")
win.geometry("800x500")
count = 0
stand = 'Helvetica 13'
lives = 0
letters_guessed = []

def clear_window():
    for widget in win.winfo_children():
                widget.destroy()

def get_word():
    global lives
    global letters_guessed
    global count
    count = 0
    letters_guessed = []
    lives = 6    
    clear_window()
    ttk.Label(win, text="Hanger, what is your word?", font=stand).pack()
    entry = Entry(win, width = 42)
    entry.config(show="*")
    entry.pack()
    ttk.Label(win, text = "Confirm Word", font=stand).pack()
    confirmation = Entry(win, width = 42)
    confirmation.config(show="*")
    confirmation.pack()
    ttk.Button(win, text = "Play", command = lambda: check_word(entry.get().upper(), confirmation.get().upper())).pack()

def check_word(word, confirmed):
    global count
    count += 1
    check_match = Label(win, text="", font=stand)
    check_match.pack()
    if word != confirmed or len(word) < 2 or not word.isalpha(): 
        if count > 1:
            pass
        else:
            check_match.config(text="ERROR. Please make sure the following are true:")
            ttk.Label(text="The words match\nOnly alphabetical characters are used\n"
                            "The word is at least 2 characters long", font=stand).pack()
                                    
    else:
        clear_window()
        play(word)

def play(string):
    board = []
    for _ in range(len(string)):
        board.append("_")
    ttk.Label(win, text='Guesser, guess a letter and click "Guess"', font=stand).pack()
    board_label = Label(win, text=board, font='Helvetica 32')
    board_label.pack()
    entry = Entry(win, width=1)
    entry.pack()
    ttk.Button(win, text="Guess", command=lambda: check_guess(entry, string, board, board_label, lives_label, guessed, check_length)).pack()
    lives_label = Label(win, text=str(lives) + " lives left", font=stand)
    lives_label.pack()
    check_length = Label(win, text="", font=stand)
    check_length.pack()
    guessed = Label(win, text=letters_guessed, font=stand)
    guessed.pack()

def check_guess(entry, string, list, label1, label2, guessed, check_length):
    global lives
    letter = entry.get().upper()
    entry.delete(0, END)
    if len(letter) > 1 or not letter.isalpha():
        check_length.config(text="Please guess exactly one alphabetical character at a time.")
        return
    else:
        check_length.config(text="")
    if letter in letters_guessed:
        return
    letters_guessed.append(letter)
    guessed.config(text=letters_guessed)
    if letter in string:
        i = 0
        for char in string:
            if char == letter:
                list[i] = letter
            i +=1
        label1.config(text=list)
        if "_" not in list:
            clear_window()
            end_game("Guesser", string)
    else:
        lives -= 1
        label2.config(text=str(lives) + " lives left")
        if lives == 0:
            clear_window()
            end_game("Hanger", string)


def end_game(winner, word):
    global lives
    ttk.Label(win, text=word, font='Helvetica 32').pack()
    ttk.Label(win, text=f"{lives} lives left. {winner} wins!").pack()
    ttk.Button(win, text="New Game", command=get_word).pack()
                        


def main():
    get_word()
    win.mainloop()
main()

