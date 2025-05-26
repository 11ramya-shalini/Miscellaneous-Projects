import tkinter as tk
import math

BG_COLOR = "#2c3e50"
ENTRY_BG = "#ecf0f1"
BTN_BG = "#34495e"
BTN_HOVER = "#3d566e"
BTN_OP = "#f34312"
BTN_EQUAL = "#27ae5fdd"
TEXT_COLOR = "#ffffff"
FONT = ("Arial", 16)


root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("600x600")
root.config(bg=BG_COLOR)
root.resizable(False,False)

entry = tk.Entry(root, font=("Arial", 20), bg=ENTRY_BG, fg="#000", borderwidth=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=25, padx=10, pady=10)

def click(symbol):
    entry.insert(tk.END, symbol)
def clear():
    entry.delete(0, tk.END)
def delete():
    entry.delete(len(entry.get())-1)
def calculate():
    try:
        expression = entry.get()
        expression = expression.replace("^", "**")
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")                

def apply_function(func):
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        if func == "sqrt":
            entry.insert(tk.END, math.sqrt(value))
        elif func == "log":
            entry.insert(tk.END, math.log10(value))
        elif func == "ln":
            entry.insert(tk.END, math.log(value))
        elif func == "sin":
            entry.insert(tk.END, math.sin(math.radians(value)))
        elif func == "cos":
            entry.insert(tk.END, math.cos(math.radians(value)))
        elif func == "tan":
            entry.insert(tk.END, math.tan(math.radians(value)))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

buttons = [
    ("7", "lightpink"), ("8", "lightpink"), ("9", "lightpink"), ("/", "orange"), ("√", "lightblue"),
    ("4", "lightpink"), ("5", "lightpink"), ("6", "lightpink"), ("*", "orange"), ("^", "lightblue"),
    ("1", "lightpink"), ("2", "lightpink"), ("3", "lightpink"), ("-", "orange"), ("π", "lightblue"),
    ("0", "lightpink"), (".", "lightpink"), ("=", "yellowgreen"), ("+", "orange"), ("e", "lightblue"),
    ("C", "#f34312"), ("Del", "#f34312"), ("sin", "lightblue"), ("cos", "lightblue"), ("tan", "lightblue"),
    ("ln", "lightblue"), ("log", "lightblue"),
]

row, col = 1, 0
for item in buttons:
    text, color = item[0], item[1]
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    elif text == "Del":
        cmd = delete
    elif text in ["sin", "cos", "tan", "log", "ln", "√"]:
        func_map = {"√": "sqrt", "sin": "sin", "cos": "cos", "tan": "tan", "log": "log", "ln": "ln"}
        cmd = lambda f=func_map[text]: apply_function(f)
    elif text in ["π", "e", "^"]:
        cmd = lambda t=text: click(t)
    else:
        cmd = lambda t=text: click(t)

    b = tk.Button(root, text=text, width=6, height=2, font=("Arial", 12),
                  bg=color, fg="black", command=cmd)
    b.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 4:
        col = 0
        row += 1  
root.mainloop()        