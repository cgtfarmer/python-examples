from tkinter import *

window = Tk()

greeting = Label(text="---------- Hello, World! ----------")

button1 = Button(text="Button 1")
button2 = Button(text="Button 2")
button3 = Button(text="Button 3")

def main():
  button1.configure(command=printStuff1)
  button2.configure(command=printStuff2)
  button3.configure(command=printStuff3)

  greeting.pack()
  button1.pack()
  button2.pack()
  button3.pack()

  window.mainloop()

def printStuff1():
  print("ABC")

def printStuff2():
  print("DEF")

def printStuff3():
  print("GHI")

if __name__ == '__main__':
  main()
