import tkinter as tk
from unittest import result

class SquareGridApp:
    def __init__(self, master, rows=20, cols=20):
        # Store the reference to the parent window and the dimensions of the grid
        self.master = master
        self.rows = rows
        self.cols = cols

        # Initialize a 2D list called 'colors' to track each cell's color state.
        # True means the cell is white, False means the cell is black.
        self.colors = [[True for _ in range(cols)] for _ in range(rows)]

        # We'll keep a parallel 2D list of Label widgets to display our grid.
        self.labels = []

        # Create a grid of Label widgets, each one representing a cell.
        for r in range(rows):
            row_labels = []
            for c in range(cols):
                # Create a label that represents a single cell.
                # 'width' and 'height' set its size, 'bg="white"' sets its initial color.
                # 'borderwidth=1' and 'relief="solid"' give it a visible border.
                lbl = tk.Label(master, width=2, height=1, bg="white", borderwidth=1, relief="solid")

                # Place the label in the grid layout at position (r, c).
                # 'padx' and 'pady' add some space around the cells.
                lbl.grid(row=r, column=c, padx=1, pady=1)

                # Bind a left mouse click event ("<Button-1>") to this label.
                # When clicked, it calls 'self.toggle_color(rr, cc)' with the row and column of this cell.
                # We use a lambda function to capture the current 'r' and 'c' values.
                lbl.bind("<Button-1>", lambda e, rr=r, cc=c: self.toggle_color(rr, cc))

                # Append this label to the current row's list.
                row_labels.append(lbl)

            # After finishing one row, add the row of labels to 'self.labels'.
            self.labels.append(row_labels)

        # Create a "Generate" button below the grid.
        # When clicked, it calls 'self.generate_string()'.
        gen_button = tk.Button(master, text="Generate", command=self.generate_string)

        # Position the "Generate" button in the next row below the grid.
        # 'columnspan=cols' makes it stretch across the entire width of the grid.
        gen_button.grid(row=rows, column=0, columnspan=cols)

    def toggle_color(self, r, c):
        # Flip the boolean value in 'self.colors' for the clicked cell.
        # If it was True (white), now it becomes False (black), and vice versa.
        self.colors[r][c] = not self.colors[r][c]

        # Determine the new color based on the boolean value.
        new_color = "white" if self.colors[r][c] else "black"

        # Update the label widget's background color to reflect the change.
        self.labels[r][c].configure(bg=new_color)

    def generate_string(self):
        # This function generates a string representation of the current grid.
        # '-' represents a white cell, '#' represents a black cell.

        lines = []
        for r in range(self.rows):
            line = []
            for c in range(self.cols):
                # Check the cell's color. If True (white), append '-', otherwise '#'.
                line.append('-' if self.colors[r][c] else '#')
            # Join the row of characters into a single string.
            lines.append(''.join(line))
        
        result = '\n'.join(lines)
        # Print the entire grid, each row on a new line.
        print(result)
        return result 

if __name__ == "__main__":
    # This block only runs if this script is executed directly (not imported).

    # Create the main application window.
    root = tk.Tk()
    # Set the window title.
    root.title("Clickable Grid")

    # Create an instance of SquareGridApp, passing in the 'root' window.
    app = SquareGridApp(root)

    # Start the Tkinter event loop, so the window stays open and responds to user actions.
    root.mainloop()
    grid_string = app.generate_string()
    print('Here is the grid string:')
    print(grid_string)