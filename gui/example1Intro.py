import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="---------- Hello, World! ----------")

button = tk.Button(text="Awesome Button")

def main():
  greeting.pack()
  button.pack()

  window.mainloop()

if __name__ == '__main__':
  main()
