from manim import *
import numpy as np
import tkinter as tk
from grip_app import run_app, default_string  # Import the function from test.py

class LifeGame(Scene):
    def construct(self): 
        height = 30
        width = int(height * 1.5)
        #maze_string = run_app(rows=height, cols=width)
        maze_string = default_string()
        # Now you have the grid_string here, you can use it to do whatever you like.
        # For example, just create a square to show that the scene works:
        # You could also print the grid_string to the console here if you like:
        print("Received maze string in Manim:\n", maze_string)

        maze = []  # 2D array of squares like we see it
        maze_bool = []  # 2D array of true/false values
        all_squares = VGroup()

        for row in maze_string.strip().split("\n"):
            maze.append([])
            maze_bool.append([])
            for char in row:
                maze[-1].append(
                    Square(
                        color=WHITE if char == "-" else BLACK,
                        fill_opacity=1
                    ).scale(0.1*30/height)
                ) #create a 2d array of squares
                maze_bool[-1].append(char != "-") #create a 2d array of bools for the squares, True(live) if white, False(dead) if black
                all_squares.add(maze[-1][-1]) #add a VGroup of all squares
        
        rows = len(maze)
        cols = len(maze[0])
        
        #self.play(FadeIn(all_squares.arrange_in_grid(rows, cols, buff=0.05)))

        def get_neighbors_center(r, c, rows, cols):
            neighbors = []
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        neighbors.append((r + dr, c + dc))
            return neighbors
        
        def get_neighbors_edge(r, c, rows, cols):
            neighbors = []
            if r == 0 and c == 0:
                neighbors = [(0, 1), (1, 0), (1, 1)]
            elif r == 0 and c == cols - 1:
                neighbors = [(0, cols - 2), (1, cols - 1), (1, cols - 2)]
            elif r == rows - 1 and c == 0:
                neighbors = [(rows - 1, 1), (rows - 2, 0), (rows - 2, 1)]
            elif r == rows - 1 and c == cols - 1:
                neighbors = [(rows - 1, cols - 2), (rows - 2, cols - 1), (rows - 2, cols - 2)]
            elif r == 0:
                neighbors = [(0, c - 1), (0, c + 1), (1, c - 1), (1, c), (1, c + 1)]
            elif r == rows - 1:
                neighbors = [(rows - 1, c - 1), (rows - 1, c + 1), (rows - 2, c - 1), (rows - 2, c), (rows - 2, c + 1)]
            elif c == 0:
                neighbors = [(r - 1, 0), (r + 1, 0), (r - 1, 1), (r, 1), (r + 1, 1)]
            elif c == cols - 1:
                neighbors = [(r - 1, cols - 1), (r + 1, cols - 1), (r - 1, cols - 2), (r, cols - 2), (r + 1, cols - 2)]
            return neighbors
        
        def calculate_new_state(r, c, rows, cols, maze_bool):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                neighbors = get_neighbors_edge(r, c, rows, cols)
            else:
                neighbors = get_neighbors_center(r, c, rows, cols)
            live_neighbors = sum([maze_bool[nr][nc] for nr, nc in neighbors])
            if maze_bool[r][c] and live_neighbors in [2, 3]:
                return True
            if not maze_bool[r][c] and live_neighbors == 3:
                return True
            return False
        
        def update_maze(maze_bool, rows, cols):
            new_maze_bool = np.zeros((rows, cols), dtype=bool)
            for r in range(rows):
                for c in range(cols):
                    new_maze_bool[r][c] = calculate_new_state(r, c, rows, cols, maze_bool)
            return new_maze_bool
        
        def maze_check(maze_bool):
            text = []
            for r in range(len(maze_bool)):
                text.append([])
                for c in range(len(maze_bool[0])):
                    if maze_bool[r][c]:
                        text[-1].append("#")
                    else:
                        text[-1].append("-")
                text[-1] = "".join(text[-1])
            return "\n".join(text)
                        
        
        generation = 300
        group = []

        for i in range(generation):
            #print(maze_check(maze_bool), "\n")
            maze_bool = update_maze(maze_bool, rows, cols)
            
            # Update colors in-place
            for r in range(rows):
                for c in range(cols):
                    maze[r][c].set_color(BLACK if maze_bool[r][c] else WHITE)
            
            # Create a new VGroup for the current state
            current_squares = VGroup(*[maze[r][c] for r in range(rows) for c in range(cols)])
            current_squares.arrange_in_grid(rows, cols, buff=0.05)
            
            # Show the current state
            if i == 0:
                self.play(FadeIn(current_squares))
            else:
                # Transform previous state into the current state for a smooth transition
                self.play(Transform(previous_squares, current_squares), run_time=0.1)
            
            self.wait(0.1)
            previous_squares = current_squares

            
