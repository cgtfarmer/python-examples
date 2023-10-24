import tkinter as tk

def main():
  window = tk.Tk()

  greeting = tk.Label(text="Hello, Tkinter")
  greeting.grid(row=0, column=0, columnspan=3, sticky = tk.W+tk.E)

  button1 = tk.Button(text="First")
  button1.grid(row=1, column=0)
  button1.bind("<Button-1>", printStuff1)

  button2 = tk.Button(text="Second")
  button2.grid(row=1, column=1)
  button2.bind("<Button-1>", printStuff2)

  button3 = tk.Button(text="Third")
  button3.grid(row=1, column=2)
  button3.bind("<Button-1>", printStuff3)

  window.mainloop()

def printStuff1(event):
  print("ABC")

def printStuff2(event):
  print("DEF")

def printStuff3(event):
  print("GHI")

if __name__ == '__main__':
  main()
