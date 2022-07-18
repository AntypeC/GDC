from ast import operator
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
    
    def parse(self, *kwargs):
        return 'break'

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
        global random_response
        new_line = "\n"
        random_response = ['smh...', 'smh...', 'smh...', 'smh...', "I was today years old when I realized I didn't like you.", "Someday you'll go far. And I really hope you stay there.", 'QUIT THIS !!']
        self.expr = self.source.get("1.0", tk.END) # A sin (B(x - C)) + D
        self.expr = self.expr.replace(new_line, '')
        self.source.delete("1.0", "end")

        chars = ' 0123456789+-*/.()'
        isEquation = False
        isContinuous = False
        intersection = []
        difference = []

        for i in list(self.expr):
            if i in list(chars):
                intersection.append(i) # append every element inside self.expr that is also inside chars
            if i not in intersection:
                difference.append(i) # append every element inside self.expr that isn't inside chars

        indices = len(difference)-1

        print('\nInput: ', new_line, self.expr)
        print('\nOutput: ')

        # import differences (key) for more unspecified continuous equations
        trig_end = ['n', 's']
        five_step_list = ['n', 'x']
        two_step_list = ['n', 'p', 's', 'i', 'n', 'n', 'p', 'c', 'o', 's', 'n', 'p', 't', 'a', 'n', 'x']

        def multiples(value, length):
            return [*range(value, length*value+1, value)]

        if difference == []: # condition 2
            isEquation = True
            isContinuous = False
        elif difference == ['x']: # condition 1
            isEquation = True
            isContinuous = True
        elif difference == ['n', 'p', 's', 'i', 'n']: # condition 2
            isEquation = True
            isContinuous = False
        elif difference == ['n', 'p', 'c', 'o', 's']: # condition 2
            isEquation = True
            isContinuous = False
        elif difference == ['n', 'p', 't', 'a', 'n']: # condition 2
            isEquation = True
            isContinuous = False
        elif difference == ['n', 'p', 's', 'i', 'n', 'x']: #condition 1
            isEquation = True
            isContinuous = True
        elif difference == ['n', 'p', 'c', 'o', 's', 'x']: #condition 1
            isEquation = True
            isContinuous = True
        elif difference == ['n', 'p', 't', 'a', 'n', 'x']: #condition 1
            isEquation = True
            isContinuous = True
        elif difference == ['n', 'p', 's', 'i', 'n', 'n', 'p', 's', 'i', 'n', 'x']: #condition 1
            isEquation = True
            isContinuous = True
        elif difference == ['n', 'p', 's', 'i', 'n', 'n', 'p', 'c', 'o', 's', 'x']: #condition 1
            isEquation = True
            isContinuous = True
        elif difference == ['n', 'p', 's', 'i', 'n', 'n', 'p', 't', 'a', 'n', 'x']: #condition 1
            isEquation = True
            isContinuous = True
        elif difference[0] == 'n' and difference[-1] == 'x': # big boi
            for n in multiples(5, int(indices/5)):
                if difference[n] in five_step_list:
                    for i in multiples(2, int(indices/2)):
                        if difference[i] in two_step_list:
                            isEquation = True
                            isContinuous = True
                        else:
                            pass
                else:
                    pass
        elif difference[0] == 'n' and difference[-1] in trig_end:
            for n in multiples(5, int(indices/5)):
                if difference[n] == 'n':
                    for i in multiples(2, int(indices/2)):
                        if difference[i] in two_step_list:
                            isEquation = True
                        else:
                            pass
                else:
                    pass
        else:
            pass
        
        if isEquation is True and isContinuous is True:
            x, y = self.generate_model()
            print(' Domain: ', f"{new_line} {np.array2string(x, precision=2, floatmode='fixed')}", new_line, 'Range: ', f"{new_line} {np.array2string(y, precision=2, floatmode='fixed')}")
            self.graph_plt(x, y)
        elif isEquation is True:
            x, y = self.generate_model()
            print(f' {y}')
            self.source.insert(tk.END, str(y))
        else:
            self.random_response()
        
        # print('\nDiagnostics:')
        # print(' intersection is ', intersection)
        # print(' difference (key) is ', difference)
        # print(' isEquation is ', isEquation)

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
        self.source.bind('<Return>', self.parse)

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
        x = np.linspace(-domain_range, domain_range)
        zero_div_error_response = ['Division by zero is not allowed.', "Zero-based division is not permitted.", "It is not permitted to divide by zero.", "It is forbidden to divide by zero."] 
        random.shuffle(zero_div_error_response)
        try:
            y = eval(self.expr)
        except ZeroDivisionError:
            y = zero_div_error_response[0]
        except Exception:
            self.random_response()
        return x, y
    
    def random_response(self):
        random.shuffle(random_response)
        print(random_response[0])
        self.source.insert(tk.END, random_response[0])

    def graph_plt(self, x, y):
        # x = np.linspace(0.2,10,100)
        # fig, ax = plt.subplots()
        # ax.plot(x, 1/x)
        # ax.plot(x, np.log(x))
        # ax.set_aspect('equal')
        # ax.grid(True, which='both')

        # ax.axhline(y=0, color='k')
        # ax.axvline(x=0, color='k')
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