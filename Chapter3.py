def Chapter3_intro():
    print("After finding out where the person works you now arrive at the work place.")
Chapter3_intro()
def security_interview():
    answer = input("You now see the security guard of the store do you want to interview them?(y/n)")
    if answer.upper() == 'Y':
        print("Detective: Hello sir, we are looking for this missing person do you recognize him?\n"
              "Security: He looks familiar I believe he was working the register last night.\n"
              "Detective: Do you remember around what time he left?\n"
              "Security: I am not sure but I remember seeing him last around 8 PM.\n"
              "Detective: Can we access your security cameras?\n"
              "Security: Yes follow me\n"
              "As you are reviewing footage you see them leave with someone in the parking lot\n"
              "Detective: I am going to need a copy of this")
    else:
        print("Choosing a different action")
security_interview()
def satisfied_interview():
    answer = input("Are you satisfied with the interview?(y/n)")
    if answer.upper() == 'Y':
        print("You are now leaving the back room.")
    else:
        print ("Replaying Security interview")
        print(security_interview())
satisfied_interview()
def coworker_interview():
    answer = input("As you leave the back room you see a coworker do you want to interview them?(y/n)")
    if answer.upper() == 'Y':
        print("Detective: Good afternoon, we are looking for this person do you recognize him?\n"
              "Coworker: Yes I know him that is John, is everything ok?.\n"
              "Detective: He is missing and we need to find him, when was the last time you saw him?\n"
              "Coworker: We actually had a shift together last night and I said bye to him.\n"
              "Detective: Do you know where he went after?\n"
              "Coworker: I have no idea I left and he went to his car\n"
              "Detective: Do you recognize this person by chance?\n"
              "Coworker: I have no idea who that is\n"
              "Detective: Thank you for your time.")
    else:
        print("Choosing a different action")
coworker_interview()
def satisfied_interview2():
    answer = input("Are you satisfied with the interview?(y/n)")
    if answer.upper() == 'Y':
        print("Continue to parking lot")
    else:
        print ("Replaying Coworker interview")
        print(coworker_interview())
satisfied_interview2()
def search_car():
    answer = input("You have now found John's car would you like to search it?(y/n)")
    if answer.upper() == 'Y':
        fp = input("There are some fingerprints on the window would you like to collect them?(y/n)")
        if fp.upper() == 'Y':
            print("Detective: Let me collect these fingerprints for testing\n"
                  "As you are collecting the fingerprints you notice some keys")
        else:
            print("Continue searching.")
            print(search_car())
    keys = input("Would you like to collect the keys in the car?")
    if keys.upper() == 'Y':
        print("You put the keys in a bag and are now ready to go")
    else:
        print("Continue searching")
        print(search_car())
search_car()
def Chapter3_end():
    answer = input("Did you find all the clues?(y/n)")
    if answer.upper() == 'Y':
        print("Moving to chapter 4")
    else:
        print('Returning to previous module')
Chapter3_end()
def main():
    Chapter3_intro()
    security_interview()
    satisfied_interview()
    coworker_interview()
    satisfied_interview2()
    search_car()
    Chapter3_end()
main()