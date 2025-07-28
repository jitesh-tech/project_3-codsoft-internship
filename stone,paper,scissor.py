
# stone paper scissor game for codesoft
import tkinter as tk
import random

# NOW WE'LL CREATE THE MAIN CLASS FOR THE GAME

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("ROCK, PAPER, SCISSORS - GAME")
        self.root.geometry("600x400")  

       
        self.choices = ["Rock", "Paper", "Scissors"]

   
        self.user_score = 0
        self.computer_score = 0

        
        self.label = tk.Label(root, text="Choose Rock, Paper or Scissors", font=('Arial', 15))
        self.label.pack(pady=10)

     
        self.score_label = tk.Label(root, text="You: 0   <--|-->   Computer: 0", font=('Arial', 15))
        self.score_label.pack(pady=10)  

        #  styling the Buttons for Rock, Paper, Scissors
        for choice in self.choices:
            btn = tk.Button(root, text=choice, width=16, font=('Arial', 12),
                            command=lambda c=choice: self.play(c))
            btn.pack(pady=5)

        # RESULT DISPLAYING IS HERE
        self.result = tk.Label(root, text="", font=('Arial', 14), fg="blue")
        self.result.pack(pady=20)

        self.reset_button = tk.Button(root, text="Reset Game", width=20, font=('Arial', 12), bg='red', fg='white',
                                      command=self.reset_game)
        self.reset_button.pack(pady=15)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result_text = f"You chose {user_choice}, Computer chose {computer_choice}. "

        # MAIN LOGIC OF THE GAME
        if user_choice == computer_choice:
            result_text += "It's a draw! Try again."
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result_text += "You win!"
            self.user_score += 1
        else:
            result_text += "Computer wins!"
            self.computer_score += 1

        # NOW WE'LL UPDAAT THE LABELS
        self.result.config(text=result_text)
        self.score_label.config(text=f"You: {self.user_score}   <--|-->   Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result.config(text="Game has been reset. Start again!")
        self.score_label.config(text="You: 0   <--|-->   Computer: 0")


#  Start the game
root = tk.Tk()
game = RockPaperScissors(root)
root.mainloop()

