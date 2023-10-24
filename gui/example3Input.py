import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="---------- Hello, World! ----------")

entry = tk.Entry()

button = tk.Button(text="Awesome Button")

def main():
  button.bind("<Button-1>", doTheThing)

  greeting.pack()
  entry.pack()
  button.pack()

  window.mainloop()

def doTheThing(event):
  inputValue = entry.get()
  print(f'Hello {inputValue}, how are you today?')

if __name__ == '__main__':
  main()
