import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="---------- Hello, World! ----------")

radio_var = tk.StringVar()
radioButton1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1", command=None)
radioButton2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2", command=None)
radioButton3 = tk.Radiobutton(window, text="Option 3", variable=radio_var, value="Option 3", command=None)

button = tk.Button(window, text="Clear")

def main():
  button.bind("<Button-1>", doTheThing)

  greeting.pack()

  radioButton1.pack()
  radioButton2.pack()
  radioButton3.pack()

  button.pack()

  window.mainloop()

def doTheThing(event):
  radio_var.set("")

if __name__ == '__main__':
  main()
