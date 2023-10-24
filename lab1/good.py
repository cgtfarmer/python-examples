def main():
    john_vote = 0
    jane_vote = 0

    while (vote_menu().strip().lower() != "x"):
        candidate_selection = candidate_menu()

        if candidate_selection == 1:
            john_vote += 1
            print("Voted John")
        elif candidate_selection == 2:
            jane_vote += 1
            print("Voted Jane")

    total_vote = john_vote + jane_vote
    print(f'John - {john_vote}, Jane - {jane_vote}, Total - {total_vote}')

def vote_menu():
    print("--------------------")
    print("VOTE MENU")
    print("--------------------")
    print("v: Vote")
    print("x: Exit")

    decision = input("Option: ")
    while (decision.strip().lower() != "v") and (decision.strip().lower() != "x"):
        decision = input("Invalid (v/x):")

    return decision

def candidate_menu():
    print("--------------------")
    print("CANDIDATE MENU")
    print("--------------------")
    print("1: John")
    print("2: Jane")

    vote_for = int(input("Candidate: "))
    while (vote_for != 1) and (vote_for != 2):
        vote_for = int(input("Invalid (1/2): "))

    return vote_for

if __name__ == '__main__':
    main()
