from tkinter import *

window = Tk()
frame = Frame(master=window)

greeting = Label(master=frame, text="Hello, Tkinter")

button1 = Button(master=frame, text="Click me 1")
button2 = Button(master=frame, text="Click me 2")
button3 = Button(master=frame, text="Click me 3")

def main():
  frame.grid(row=0, column=0)

  greeting.grid(row=0, column=0, columnspan=3, sticky=W+E)

  button1.grid(row=1, column=0)
  button2.grid(row=1, column=1)
  button3.grid(row=1, column=2)

  button1.configure(command=thingy1)
  button2.configure(command=thingy2)
  button3.configure(command=thingy3)

  window.mainloop()

def thingy1():
  print("ABC")

def thingy2():
  print("DEF")

def thingy3():
  print("GHI")

if __name__ == '__main__':
  main()
