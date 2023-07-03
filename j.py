import tkinter as tk
import customtkinter as ctk
import random
from string import ascii_uppercase

def check_guess(letter):
    global guesses_left
    if letter in word:
        # Correct guess
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
        word_label.config(text=' '.join(guessed_word))
        if '_' not in guessed_word:
            result_label.config(text='Congratulations! You won!')
            keyboard_frame.grid_forget()  # Hide the keyboard after winning
    else:
        # Incorrect guess
        guesses_left -= 1
        if guesses_left == 0:
            result_label.config(text='Game over! The word was ' + word)
            keyboard_frame.grid_forget()  # Hide the keyboard after losing
        else:
            guesses_left_label.config(text='Guesses left: ' + str(guesses_left))

def create_keyboard(root):
    keyboard_frame = tk.Frame(root)
    keyboard_frame.grid(row=1, column=0, padx=10, pady=10)
    for index, letter in enumerate(ascii_uppercase):
        button = tk.Button(keyboard_frame, text=letter, width=4, height=2, command=lambda l=letter: check_guess(l))
        button.grid(row=index // 6, column=index % 6)
    return keyboard_frame

root = ctk.CTk()
root.title("Hangman Game")

words = ['HANGMAN', 'PYTHON', 'COMPUTER', 'PROGRAMMING', 'OPENAI']
word = random.choice(words).upper()
guessed_word = ['_'] * len(word)
guesses_left = 6

word_label = tk.Label(root, text=' '.join(guessed_word), font=('Arial', 24))
word_label.grid(row=0, column=0, padx=10, pady=10)

guesses_left_label = tk.Label(root, text='Guesses left: ' + str(guesses_left), font=('Arial', 16))
guesses_left_label.grid(row=2, column=0, padx=10, pady=10)

result_label = tk.Label(root, font=('Arial', 16))
result_label.grid(row=3, column=0, padx=10, pady=10)

keyboard_frame = create_keyboard(root)

root.mainloop()
