import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="---------- Hello, World! ----------")

button = tk.Button(text="Awesome Button")

def main():
  button.bind("<Button-1>", printStuff1)
  button.bind("<Button-2>", printStuff2)
  button.bind("<Button-3>", printStuff3)

  greeting.pack()
  button.pack()

  window.mainloop()

def printStuff1(event):
  print("You clicked with your left mouse button")

def printStuff2(event):
  print("You clicked with your middle mouse button")

def printStuff3(event):
  print("You clicked with your right mouse button")

if __name__ == '__main__':
  main()
