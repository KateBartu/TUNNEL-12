"""
File: cabin_five.py

Description:
Cabin with the conductor’s locked door. Interaction hints at
the player’s connection to the train.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import main
import cabin_one
import final_cabin


def enter(state):

    if state.get("took_hatch_shortcut"):
        return

    main.display_status(state, 1)
    print("------------------------------------------------------\n"
          "\nCABIN 5\n")
    print("A locked conductor's door blocks the way forward.\n"
          "A small brass plaque reads:\n"
          "AUTHORIZED PERSONNEL ONLY\n")
    print()
    print("A circular slot sits beside the handle.\n"
          "------------------------------------------------------\n")

    choice = main.get_choice(
        "Do you\n"
        "1) Insert the token\n"
        "2) Restart with caution.\n",
        {"1", "2"}
    )

    if choice == "1":

        if "brass_token" in main.inventory:

            print("------------------------------------------------------\n"
                  "\nThe token clicks into place.\n"
                  "The door unlocks with a heavy clunk.\n"
                  "------------------------------------------------------\n")

            state["cabin5_unlocked"] = True
            final_cabin.enter(state)

        else:

            print("------------------------------------------------------\n"
                  "\nToken not found.\n"
                  "------------------------------------------------------\n")
            main.pause("Press enter to continue.\n")
            enter(state)

    else:
        print("------------------------------------------------------\n"
              "\nYou step away from the door.\n"
              "------------------------------------------------------\n")
        state["loop_count"] = max(state.get("loop_count", 1), 4)
        cabin_one.cabin_one4(state)
