def main():
    while vote_menu() == "v":
        print(candidate_menu())

def vote_menu():
    print("--------------------")
    print("VOTE MENU")
    print("--------------------")

    decision = input("v:Vote\nx:Exit\nOption: ").strip().lower()
    while decision != "v" and decision != "x":
        decision = input("Invalid:(v/x) ")
        decision = decision.strip().lower()
    return decision

def candidate_menu():
    print("--------------------")
    print("CANDIDATE MENU")
    print("--------------------")

    voteFor = int(input("1.John\n2.Jane\nCandidate: "))
    while voteFor != 1 and  voteFor !=2:
        voteFor = int(input("Invalid(1/2): "))

    if voteFor == 1:
        print("Voted John")
    elif voteFor == 2:
        print("Voted Jane")
    return voteFor

if __name__== '__main__':
    main()
