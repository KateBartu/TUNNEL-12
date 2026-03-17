"""
File: cabin_three.py

Description:
Third cabin with environmental damage and a cracked window
reflection hinting at the conductor’s presence.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import cabin_four
import main


def enter(state):

    main.display_status(state, 1)
    print("------------------------------------------------------\n"
          "\nCABIN 3\n")
    print("You step into the next cabin.\n"
          "The lights buzz loudly overhead.\n"
          "Half the seats are overturned.\n"
          "One window is cracked like a spiderweb.\n"
          "The train groans as it moves through the dark.\n"
          "------------------------------------------------------\n")

    choice = main.get_choice(
        "Do you\n"
        "1) Inspect the broken window\n"
        "2) Move to the next cabin\n",
        {"1", "2"}
    )

    if choice == "1":
        broken_window(state)
    else:
        cabin_four.enter(state)


def broken_window(state):

    print("------------------------------------------------------\n"
          "You run your hand along the cracked glass.\n"
          "Cold air leaks through the fracture.\n"
          "Outside, the tunnel wall flashes past inches away.\n"
          "Too close.\n"
          "For a moment you see something reflected in the glass.\n"
          "A man wearing a conductor's cap.\n"
          "You turn around.\n"
          "No one is there.\n"
          "You make towards the doors to Cabin 4.\n"
          "------------------------------------------------------\n")

    state["saw_conductor_reflection"] = True
    state["knows_conductor"] = True
    main.pause("Press enter to continue.")
    cabin_four.enter(state)
