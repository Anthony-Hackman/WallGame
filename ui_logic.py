from tkinter import *
import subprocess

def start_game():
    subprocess.Popen(["python", "game_logic.py"])

def show_instructions():
    instructions_window = Toplevel(root)
    instructions_window.title("Instructions")
    instructions_window.config(bg="#4B5D67")
    instruction_text = "Game instructions\n\nAvoid the walls and survive as long as you can."
    instruction_label = Label(instructions_window, text=instruction_text, font=("Helvetica", 12, "italic"), fg='khaki', bg="#4B5D67")
    instruction_label.pack(pady=20, padx=20)
    close_button = Button(instructions_window, text="Close", font=("Helvetica", 14, "bold"), command=instructions_window.destroy, fg='khaki', bg="#4B5D67")
    close_button.pack(pady=10)

def exit_game():
    root.destroy()

root = Tk()
root.title('Wall Game - Main Menu')
root.config(bg="#4B5D67")

# Heading
heading_label = Label(root, text="Walls by Hack", font=("Helvetica", 24, "normal"), bg="#4B5D67", fg='khaki')
heading_label.pack(pady=10)

# Start Button
start_button = Button(root, text="Start Game", font=("Helvetica", 14, "bold"), command=start_game, fg='khaki', bg="#4B5D67")
start_button.pack(pady=10)

# Instructions
instructions_button = Button(root, text="Instructions", font=("Helvetica", 14, "bold"), command=show_instructions, fg='khaki', bg="#4B5D67")
instructions_button.pack(pady=10)

# Exit
exit_button = Button(root, text="Exit", font=("Helvetica", 14, "bold"), command=exit_game, fg='khaki', bg="#4B5D67")
exit_button.pack(pady=10)

root.mainloop()


