import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    text_edit.delete('1.0', tk.END)  # clear the Text widget
    with open(filepath, "r") as f:
        contents = f.read()
        text_edit.insert(tk.END, contents)
    # Change the name of the window to the opened file name
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    with open(filepath, "w") as f:
        contents = text_edit.get('1.0', tk.END)
        f.write(contents)
    window.title(f"Save File: {filepath}")

def main():
    # Initialize  the Tkinter window.
    window = tk.Tk()
    window.title("Text-editor")
    # Configure size of text component
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    # Text edit widget
    text_edit = tk.Text(window, font="Helvetica 18")
    # Uses a grid system row 0 col 0 = top left corner
    text_edit.grid(row=0, column=1)

    # Create Frame and Buttons within the frame
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command= lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command= lambda: open_file(window, text_edit))

    # Sticky arg for buttons keeps them the identical in size
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    # sticky arg on makes sure frame stays in place when resizing window and on a certain side
    frame.grid(row=0, column=0, sticky="ns")

    # Bind commands to key press
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()

main()
