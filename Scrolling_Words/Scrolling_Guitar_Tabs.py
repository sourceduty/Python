import tkinter as tk

# Guitar Tabs
tabs = """
e|-------------------------------0--0--0--0--0--0--0--0---------------------|
B|-------------------1--1--1--1--------------1--------------1--1--1--1------|
G|------------0--0----------------------------------------------------------|
D|------2--2-----------------------------------------------------------------|
A|--3--3---------------------------------------------------------------------|
E|---------------------------------------------------------------------------|

e|-------------------------------0--0--0--0--0--0--0--0---------------------|
B|-------------------1--1--1--1--------------1--------------1--1--1--1------|
G|------------0--0----------------------------------------------------------|
D|------2--2-----------------------------------------------------------------|
A|--3--3---------------------------------------------------------------------|
E|---------------------------------------------------------------------------|

e|-------------------------------0--0--0--0--0--0--0--0---------------------|
B|-------------------1--1--1--1--------------1--------------1--1--1--1------|
G|------------0--0----------------------------------------------------------|
D|------2--2-----------------------------------------------------------------|
A|--3--3---------------------------------------------------------------------|
E|---------------------------------------------------------------------------|

e|-------------------------------0--0--0--0--0--0--0--0---------------------|
B|-------------------1--1--1--1--------------1--------------1--1--1--1------|
G|------------0--0----------------------------------------------------------|
D|------2--2-----------------------------------------------------------------|
A|--3--3---------------------------------------------------------------------|
E|---------------------------------------------------------------------------|

e|-------------------------------0--0--0--0--0--0--0--0---------------------|
B|-------------------1--1--1--1--------------1--------------1--1--1--1------|
G|------------0--0----------------------------------------------------------|
D|------2--2-----------------------------------------------------------------|
A|--3--3---------------------------------------------------------------------|
E|---------------------------------------------------------------------------|
"""

class ASCIIAnimation:
    def __init__(self, root):
        self.root = root
        self.y_pos = root.winfo_screenheight()

        # Canvas for Guitar Tabs
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Adding Guitar Tabs to Canvas
        self.text_id = self.canvas.create_text(400, self.y_pos, text=tabs, font=("Courier", 10), anchor="s")

        # Start Animation
        self.animate()

    def animate(self):
        self.y_pos -= 2  # Speed of scrolling
        self.canvas.coords(self.text_id, 400, self.y_pos)

        # Reset position for continuous loop
        if self.y_pos < -self.root.winfo_screenheight():
            self.y_pos = self.root.winfo_screenheight()

        self.root.after(50, self.animate)  # Adjust for smoother or faster animation

# Application Window
root = tk.Tk()
root.geometry("800x600")
root.title("Guitar Tabs Animation")

app = ASCIIAnimation(root)

root.mainloop()