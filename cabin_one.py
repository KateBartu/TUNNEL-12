"""
File: cabin_one.py

Description:
Handles the first cabin, introduces the time loop mechanic,
the old woman, and the roof hatch shortcut.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import cabin_two
import main
import final_cabin


def enter(state):
    if state.get("loop_count", 1) == 1:
        first_loop(state)
    elif state.get("loop_count", 1) == 2:
        cabin_one2(state)
    elif state.get("loop_count", 1) == 3:
        cabin_one3(state)
    else:
        cabin_one4(state)


# ================= FIRST LOOP ================= #

def first_loop(state):

    main.display_status(state, 1)
    print("------------------------------------------------------\n"
          "\nCABIN 1\n")
    print("The train hums beneath your feet.\n"
          "The map above the door reads: NEXT STOP - TUNNEL 12\n"
          "You don't remember boarding\n"
          "You don't even remember buying a ticket.\n"
          "The intercom crackles, 'Thank you for choosing TriMet Transit, we pride ourselves on the saf-'\n"
          "Static.\n"
          "An old woman across from you stares.\n"
          "'You're early', she snarks.\n"
          "You look up at the time displayed above the door.\n"
          "8:07pm\n"
          "Befuddled, you stand up.\n"
          "------------------------------------------------------\n")

    choice = main.get_choice(
        "Do you\n"
        "1) look around.\n"
        "2) charge ahead to the next cabin.\n",
        {"1", "2"}
    )

    if choice == "1":
        option_1(state)
    else:
        cabin_two.enter(state)


# ================= SECOND LOOP ================= #

def cabin_one2(state):

    main.display_status(state, 1)
    print("------------------------------------------------------\n"
          "\nCABIN 1\n")
    print("The train hums beneath your feet.\n"
          "The map above the door reads: NEXT STOP - TUNNEL 12\n"
          "The intercom crackles, 'Thank you for choosing TriMet Transit-'\n"
          "What the f***? Wasn't I just here?\n"
          "You check the time.\n"
          "8:07pm\n"
          "------------------------------------------------------\n")

    choice = main.get_choice(
        "Do you\n"
        "1) Ask the old lady, 'Where are we going?'\n"
        "2) charge ahead to the next cabin.\n",
        {"1", "2"}
    )

    if choice == "1":
        option_3(state)
    else:
        cabin_two.enter(state)


# ================= THIRD LOOP ================= #

def cabin_one3(state):

    main.display_status(state, 1)
    print("------------------------------------------------------\n"
          "\nCABIN 1\n")
    print("The train hums beneath your feet.\n"
          "Back in cabin 1? No way - it can't be...\n"
          "Nobody is here.\n"
          "'...passenger disturbance in Cabin Two...' The intercom crackles\n"
          "'...please remain calm...'\n"
          "'...this train will be stopping shortly...'\n"
          "------------------------------------------------------\n")

    choice = main.get_choice(
        "Do you\n"
        "1) Rush back to Cabin Two\n"
        "2) Try to talk to the lady one more time\n",
        {"1", "2"}
    )

    if choice == "1":
        cabin_two.enter(state)
    else:
        option_retalk(state)


def option_retalk(state):

    print("------------------------------------------------------\n"
          "You walk up to the old lady.\n"
          "She suddenly grabs your sleeve and presses a small folded piece of paper into your hand.\n"
          "'Take it,' she says.\n"
          "You look at it. Blank on the outside.\n"
          "“What is it?” you ask.\n"
          "“Don’t open it,” she says quickly.\n"
          "'Then why give it to me?'\n"
          "She glances toward the dark window.\n"
          "'Open it only if you’re in real trouble.'\n"
          "She lets go of your sleeve.\n"
          "'And not before.' she warns with a stern look. \n"
          "You pocket the paper.\n"
          "------------------------------------------------------\n")
    state["has_old_woman_paper"] = True
    main.acquire_item("old woman's note", state, 1)

    main.pause("Press enter to continue to Cabin 2.\n")
    cabin_two.enter(state)


# ================= FOURTH LOOP shortcut =================

def cabin_one4(state):

    main.display_status(state, 1)
    print("------------------------------------------------------\n"
          "\nCABIN 1\n")
    print("The train hums beneath your feet.\n"
          "Back again. You think to yourself.\n"
          "You look above you and notice a hatch glows faintly of an outside light.\n")
    main.pause("Press enter to go through the hatch.\n")
    print("You climb on top of the chairs and lift yourself through the hatch and onto the roof.\n"
          "There's enough room to stand as the train.\n "
          "You can see all the way out to the very front cabin.\n"
          "I'm sure if you're careful you could make it!\n"
          "------------------------------------------------------\n")
    state["took_hatch_shortcut"] = True
    final_cabin.enter(state)


# ================= OPTION A ================= #

def option_1(state):

    print("------------------------------------------------------\n"
          "The route map flickers between stations too fast to read.\n"
          "Every advertisement features the same smiling man.\n"
          "A hatch on the roof, slightly open, letting in the heavy sound of the tracks.\n"
          "The windows show only darkness.\n"
          "A forgotten coffee cup on the seat beside you. It’s warm.\n"
          "------------------------------------------------------\n")

    sub_choice = main.get_choice(
        "Do you\n"
        "1) keep looking\n"
        "2) Move onto the next cabin.\n",
        {"1", "2"}
    )

    if sub_choice == "1":
        option_11(state)
    else:
        cabin_two.enter(state)


# ================= OPTION A1 =================

def option_11(state):

    print("------------------------------------------------------\n"
          "You've looked long enough and you realize,\n"
          "No one else is blinking.\n"
          "Not the old lady.\n"
          "Not the man gripping the pole.\n"
          "Not the teenager with headphones.\n"
          "When you make eye contact with one of them, they blink in unison.\n"
          "All of them.\n"
          "Then the intercom whispers your name from the cabin beyond.\n"
          "------------------------------------------------------\n")

    sub_choice = main.get_choice(
        "Do you\n"
        "1) get as fast as you can out of cabin 1.\n"
        "2) Ask 'How do they know my name?'\n",
        {"1", "2"}
    )

    if sub_choice == "1":
        cabin_two.enter(state)

    else:
        print("------------------------------------------------------\n"
              "Your voice cracks as you ask the question.\n"
              "'How do they know my name?'\n"
              "The old woman smiles.\n"
              "'Because you've asked before.'\n"
              "The teenager slowly removes his headphones.\n"
              "The man at the pole turns toward you.\n"
              "The smiling man from the advertisements is now standing in the aisle.\n"
              "You don't remember him standing up.\n"
              "The lights flicker.\n"
              "Everything goes dark.\n"
              "The hum never stops.\n"
              "------------------------------------------------------\n")
        state["loop_count"] = 2
        cabin_one2(state)


# ================= OPTION C =================

def option_3(state):

    print("------------------------------------------------------\n"
          "Where are we going? You ask the lady.\n"
          "She doesn’t answer immediately.\n"
          "She studies you like someone remembering a dream.\n"
          "Then she says:\n"
          "Tunnel 12.\n"
          "We always go to Tunnel 12.\n"
          "'What happens then?' You ask.\n"
          "Her voice softens.\n"
          "'You always forget that part.'\n"
          "The lights flicker.\n"
          "For half a second.\n"
          "------------------------------------------------------\n")

    main.pause("Press enter to continue.\n")
    current_loop = state.get("loop_count", 1)

    if current_loop <= 1:
        state["loop_count"] = 2
        cabin_one2(state)
    else:
        state["loop_count"] = 3
        cabin_one3(state)
