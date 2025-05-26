import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(True,True)
root.mainloop()

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, padx=10, pady=10)