def Chapter5_intro():
    print("Detective enters the interview room and shares footage of the unknown person to mom")
Chapter5_intro()
print("You found an unknown person in the parking lot security footage")
def mom_interview():
    answer = input("Would you like to interview the mom?(y/n)")
    if answer.upper() == 'Y':
        print("Detective: Do you recognize this person by your son?\n"
              "Mom: No I have never seen them\n"
              "Detective: Do you know if maybe this is a friend or a coworker?\n"
              "Mom: I have no idea\n"
              "Detective: You are free to go")
    else:
        print("Select a different option")
mom_interview()
def roommate_interview():
    answer = input("Would you like to interview the roommate?(y/n)")
    if answer.upper() == 'Y':
        print("Detective: Do you recognize this person by your roommate?\n"
              "Roommate: I think I saw her at the apartment before but never really asked who she was\n"
              "Detective: Do you know her name or who might know her?\n"
              "Roommate: I have no idea\n"
              "Detective: You are free to go")
    else:
        print("Keep interviewing")
roommate_interview()
def bestfriend_interview():
    answer = input("Would you like to interview the best friend?(y/n)")
    if answer.upper() == 'Y':
        print("Detective: Do you recognize this person by your friend?\n"
              "Best friend: yes she looks familiar but I can't remember\n"
              "Detective: Maybe this zoomed in picture will help\n"
              "Best friend: Oh yeah that is his ex she probably forced him to go with her \n"
              "Detective: Do you know where she might be or where she lives?\n"
              "Best friend: Yes she lives 3 blocks away from me\n"
              "Detective: Maybe she knows something")
    else:
        print("Select a different option")
        print(mom_interview())
bestfriend_interview()
def Chapter5_end
    print("Good job detective you got closer to solving the case\n"
          "be sure to continue on the next adventure.")
    quit()
Chapter5_end()
def main():
    Chapter5_intro()
    mom_interview()
    roommate_interview()
    bestfriend_interview()
    Chapter5_end()