import tkinter as tk
from tkinter import messagebox

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ValueError("cannot divide by zero")
    return a/b


class CalculatorApp:
    def __init__(self,root):
        self.root=root
        self.root.title("🧮 Simple Calculator")
        self.root.geometry("400x300")
        self.root.configure(bg="#d8aef0")

        #input fields
        tk.Label(root, text="Enter first number:").pack(pady=5)
        self.entry1 =tk.Entry(root)
        self.entry1.pack()

        tk.Label(root, text="Enter second number:").pack(pady=5)
        self.entry2 =tk.Entry(root)
        self.entry2.pack()

        # Buttons for operations
        button_frame =tk.Frame(root, bg="#b258e7")
        button_frame.pack(pady=10)

        tk.Button(button_frame,text="+",width=8, command=self.handle_add).grid(row=0, column=0, padx=5)
        tk.Button(button_frame,text="-",width=8, command=self.handle_subtract).grid(row=0, column=1, padx=5)
        tk.Button(button_frame,text="x",width=8, command=self.handle_multiply).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame,text="/",width=8, command=self.handle_divide).grid(row=1, column=1, padx=5, pady=5)

        # Result label
        self.result_label= tk.Label(root, text="Result", font="bold", bg="#9F8FA9")
        self.result_label.pack(pady=15)

    def get_inputs(self):
        try:
            a= float(self.entry1.get())
            b= float(self.entry2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None
        

    def handle_add(self):
        a,b= self.get_inputs()
        if a is not None:
            result= add(a,b)
            self.result_label.config(text= f"Result: {result}")


    def handle_subtract(self):
        a,b= self.get_inputs()
        if a is not None:
            result= subtract(a,b)
            self.result_label.config(text= f"Result: {result}")

    def handle_multiply(self):
        a,b= self.get_inputs()
        if a is not None:
            result= multiply(a,b)
            self.result_label.config(text= f"Result: {result}")

    def handle_divide(self):
        a,b= self.get_inputs()
        if a is not None:
            try:
                result= divide(a,b)
                self.result_label.config(text= f"Result: {result}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

if __name__== "__main__":
    root= tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()