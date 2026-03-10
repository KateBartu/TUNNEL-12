"""
Program Name: Tunnel 12

Description:
Runs the main game loop, manages cabin transitions, and tracks
player state throughout the train and time loops.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import cabin_one
import cabin_two
import cabin_three
import cabin_four
import cabin_five
import final_cabin
from minigames.morse_puzzle import generate_code

loop_count = 1
game_over = False

game_state = {
    "loop_count": 1,
    "knows_about_loop": False,
    "saw_ticket": False,
    "met_smiling_man": False,
    "saw_shadow": False,
    "knows_conductor": False,
    "has_old_woman_paper": False,
    "took_hatch_shortcut": False,
    "picked_up_metal_object": False,
    "has_unlocked": False,
    "morse_code": ""
}

inventory = []


def main():
    global loop_count
    global game_over

    print("=======================")
    print("|      TUNNEL 12      |")
    print("=======================\n")

    player_name = input("Please enter your name: \n")
    print(f"Welcome {player_name}, to Tunnel 12.\n")
    print("The train hums beneath your feet.\n"
          "You don't remember boarding or buying a ticket.\n")

    while not game_over:
        game_state["loop_count"] = loop_count
        game_state["morse_unlocked"] = False

        generate_code(game_state)

    while not game_over:

        game_state["loop_count"] = loop_count

        print("\n" + "=" * 40)
        print("LOOP:", loop_count)
        print("=" * 40)

        if game_state.get("took_hatch_shortcut"):
            game_over = final_cabin.enter(game_state, loop_count)

        else:
            cabin_one.enter(game_state)
            cabin_two.enter(game_state)
            cabin_three.enter(game_state)
            cabin_four.enter(game_state)
            cabin_five.enter(game_state)

            game_over = final_cabin.enter(game_state, loop_count)

        loop_count += 1


if __name__ == "__main__":
    main()

