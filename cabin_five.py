"""
File: cabin_five.py

Description:
Cabin with the conductor’s locked door. Interaction hints at
the player’s connection to the train.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import main
import cabin_two
import final_cabin

def enter(state):

    if state.get("took_hatch_shortcut"):
        return

    print("\nCABIN 5\n")
    print("A locked conductor's door blocks the way forward.\n"
        "A small brass plaque reads:\n"
        "AUTHORIZED PERSONNEL ONLY\n")

    if "brass_token" in main.inventory:
        print("The circular indentation beside the door matches the token from the man in the gray coat.")
        choice = input("Do you\n"
                       "1) Insert the token\n"
                       "2) Step away\n")

        if choice == "1":
            print("The token clicks into place.\n"
                  "The door unlocks with a heavy clunk\n")
            final_cabin.enter({}, main.loop_count)

        else:
            print("You hesitate.")
            state["loop_count"] = state.get("loop_count", 1) + 1
            final_cabin.enter({}, main.loop_count)

    else:
        print("The door us locked.\n"
              "A circular slot sits beside the handle.\n")
        input("Press enter to continue.\n")
        state["loop_count"] = state.get("loop_count", 1) + 1
        cabin_two.enter(state)