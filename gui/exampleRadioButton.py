import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="---------- Hello, World! ----------")

entry = tk.Entry()

radio_var = tk.StringVar()
radioButton1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1", command=None)
radioButton2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2", command=None)
radioButton3 = tk.Radiobutton(window, text="Option 3", variable=radio_var, value="Option 3", command=None)

button = tk.Button(text="Awesome Button")

def main():
  button.bind("<Button-1>", doTheThing)

  greeting.pack()
  entry.pack()
  button.pack()

  radioButton1.pack()
  radioButton2.pack()
  radioButton3.pack()

  window.mainloop()

def doTheThing(event):
  inputValue = entry.get()
  print(f'Hello {inputValue}, how are you today?')

if __name__ == '__main__':
  main()
