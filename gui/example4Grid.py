import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")

button1 = tk.Button(text="Click me 1")
button2 = tk.Button(text="Click me 2")
button3 = tk.Button(text="Click me 3")

def main():
  greeting.grid(row=0, column=0, columnspan=3, sticky = tk.W+tk.E)

  button1.grid(row=1, column=0)
  button2.grid(row=1, column=1)
  button3.grid(row=1, column=2)

  button1.bind("<Button-1>", thingy1)
  button2.bind("<Button-1>", thingy2)
  button3.bind("<Button-1>", thingy3)

  window.mainloop()

def thingy1(event):
  print("ABC")

def thingy2(event):
  print("DEF")

def thingy3(event):
  print("GHI")

if __name__ == '__main__':
  main()
