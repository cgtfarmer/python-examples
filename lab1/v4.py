def main():
    while vote_menu() == "v":
        candidate_menu()

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

def candidate_menu():
    print("--------------------")
    print("CANDIDATE MENU")
    print("--------------------")
    print("1: John")
    print("2. Jane")

    voteFor = int(input("Candidate: "))
    while voteFor != 1 and  voteFor !=2:
        voteFor = int(input("Invalid(1/2): "))

    if voteFor == 1:
        print("Voted John")
    elif voteFor == 2:
        print("Voted Jane")

    return voteFor

if __name__== '__main__':
    main()
