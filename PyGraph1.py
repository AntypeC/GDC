import matplotlib.pyplot as plt
import numpy as np
import os
import random
import tkinter as tk

class Entry_gui:
    def __init__(self, master):
        self.master = master
        self.expr = ''
        master.title("GDC")
        master.geometry("375x550")

        self.source = tk.Text()
        self.source.pack() 
        self.source.config(font=("Courier"))

        self.btn_layout()

    def zeroButtonFunction(self, *kwargs): # number 0-9
        self.source.insert(tk.END, '0')

    def oneButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '1')

    def twoButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '2')

    def threeButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '3')

    def fourButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '4')

    def fiveButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '5')

    def sixButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '6')

    def sevenButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '7')

    def eightButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '8')

    def nineButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '9')

    def addButtonFunction(self, *kwargs): 
        self.source.insert(tk.END, '+')

    def subButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '-')

    def multButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '*')

    def divButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '/')

    def decimalButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '.')

    def equalButtonFunction(self, *kwargs):
        self.expr = self.source.get("1.0", tk.END) # A sin (B(x - C)) + D
        self.source.delete("1.0", "end")
        x, y = self.generate_model()
        new_line = "\n"
        self.expr = self.expr.replace(new_line, '')
        print('\nInput: \n', self.expr)
        print('\nOutput: ')
        if 'x' in self.expr:
            print(' Domain: ', f"{new_line} {np.array2string(x, precision=2, floatmode='fixed')}", '\n Range: ', f"{new_line} {np.array2string(y, precision=2, floatmode='fixed')}")
            self.graph_plt(x, y)
        else:
            print(f' {y}')
            self.source.insert(tk.END, str(y))

    def clearButtonFunction(self, *kwargs):
        self.source.delete('1.0', tk.END)

    def parentheses1ButtonFunction(self, *kwargs):
        self.source.insert(tk.END, '(')

    def parentheses2ButtonFunction(self, *kwargs):
        self.source.insert(tk.END, ')')

    def trigButtonFunction(self, *kwargs):
        self.sinButton.place(x=280, y=50)
        self.cosButton.place(x=280, y=150)
        self.tanButton.place(x=280, y=250)
        self.backButton.place(x=280, y=450)

    def sinButtonFunction(self, *kwargs):
        self.source.insert(tk.END, 'np.sin(')

    def cosButtonFunction(self, *kwargs):
        self.source.insert(tk.END, 'np.cos(')

    def tanButtonFunction(self, *kwargs):
        self.source.insert(tk.END, 'np.tan(')

    def backButtonFunction(self, *kwargs):
        self.sinButton.place_forget()
        self.cosButton.place_forget()
        self.tanButton.place_forget()
        self.backButton.place_forget()
        
    def btn_layout(self):
        oneButton = tk.Button(self.master, text="1", width=10, height=5)
        oneButton.place(x=10, y=50)
        oneButton.bind('<Button-1>', self.oneButtonFunction)

        twoButton = tk.Button(self.master, text="2", width=10, height=5)
        twoButton.place(x=100, y=50)
        twoButton.bind('<Button-1>', self.twoButtonFunction)

        threeButton = tk.Button(self.master, text="3", width=10, height=5)
        threeButton.place(x=190, y=50)
        threeButton.bind('<Button-1>', self.threeButtonFunction)

        fourButton = tk.Button(self.master, text="4", width=10, height=5)
        fourButton.place(x=10, y=150)
        fourButton.bind('<Button-1>', self.fourButtonFunction)

        fiveButton = tk.Button(self.master, text="5", width=10, height=5)
        fiveButton.place(x=100, y=150)
        fiveButton.bind('<Button-1>', self.fiveButtonFunction)

        sixButton = tk.Button(self.master, text="6", width=10, height=5)
        sixButton.place(x=190, y=150)
        sixButton.bind('<Button-1>', self.sixButtonFunction)

        sevenButton = tk.Button(self.master, text="7", width=10, height=5)
        sevenButton.place(x=10, y=250)
        sevenButton.bind('<Button-1>', self.sevenButtonFunction)

        eightButton = tk.Button(self.master, text="8", width=10, height=5)
        eightButton.place(x=100, y=250)
        eightButton.bind('<Button-1>', self.eightButtonFunction)

        nineButton = tk.Button(self.master, text="9", width=10, height=5)
        nineButton.place(x=190, y=250)
        nineButton.bind('<Button-1>', self.nineButtonFunction)

        zeroButton = tk.Button(self.master, text="0", width=10, height=5)
        zeroButton.place(x=100, y=350)
        zeroButton.bind('<Button-1>', self.zeroButtonFunction)

        decimalButton = tk.Button(self.master, text=".", width=6, height=5)
        decimalButton.place(x=10, y=350)
        decimalButton.bind('<Button-1>', self.decimalButtonFunction)

        equalButton = tk.Button(self.master, text="=", width=10, height=5)
        equalButton.place(x=190, y=350)
        equalButton.bind('<Button-1>', self.equalButtonFunction)

        addButton = tk.Button(self.master, text="+", width=10, height=5)
        addButton.place(x=280, y=50)
        addButton.bind('<Button-1>', self.addButtonFunction)

        subButton = tk.Button(self.master, text="-", width=10, height=5)
        subButton.place(x=280, y=150)
        subButton.bind('<Button-1>', self.subButtonFunction)

        multButton = tk.Button(self.master, text="X", width=10, height=5)
        multButton.place(x=280, y=250)
        multButton.bind('<Button-1>', self.multButtonFunction)

        divButton = tk.Button(self.master, text="/", width=10, height=5)
        divButton.place(x=280, y=350)
        divButton.bind('<Button-1>', self.divButtonFunction)

        clearButton = tk.Button(self.master, text="Clear", width=10, height=5)
        clearButton.place(x=10, y=450)
        clearButton.bind('<Button-1>', self.clearButtonFunction)

        parentheses1Button = tk.Button(self.master, text="(", width=10, height=5)
        parentheses1Button.place(x=100, y=450)
        parentheses1Button.bind('<Button-1>', self.parentheses1ButtonFunction)

        parentheses2Button = tk.Button(self.master, text=")", width=10, height=5)
        parentheses2Button.place(x=190, y=450)
        parentheses2Button.bind('<Button-1>', self.parentheses2ButtonFunction)

        trigButton = tk.Button(self.master, text="Trig", width=10, height=5)
        trigButton.place(x=280, y=450)
        trigButton.bind('<Button-1>', self.trigButtonFunction)

        self.sinButton = tk.Button(self.master, text="Sin", width=10, height=5)
        self.sinButton.bind('<Button-1>', self.sinButtonFunction)

        self.cosButton = tk.Button(self.master, text="Cos", width=10, height=5)
        self.cosButton.bind('<Button-1>', self.cosButtonFunction)

        self.tanButton = tk.Button(self.master, text="Tan", width=10, height=5)
        self.tanButton.bind('<Button-1>', self.tanButtonFunction)

        self.backButton = tk.Button(self.master, text="Back", width=10, height=5)
        self.backButton.bind('<Button-1>', self.backButtonFunction)

    def generate_model(self, domain_range=50):
        # start=0
        # step=0.001

        x = np.array(range(domain_range)) # set range
        # x = np.arange(0,domain_range)*step+start

        random_response = ['smh...', 'smh...', 'smh...', 'smh...', "I was today years old when I realized I didn't like you.", "Someday you'll go far. And I really hope you stay there.", 'QUIT THIS !!']
        zero_div_error_response = ['Division by zero is not allowed.', "Zero-based division is not permitted.", "It is not permitted to divide by zero.", "It is forbidden to divide by zero."]
        random.shuffle(random_response)
        random.shuffle(zero_div_error_response)
        
        try:
            y = eval(self.expr)
        except ZeroDivisionError:
            y = zero_div_error_response[0]
        except NameError or SyntaxError:
            y = random_response[0]
        return x, y

    def graph_plt(self, x, y):
        plt.style.use('dark_background')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid()
        plt.plot(x, y)
        plt.savefig(f"history/{self.expr}_graph.png", format="png", dpi=1200)
        plt.show()


root = tk.Tk()
Entry_gui(root)
root.mainloop()