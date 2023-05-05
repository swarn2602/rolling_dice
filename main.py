import random
import tkinter as tk

# Define a function to roll the dice
def roll_ofdice():
    # Get the number of dice and number of sides from the input fields
    num_dice = int(num_of_entry.get())
    num_sides = int(num_sides_entry.get())
    # Roll the dice and store the results in a list
    rolls = []
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    # Update the result label with the rolls
    result_label.config(text="You rolled: " + str(rolls))

# Create a new Tkinter window
root = tk.Tk()
root.title("Dice Rolling Simulator")

# Create a label and input field for the number of dice
num_of_dice= tk.Label(root, text="Number of dice:")
num_of_dice.grid(row=0, column=0)

num_of_entry = tk.Entry(root)
num_of_entry.grid(row=0, column=1)

# Create a label and input field for the number of sides
num_sides_label = tk.Label(root, text="Number of sides:")
num_sides_label.grid(row=1, column=0)

num_sides_entry = tk.Entry(root)
num_sides_entry.grid(row=1, column=1)

# Create a button to roll the dice
roll_button = tk.Button(root, text="Try Your Luck ", command=roll_ofdice)
roll_button.grid(row=2, column=0, columnspan=2)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Start
root.mainloop()
