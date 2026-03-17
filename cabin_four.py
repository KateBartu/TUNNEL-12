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

    while True:
        print("------------------------------------------------------\n"
              "\nSIGNAL TERMINAL\n")
        choice = main.get_choice(
            "1) View incoming signal\n"
            "2) Enter decoded code\n"
            "3) Exit terminal\n",
            {"1", "2", "3"}
        )
        print("------------------------------------------------------\n")

        if choice == "1":
            play(state, view_only=True)

        elif choice == "2":
            success = play(state, view_only=False)

            if success:
                print("------------------------------------------------------\n"
                      "\nThe keypad flashes green.\n"
                      "Cabin 5 unlocked.\n"
                      "------------------------------------------------------\n")

                state["cabin5_unlocked"] = True
                cabin_five.enter(state)
                return

        else:
            enter(state)
            return


def enter(state):

    if state.get("took_hatch_shortcut"):
        return

    main.display_status(state, 1)
    print("------------------------------------------------------\n"
          "\nCABIN 4\n")
    print("The lights flicker.\n"
          "Something moves in the reflection of the window.\n"
          "A heavy metal door blocks the way to the next cabin.\n"
          "Beside it sits a small signal terminal.\n"
          "------------------------------------------------------\n")

    if state.get("cabin5_unlocked"):

        print("------------------------------------------------------\n"
              "The lock light glows green.\n"
              "------------------------------------------------------\n")
        cabin_five.enter(state)
        return

    choice = main.get_choice(
        "Do you\n"
        "1) Use the signal terminal\n"
        "2) Read the old woman's note\n"
        "3) Investigate the reflection in the window\n",
        {"1", "2", "3"}
    )

    if choice == "1":
        signal_terminal(state)

    elif choice == "2":

        if state.get("has_old_woman_paper"):
            read_note(state)
        else:
            print("------------------------------------------------------\n"
                  "\nYou don't have anything to read.\n"
                  "------------------------------------------------------\n")
            main.pause("Press enter to restart at Cabin One.\n")
            state["loop_count"] = max(state.get("loop_count", 1), 3)
            cabin_one.cabin_one3(state)

    else:
        print("------------------------------------------------------\n"
              "\nNothing is there."
              "But the reflection still shows someone standing behind you.\n"
              "------------------------------------------------------\n")
        state["saw_shadow"] = True
        enter(state)


def read_note(state):

    print("------------------------------------------------------\n"
          "\nYou unfold the old woman's paper.\n")

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
    print("------------------------------------------------------\n")
    main.pause("\nPress enter to fold the paper again.\n")
    signal_terminal(state)
