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
    print("\nFINAL CABIN\n")
    main.display_status(state, "Final Cabin")
    print("The control room of the train. Dashboard lights flicker.\n")

    # If player took the hatch shortcut
    if state.get("took_hatch_shortcut"):
        print("The hatch behind you closes, leaving only the control room ahead.\n")

    # Determine endings based on player actions
    endings = []

    if state.get("knows_conductor"):
        endings.append("You feel at home behind the controls, knowing the train intimately.\n")

    if state.get("has_old_woman_paper"):
        endings.append("The note from the old woman rests in your hand.\n")

    if state.get("saw_shadow"):
        endings.append("A fleeting shadow reminds you of warnings you once ignored.\n")

    if state.get("saw_ticket"):
        endings.append(
            "The ticket in your pocket weighs heavily, reminding you of forgotten choices.\n"
            "A memory surfaces: A derailment. Tunnel collapsing. Metal screaming against the dark.\n"
            "You were the conductor. This loop… was your last moment repeating.\n"
        )

    # If the player has all key flags, break the loop
    if state.get("has_old_woman_paper") and state.get("saw_ticket") and state.get("knows_conductor"):
        endings.append("The train slows. Tunnel 12 approaches one last time.\nLoop breaks. You are free.\n")
        for msg in endings:
            print(msg)
        main.replay()
        return True

    # Otherwise, show partial ending and reset
    if endings:
        for msg in endings:
            print(msg)
        print("The controls flicker. Something feels unfinished.\n")
        print("The train plunges into darkness. Everything resets.\n")
    else:
        print("The controls flicker uncertainly. You feel lost.\n")
        print("The train plunges into darkness. Everything resets.\n")

    # Prompt for restart or exit
    main.replay()
    return False
