"""
File: cabin_four.py

Description:
Cabin with Morse code terminal used to unlock the door to Cabin 5.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import main
import cabin_five
import cabin_one
from minigames.morse_puzzle import play

def signal_terminal(state):

    print("\nSIGNAL TERMINAL\n")

    choice = input(
        "1) View incoming signal\n"
        "2) Enter decoded code\n"
        "3) Exit terminal\n")

    if choice == "1":

        # show the signal but do NOT ask for answer
        play(state, view_only = True)
        signal_terminal(state)

    elif choice == "2":
        success = play(state, view_only = False)

        if success:

            print("\nThe keypad flashes green.")
            print("Cabin 5 unlocked.\n")

            state["cabin5_unlocked"] = True
            cabin_five.enter(state)

        else:

            print("\nWrong code, try again.\n")
            signal_terminal(state)

    elif choice == "3":

        enter(state)

    else:

        print("Invalid choice.")
        signal_terminal(state)


def enter(state):

    if state.get("took_hatch_shortcut"):
        return

    main.display_status(state, 1)
    print("\nCABIN 4\n")
    print("The lights flicker.\n"
          "Something moves in the reflection of the window.\n"
          "A heavy metal door blocks the way to the next cabin.\n"
          "Beside it sits a small signal terminal.\n")

    if state.get("cabin5_unlocked"):

        print("The lock light glows green.\n")
        cabin_five.enter(state)
        return

    choice = input("Do you\n"
                   "1) Use the signal terminal\n"
                   "2) Read the old woman's note\n"
                   "3) Investigate the reflection in the window\n")

    if choice == "1":
        signal_terminal(state)

    elif choice == "2":

        if state.get("has_old_woman_paper"):
            read_note(state)
        else:
            print("\nYou don't have anything to read.\n")
            input("Press enter to restart at Cabin One.\n")
            cabin_one.cabin_one3(state)

    elif choice == "3":

        print("\nNothing is there."
              "But the reflection still shows someone standing behind you.\n")
        state["saw_shadow"] = True
        enter(state)

    else:
        print("Invalid choice.")
        enter(state)

def read_note(state):

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
    signal_terminal(state)
