"""
File: cabin_five.py

Description:
Cabin with the conductor’s locked door. Interaction hints at
the player’s connection to the train.
fart
Author: Kate Bartu
Date Created: March 10, 2026
"""

import main
import cabin_one

def enter(state):

    if state.get("took_hatch_shortcut"):
        return

    main.display_status(state, 1)
    print("\nCABIN 5\n")
    print("A locked conductor's door blocks the way forward.\n"
          "A small brass plaque reads:\n"
          "AUTHORIZED PERSONNEL ONLY\n")

    print("A circular slot sits beside the handle.\n")

    choice = input("Do you\n"
                   "1) Insert the token\n"
                   "2) Restart with caution.\n")

    if choice == "1":

        if "brass_token" in main.inventory:

            print("\nThe token clicks into place.\n"
                  "The door unlocks with a heavy clunk.\n")

            state["cabin5_unlocked"] = True

        else:

            print("\nToken not found.\n")
            input("Press enter to continue.\n")
            enter(state)

    elif choice == "2":

        print("\nYou step away from the door.\n")
        cabin_one.cabin_one4(state)

    else:
        print("Invalid choice.")
        enter(state)
