import tkinter as tk
from tkinter import messagebox, Canvas, PhotoImage, VERTICAL
from PIL import Image, ImageTk

class MontyHallGUI:
    def __init__(self, master):
        self.master = master
        master.title("Monty Hall Problem Simulator")

        # Label
        self.label = tk.Label(master, text="Select the number of doors:")
        self.label.pack()

        # Entry for number of doors
        self.num_doors_entry = tk.Entry(master)
        self.num_doors_entry.pack()

        # Button to run simulation
        self.run_button = tk.Button(master, text="Run Simulation", command=self.run_simulation)
        self.run_button.pack()

        # Frame for door buttons and canvas with scrollbar
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack()

        self.canvas = Canvas(self.canvas_frame, width=800, height=200, scrollregion=(0, 0, 800, 200))
        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # List to store door buttons
        self.door_buttons = []

    def create_doors(self, num_doors):
        # Clear existing door buttons
        for button in self.door_buttons:
            button.destroy()
        self.door_buttons = []

        # Calculate the number of rows needed
        num_rows = (num_doors + 9) // 10

        # Load door image
        door_image = Image.open("door.png")
        door_image = door_image.resize((50, 100), Image.LANCZOS)
        door_photo = ImageTk.PhotoImage(door_image)

        # Create new door buttons with space between them
        button_width = 60
        button_height = 120
        space_between = 10

        for i in range(num_doors):
            row_index = i // 10
            col_index = i % 10

            x_position = col_index * (button_width + space_between)
            y_position = row_index * (button_height + space_between)

            door_button = tk.Button(self.canvas, image=door_photo, text=f"Door {i + 1}",
                                    command=lambda i=i: self.select_door(i))
            door_button.photo = door_photo
            self.door_buttons.append(door_button)

            # Add the door button to the canvas using the create_window method
            self.canvas.create_window(x_position, y_position, window=door_button, anchor='nw')

        # Update canvas size and scroll region
        canvas_width = max(800, 10 * (button_width + space_between))
        self.canvas.config(width=canvas_width, height=num_rows * (button_height + space_between),
                           scrollregion=(0, 0, canvas_width, num_rows * (button_height + space_between)))
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def run_simulation(self):
        try:
            num_doors = int(self.num_doors_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for doors.")
            return

        if num_doors < 3:
            messagebox.showerror("Error", "Number of doors should be at least 3.")
            return

        # Create door buttons
        self.create_doors(num_doors)

        

    def select_door(self, door_index):
        messagebox.showinfo("Selected Door", f"You selected door {door_index + 1}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MontyHallGUI(root)
    root.mainloop()
