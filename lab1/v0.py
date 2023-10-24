def vote_menu():
    print("--------------------")
    print("VOTE MENU")
    print("--------------------")
    print("v:Vote")
    print("x:Exit")

    decision = input("Option: ")
    while decision != "v" and decision != "x":
        decision = input("Invalid:(v/x)")

    return decision

if __name__ == '__main__':
    vote_menu()
