import tkinter as tk
import math

window  = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x500")
window.resizable(False, False)
window.configure(bg="grey")

exp = ""

def equalpress():
    global exp
    try:
        result = str(eval(exp))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""
            
def press(value):
    global exp
    if value == 'sin':
        try:
            result = str(math.sin(math.radians(float(exp))))
            equation.set(result)
            exp = result
        except:
            equation.set("Error")
            exp = ""
    elif value == 'cos':
        try:
            result = str(math.cos(math.radians(float(exp))))
            equation.set(result)
            exp = result
        except:
            equation.set("Error")
            exp = ""
    elif value == 'tan':
        try:
            result = str(math.tan(math.radians(float(exp))))
            equation.set(result)
            exp = result
        except:
            equation.set("Error")
            exp = ""
    else:
        if exp == "Error":
            exp = ""
        if value == 'C':
            exp = ""
        else:
            if exp and (exp[-1] in "+-*/" and value in "+-*/"):
                exp = exp[:-1]
    exp += str(value)
    equation.set(exp)
    


def clear():
    global exp
    exp = ""
    equation.set("")
    
def on_key(event):
    key = event.keysym
    if key in '0123456789':
        press(key)
    elif key in ('plus', 'KP_Add'):
        press('+')
    elif key in ('minus', 'KP_Subtract'):
        press('-')
    elif key in ('asterisk', 'KP_Multiply'):
        press('*')
    elif key in ('slash', 'KP_Divide'):
        press('/')
    elif key == 'Return':
        equalpress()
    elif key == 'period':
        press('.')
    elif key == 'BackSpace':
        global exp
        exp = exp[:-1]
        equation.set(exp)
    elif key == 'Escape':
        clear()
        
window.bind('<Key>', on_key)
    
equation = tk.StringVar()

frame = tk.Frame(window, bg="white", bd=5, relief="ridge")
frame.place(x=10, y=100, width=380, height=300)  

entry_field = tk.Entry(window, textvariable=equation, font=("Arial", 20), bd=20, insertwidth=4,
                        width=24, borderwidth=4, relief="ridge", justify='right')

entry_field.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4),  
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('Clear', 4, 4)
]

for i in range(5):  
    frame.columnconfigure(i, weight=1)
for i in range(5):  
    frame.rowconfigure(i, weight=1)

for (text, row, col) in buttons:
    color = "darkgrey"
    if text in ('+', '-', '*', '/', '='):
        color = "skyblue"
    elif text == 'Clear':
        color = "white"
    elif text in ('sin', 'cos', 'tan'):
        color = "lightgreen"
    tk.Button(frame, text=text, font=('Arial', 16, 'bold'),
              bg=color, fg="black", activebackground="orange",
              command=equalpress if text == '=' else clear if text == 'Clear' else lambda t=text: press(t)
    ).grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
    
window.mainloop()        


    



