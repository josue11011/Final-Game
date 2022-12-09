def Chapter2_intro():
    print("Everyone has arrived to the station and you are ready to start interviewing")
Chapter2_intro()
def mom_interview():
    answer = input("Do you want to interview the mom?(y/n)")
    if answer.upper() == 'Y':
        print("Detective: Hello, we received a call that your son is missing do you have an idea where he might be?\n"
              "Mom: I have no idea he does not live with me anymore.\n"
              "Detective: When was the last time you talked to him?\n"
              "Mom: The las time I talked to him was about a week ago?\n"
              "Detective: Do you have any idea where he might be at?\n"
              "Mom: I have no idea maybe someone at work knows\n"
              "Detective: Thank you, you are free to go")
    else:
        print("Choosing a different action")
mom_interview()
def bestfriend_interview():
    answer = input("Do you want to interview the best friend?(y/n)")
    if answer.upper() == 'Y':
        print("Detective: Hello, we received a call that your best friend is missing do you have an idea where he might be?\n"
              "Best friend: The last time i talked to him he said he was going to work.\n"
              "Detective: When was the last time you talked to him?\n"
              "Best friend: The las time I talked to him was yesterday before he went to work.\n"
              "Detective: Where does he work at?\n"
              "Best friend: He works at a grocery store named Wells 2 block from his house.\n"
              "Detective: Thank you, you are free to go")
    else:
        print("Choosing a different action")
bestfriend_interview()
def roommate_interview():
    answer = input("Do you want to interview the roommate?(y/n)")
    if answer.upper() == 'Y':
        print(
            "Detective: Hello, we received a call that your roommate is missing do you have an idea where he might be?\n"
            "Roommate: I have no idea we got into an argument I haven't really talked to him.\n"
            "Detective: When was the last time you talked to him?\n"
            "Roommate: The las time I talked to him was probably like 3 days ago.\n"
            "Detective: Was he ever with someone you thought was suspicious\n"
            "Roommate: Not that I know of, can I go now?\n"
            "Detective: Thank you, you are free to go")
    else:
        print("Choosing a different action")
roommate_interview()
def Chapter2_end():
    answer = input("Do you want to travel to their job?(y/n)")
    if answer.upper() == 'Y':
        print("Moving to chapter 3")
    else:
        print('Returning to previous module')
Chapter2_end()
def main ():
    Chapter2_intro()
    mom_interview()
    roommate_interview()
    bestfriend_interview()
    Chapter2_end()
main()
