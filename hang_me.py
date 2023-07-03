import customtkinter as ctk
import tkinter as tk
from string import ascii_uppercase
from PIL import Image, ImageTk
import random

# Setting default theme and appearance mode
ctk.set_default_color_theme("green") 
ctk.set_appearance_mode('dark')

# List of words
words = ['hangman', 'python', 'programming', 'bestz', 'computer', "prince"]

# Hangman art
hangman_pics = [
    '''
       +---+
           |
           |
           |
          ===''',
    '''
       +---+
       O   |
           |
           |
          ===''',
    '''
       +---+
       O   |
       |   |
           |
          ===''',
    '''
       +---+
       O   |
      /|   |
           |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
           |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      /    |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      / \\  |
          ==='''
]

# Initialize game variables
current_word = ''
current_word_display = ''
remaining_guesses = 6
guessed_letters = set()

def start_game():
    global current_word, current_word_display, remaining_guesses, guessed_letters
    current_word = random.choice(words).lower()
    current_word_display = " _ " * len(words)
    remaining_guesses = 6
    guessed_letters = set()
    word_label.configure(text=current_word_display)
    hangman_label.configure(text=hangman_pics[0])
    status_label.configure(text='')

def restart_game():
    global current_word, current_word_display, remaining_guesses, guessed_letters
    current_word = random.choice(words).lower()
    current_word_display = " _ " * len(words)
    remaining_guesses = 6
    guessed_letters = set()
    word_label.configure(text=current_word_display)
    hangman_label.configure(text=hangman_pics[0])
    status_label.configure(text='')

def make_guess():
    global remaining_guesses, current_word_display
    guess = guessed_letters.get().lower()
    guessed_letters.delete(0, ctk.END)
    if len(guess) != 1 or not guess.isalpha():
        status_label.configure(text='Invalid guess. Please enter a single letter.')
        return
    if guess in guessed_letters:
        status_label.configure(text='You already guessed that letter.')
        return
    guessed_letters.add(guess)
    if guess in current_word:
        current_word_display = ''.join([c if c in guessed_letters else '_' for c in current_word])
        word_label.configure(text=current_word_display)
        if current_word_display == current_word:
            status_label.configure(text='Congratulations! You won!')
            return
    else:
        remaining_guesses -= 1
        hangman_label.configure(text=hangman_pics[6 - remaining_guesses])
        if remaining_guesses == 0:
            status_label.configure(text=f'Game Over. The word was "{current_word}".')
            return
    status_label.configure(text=f'Remaining guesses: {remaining_guesses}')

# Create the main root
root = ctk.CTk()
root.title('Hangman')

# Hangman image label
hangman_label = ctk.CTkLabel(root, font=('Courier', 14), justify=ctk.LEFT)
hangman_label.pack()

# Word label
word_label = ctk.CTkLabel(root, font=('Courier', 18, 'bold'), pady=10)
word_label.pack()

# Guess entry and button
# guess_entry = ctk.CTkEntry(root, font=('Courier', 14))
# guess_entry.pack()
guess_button = ctk.CTkButton(root, text='Guess', font=('Courier', 14,),corner_radius= 15, command=make_guess)
guess_button.pack(pady=10)

# Status label
status_label = ctk.CTkLabel(root, font=('Courier', 14), pady=10)
status_label.pack()

# Start button
start_button = ctk.CTkButton(root, text='Start', font=('Courier', 14, "bold"),corner_radius= 15, command=start_game)
start_button.pack()

restart_button = ctk.CTkButton(root, text='restart', font=('Courier', 14, "bold"), corner_radius= 15, command=restart_game)
restart_button.pack(pady=10)

if __name__=="__main__":
    start_game()
    restart_game()
    make_guess()



    root.mainloop()

# Start the Game
