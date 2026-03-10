"""
File: cabin_four.py

Description:
Cabin with minigame to unlock door to cabin 5 and reflection of shadow

Author: Kate Bartu
Date Created: March 10, 2026
"""

import cabin_five
from minigames.morse_puzzle import play


def read_note():

    print("\nYou unfold the old woman's paper.\n")
    print("""
    ===================================
          METRO SIGNAL REFERENCE

          MORSE TRANSLATION TABLE

           A : .-        N : -.
           B : -...      O : ---
           C : -.-.      P : .--.
           D : -..       Q : --.-
           E : .         R : .-.
           F : ..-.      S : ...
           G : --.       T : -
           H : ....      U : ..-
           I : ..        V : ...-
           J : .---      W : .--
           K : -.-       X : -..-
           L : .-..      Y : -.--
           M : --        Z : --..

    ===================================
    """)

    input("\nPress enter to fold the paper again.\n")


def enter(state):

    if state.get("took_hatch_shortcut"):
        return

    print("\nCABIN 4\n")
    print("The lights flicker.\n"
          "Something moves in the reflection of the window.\n")

    choice = input("Do you:\n"
                   "1) Turn around\n"
                   "2) Ignore it\n")

    if choice == "1":
        print("\nNothing is there."
              "But the reflection still shows someone standing behind you.\n")
        state["saw_shadow"] = True

    else:
        print("\nYou keep your eyes forward.\n"
              "You move toward the door leading to the next cabin.\n"
              "It's locked.\n"
              "Beside the handle is a small signal terminal.\n")

    if state.get("cabin5_unlocked"):
        print("The lock light glows green.\n")
        cabin_five.enter(state)
        return


    choice = input("Do you\n"
                   "1) Attempt to decode the signal\n"
                   "2) Read the old woman's note\n"
                   "3) Step away\n")

    if choice == "1":

        success = play(state)

        if success:
            print("\nThe keypad flashes green.")
            print("The lock releases with a heavy clunk.\n")

            state["cabin5_unlocked"] = True
            cabin_five.enter(state)

        else:
            print("\nThe signal fails.")
            print("The lights flicker violently.\n")

            input("Press enter as the train shudders...\n")

    elif choice == "2":

        if state.get("has_old_woman_paper"):
            read_note()
        else:
            print("\nYou don't have anything to read.\n")

        enter(state)

    else:

        print("\nYou step away from the door.\n")