def Chapter4_intro():
    print("You are racing to go back to the office to analyze the clues you found")
Chapter4_intro()
def fingerprint_check():
    answer = input("Do you want to analyze the finger prints?(y/n)")
    if answer.upper () == 'Y':
        print("After analyzing it turns out that the finger prints were the missing person's")
    else:
        print ("Continue looking through the clues")
fingerprint_check()
def fp_skip():
    fpa = input("Did you find the fingerprints useful enough to move on?(y/n)")
    if fpa.upper() == 'Y':
       print("Move on to chapter 5")
       quit()
    else:
        print("Continue searching through clues.")
fp_skip()
def text_messages():
    answer = input("Would you like to examine the text messages?(y/n)")
    if answer.upper() == "y":
        print("Conversation 1:\n"
              "Best friend: Hey John what's up? \n"
              "John: What's up man getting ready to go to work  \n"
              "Best friend: There's a party going on tomorrow do you want to come? \n"
              "John: Yes I will be there\n"
              "Conversation 2:\n"
              "John: Hey, how have you been? \n"
              "Unknown: Why are you texting me? \n"
              "John: Because I miss you \n"
              "Unknown: Goodbye")
    else:
        print("Keep examining the clues")
text_messages()
def tm_skip():
    tm = input("Did you find the text messages useful enough to move on?(y/n)")
    if tm.upper() == 'Y':
       print("Move on to chapter 5")
       quit()
    else:
        print("Continue searching through clues.")
tm_skip()
def security_footage():
    answer = input("Would you like to examine the security footage?(y/n)")
    if answer.upper() == "y":
        print("You notice John leaving with somebody else.")
    else:
        print("Keep searching")
        print(security_footage())
security_footage()
def Chapter4_end():
    answer = input("Do you want to call mom,best friend, and roommate?(y/n)")
    if answer.upper() == 'Y':
        print("Detective: I need you to come look at something\n"
              "Mom: Ok I am on my way\n"
              "Detective: I need you to come see this\n"
              "roommate: Ok I will be there\n"
              "Detective: I need you to come back to the station\n"
              "Best friend: On my way")
        print("Moving to chapter 5")
    else:
        print('Returning to previous module')
Chapter4_end()
def main():
    Chapter4_intro()
    fingerprint_check()
    fp_skip()
    text_messages()
    tm_skip()
    security_footage()
    Chapter4_end()
main()