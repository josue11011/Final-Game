def Chapter1_intro():
    print("You are getting put of your car and as you get out of your car you receive a phone call")
Chapter1_intro()
def phone_call():
    answer = input ("Your phone is ringing would you like to answer? (y/n)")
    if answer.upper() == 'Y':
        print("Detective we have a call about a missing person we need you to go to their house")
    else:
        print("You may return to menu")
phone_call()
def player_travel():
     answer = input ("Would you like to travel to the house?")
     if answer.upper() == 'Y':
         print("you are now traveling to the house")
     else:
         print("you are now traveling back to the station")
player_travel()
def house():
    print("you have searched the house and found something under the couch")
    answer=input("Did you find the phone?(y/n)")
    if answer.upper() == 'Y':
        print("Let's call the mom, best friend and room mate")
        print("Detetive: Hello, Mom I need to interview you about your missing son \n"
              "Mom: Yes I will be on my way\n"
              "Detetive: Hello, I need to interview you about your missing roommate\n"
              "Roommate: Yes I will be on my way\n"
              "Detective: Hello, I need to interview you about your missing best friend\n"
              "Best Friend: Ok I will be there")
    else:
        print("Keep searching")
house()
def Chapter1_end():
    answer=input("Do you want to go back to the station?(y/n)")
    if answer.upper() == 'Y':
        print("Moving to chapter 2")
    else:
        print('Returning to previous module')
Chapter1_end()
def main():
    Chapter1_intro()
    phone_call()
    player_travel()
    house()
    Chapter1_end()
main()

