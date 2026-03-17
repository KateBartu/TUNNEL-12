"""
File: final_cabin.py

Description:
Control room and final reveal. Ending depends on which actions the player
took in previous cabins. Player can choose to restart or exit at the end.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import main

def enter(state):
    print("------------------------------------------------------\n"
          "\nFINAL CABIN\n")
    main.display_status(state, "Final Cabin")
    print("The control room of the train. Dashboard lights flicker.\n"
          "An eerie silence fills the cabin.\n"
          "A concerningly familiar feeling creeps upon you.\n"
          "------------------------------------------------------\n")

    # If player took the hatch shortcut
    if state.get("took_hatch_shortcut"):
        print("------------------------------------------------------\n"
              "The hatch behind you closes, leaving only the control room ahead.\n"
              "------------------------------------------------------\n")

    # Determine endings based on player actions
    endings = []

    if state.get("knows_conductor"):
        endings.append(
            "You settle into the conductor’s seat.\n"
            "Your hands move instinctively across the controls.\n"
            "Every lever, every dial... you know them.\n"
            "You don’t remember learning. Only that you already did.\n"
        )

    if state.get("has_old_woman_paper"):
        endings.append(
            "The paper trembles in your hand.\n"
            "The old woman’s words no longer feel cryptic.\n"
            "They feel like instructions you wrote for yourself.\n"
            "A memory claws its way back: steel bending, tunnel collapsing, time folding inward.\n"
        )

    if state.get("saw_conductor_reflection"):
        endings.append(
            "You glance at the darkened glass of the control panel.\n"
            "The reflection staring back isn’t just you.\n"
            "It’s someone who has done this before.\n"
            "Many times.\n"
        )

    if state.get("saw_shadow"):
        endings.append(
            "Something shifts in the corner of your vision.\n"
            "That same shadow from before.\n"
            "Not following you... waiting for you to catch up.\n"
        )

    if state.get("picked_up_metal_object"):
        endings.append(
            "The weight of the metal object in your pocket feels significant.\n"
            "Not random. Not lost.\n"
            "Placed.\n"
            "A tool... or a mistake.\n"
        )

    if state.get("cabin5_unlocked"):
        endings.append(
            "You remember forcing something open.\n"
            "Breaking a path that wasn’t meant to be taken.\n"
            "The train didn’t stop you.\n"
            "It never does.\n"
        )

    # True ending
    if (state.get("has_old_woman_paper")
            and state.get("saw_conductor_reflection")
            and state.get("knows_conductor")):

        endings.append(
            "Everything aligns.\n"
            "The memories. The warnings. The role you tried to forget.\n\n"
            "You were the conductor.\n"
            "And this loop... was never a prison.\n"
            "It was a delay.\n\n"
            "A second chance.\n"
        )

        endings.append(
            "The train begins to slow.\n"
            "Tunnel 12 approaches, no longer endless.\n"
            "The darkness ahead feels different.\n"
            "Not a reset.\n"
            "An exit.\n\n"
            "The loop breaks.\n"
        )

        for msg in endings:
            print(msg)

        main.replay()
        return True

    # Partial ending and reset
    if endings:
        for msg in endings:
            print(msg)

        print("The controls flicker, resisting your touch.\n"
              "You’re close... but not complete.\n")
        print("The train plunges into darkness.\n"
              "The loop tightens its grip.\n")
    else:
        print("You stare at the controls, waiting for recognition.\n"
              "Nothing comes.\n")
        print("The train doesn’t slow.\n"
              "It never intended to.\n")
        print("Darkness swallows the cabin.\n"
              "Everything resets.\n")

    # Prompt for restart or exit
    main.replay()
    return False
