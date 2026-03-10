"""
File: cabin_three.py

Description:
Third cabin with environmental damage and a cracked window
reflection hinting at the conductor’s presence.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import cabin_four

def enter(state):

    print("\nCABIN 3\n")

    print("You step into the next cabin.\n"
          "The lights buzz loudly overhead.\n"
          "Half the seats are overturned.\n"
          "One window is cracked like a spiderweb.\n"
          "The train groans as it moves through the dark.\n")

    close = input("Do you want to close the cabin door behind you?\n"
                  "Yes/No   (y) or (n)\n")
    if close.lower() == "y":
        print("\nYou close the cabin door behind you.")

    elif close.lower() == "n":
        print("\nYou leave the cabin door open.")

    choice = input("Do you\n"
                   "1) Inspect the broken window\n"
                   "2) Move to the next cabin\n")

    if choice == "1":
        broken_window(state)

    elif choice == "2":
        cabin_four.enter(state)

    else:
        print("Invalid choice.")


def broken_window(state):

    print("\nYou run your hand along the cracked glass.\n"
          "Cold air leaks through the fracture.\n"
          "Outside, the tunnel wall flashes past inches away.\n"
          "Too close.\n"
          "For a moment you see something reflected in the glass.\n"
          "A man wearing a conductor's cap.\n"
          "You turn around.\n"
          "No one is there.\n"
          "You make towards the doors to Cabin 4.")

    state["saw_conductor_reflection"] = True
    input("Press enter to continue.")
    cabin_four.enter(state)