from tkinter import *

window = Tk()

greeting = Label(text="---------- Hello, World! ----------")

entry = Entry()

button = Button(text="Awesome Button")

def main():
  button.configure(command=doTheThing)

  greeting.pack()
  entry.pack()
  button.pack()

  window.mainloop()

def doTheThing():
  inputValue = entry.get()
  print(f'Hello {inputValue}, how are you today?')

if __name__ == '__main__':
  main()
