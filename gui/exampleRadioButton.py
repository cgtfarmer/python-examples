from tkinter import *

window = Tk()

question = Label(text="Choose your favorite color:")

radioVar = StringVar()
radioButton1 = Radiobutton(window, text="Red", variable=radioVar, value="red")
radioButton2 = Radiobutton(window, text="Green", variable=radioVar, value="green")
radioButton3 = Radiobutton(window, text="Blue", variable=radioVar, value="blue")

button = Button(window, text="Clear")

def main():
  button.configure(command=clearRadioSelection)

  question.pack()

  radioButton1.pack()
  radioButton2.pack()
  radioButton3.pack()

  button.pack()

  window.mainloop()

def clearRadioSelection():
  radioVar.set("")

if __name__ == '__main__':
  main()
