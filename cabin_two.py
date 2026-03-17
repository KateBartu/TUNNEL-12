"""
File: cabin_two.py

Description:
Second cabin where the player meets the man in the gray coat
and discovers early clues about the train's mystery.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import cabin_one
import cabin_three
import main


def enter(state):

    if state.get("took_hatch_shortcut"):
        return

    main.display_status(state, 1)
    print("------------------------------------------------------\n"
          "\nCABIN 2\n")
    print("You step into Cabin 2.\n"
          "The lighting is harsher here.\n"
          "The seats are empty.\n"
          "At the far end, a man in a gray coat checks his watch.\n"
          "Above the door, the time reads: 8:13pm.\n"
          "------------------------------------------------------\n")

    choice = main.get_choice(
        "Do you\n"
        "1) Watch the man\n"
        "2) Look around the cabin\n",
        {"1", "2"}
    )

    if choice == "1":
        watch_man(state)
    else:
        look_around_cabin_two(state)


def watch_man(state):
    print("------------------------------------------------------\n"
          "You keep your eyes on him.\n"
          "8:14pm.\n"
          "His hand slips."
          "Something metallic hits the floor."
          "It rolls beneath a seat.\n"
          "------------------------------------------------------\n")

    choice = main.get_choice(
        "Do you\n"
        "1) Dive for it\n"
        "2) Hesitate\n",
        {"1", "2"}
    )

    if choice == "1":
        print("------------------------------------------------------\n"
              "You drop to the floor.\n"
              "Your fingers brush metal—\n"
              "The lights cut out.\n"
              "The train lurches violently.\n"
              "Everything goes black.\n"
              "You clutch onto the metal object and stand bold upright.\n"
              "When the lights flicker back on, you're all alone in the cabin once more.\n"
              "You look at the object in your hand, It's a small brass transit token.\n"
              "------------------------------------------------------\n")
        state["picked_up_metal_object"] = True
        state["saw_ticket"] = True

        if "brass_token" not in main.inventory:
            main.inventory.append("brass_token")
        main.display_status(state, 2)

        main.pause("Press enter to continue to Cabin 3\n")
        cabin_three.enter(state)

    else:
        print("------------------------------------------------------\n"
              "You freeze.\n"
              "The man slowly looks at you.\n"
              "'Too late,' he says.\n"
              "The lights flicker.\n"
              "The world folds inward.\n"
              "------------------------------------------------------\n")
        state["loop_count"] = max(state.get("loop_count", 1), 3)
        cabin_one.cabin_one3(state)


# ---------------- OPTION 2 ---------------- #

def look_around_cabin_two(state):

    print("------------------------------------------------------\n"
          "The advertisements here are different.\n"
          "Every screen displays a smiling man.\n"
          "Below his face reads:\n"
          "'Consistency is comfort.'\n"
          "There is an open door at the far end of the cabin."
          "------------------------------------------------------\n")
    main.pause("Press enter to continue\n")
    cabin_three.enter(state)
