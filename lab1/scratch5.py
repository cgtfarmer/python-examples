
def main():
    print("Hello, World!")

    print(getStuff())

    result = getStuff()

    print(result)

    result = getStuff()

    newResult = result + " and things"

    print(newResult)

def getStuff():
   return "Stuff"

if __name__ == '__main__':
    main()

# def getAnswer():
#   selection = input("Gimme stuff: ")

#   return selection
