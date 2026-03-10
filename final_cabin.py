"""
File: final_cabin.py

Description:
Control room and final reveal. The player learns the truth
about Tunnel 12 and can break the loop if all conditions are met.

Author: Kate Bartu
Date Created: March 10, 2026
"""

def enter(state, loops):

    print("\nFINAL CABIN\n")
    print("The control room of the train. Dashboard lights flicker.\n")

    if state.get("took_hatch_shortcut"):
            print("The hatch behind you closes, leaving only the control room ahead.\n")

    if state.get("knows_conductor"):

        if state.get("has_old_woman_paper"):
            print("Your hands rest naturally on the controls. You know this room. You know this train.\n")

            if state.get("saw_shadow"):
                print("A fleeting shadow reminds you of earlier warnings.\n")

            if state.get("saw_ticket"):
                print("The ticket in your pocket weighs heavily, reminding you of forgotten choices.\n"
                      "A memory surfaces: A derailment. Tunnel collapsing. Metal screaming against the dark.\n"
                      "You were the conductor. This loop… was your last moment repeating.\n"
                      "The train slows. Tunnel 12 approaches one last time.\nLoop breaks. You are free.\n")
                return True

        else:
            print("You sense familiarity, but something is missing. Perhaps guidance you ignored.\n")
            print("The train plunges into darkness. Everything resets.\n")
        return False

    else:

        print("The controls flicker. Something feels unfinished.\n"
              "The train plunges into darkness. Everything resets.\n")
        return False