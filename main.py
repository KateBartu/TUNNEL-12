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

# --------------------------
# GLOBAL INVENTORY
# --------------------------
inventory = []  # shared across all cabins

# --------------------------
# RESET GAME STATE
# --------------------------
def reset_state():
    """Return initial state for a new game loop (does NOT reset inventory)."""
    return {
        "loop_count": 1,
        "saw_ticket": False,
        "saw_shadow": False,
        "knows_conductor": False,
        "has_old_woman_paper": False,
        "took_hatch_shortcut": False,
        "picked_up_metal_object": False,
        "cabin5_unlocked": False,
        "saw_conductor_reflection": False,
        "morse_code": ""
    }

# --------------------------
# DISPLAY HUD
# --------------------------
def display_status(state, cabin):
    """Display loop, cabin number, and current inventory."""
    print("\n" + "=" * 45)
    print(f"LOOP: {state.get('loop_count', 1)} | CABIN: {cabin}")
    if inventory:
        print("INVENTORY:", ", ".join(inventory))
    else:
        print("INVENTORY: empty")
    print("=" * 45 + "\n")

# --------------------------
# HELPER TO PICK UP ITEMS
# --------------------------
def acquire_item(item, state, cabin):
    """Add item to inventory and immediately refresh HUD."""
    if item not in inventory:
        inventory.append(item)
    display_status(state, cabin)

# --------------------------
# MAIN GAME LOOP
# --------------------------
def play_game():
    game_state = reset_state()
    loop_count = 1
    game_over = False

    while not game_over:
        game_state["loop_count"] = loop_count
        generate_code(game_state)

        print("\n" + "=" * 40)
        print("LOOP:", loop_count)
        print("=" * 40)

        if game_state.get("took_hatch_shortcut"):
            # skip cabins if hatch taken
            game_over = final_cabin.enter(game_state, loop_count)
        else:
            cabin_one.enter(game_state)
            cabin_two.enter(game_state)
            cabin_three.enter(game_state)
            cabin_four.enter(game_state)
            cabin_five.enter(game_state)
            game_over = final_cabin.enter(game_state, loop_count)

        loop_count += 1

    replay()

# --------------------------
# REPLAY PROMPT
# --------------------------
def replay():
    choice = input("\nPlay again? (y/n): ").lower()
    if choice == "y":
        inventory.clear()  # clear inventory when starting fresh
        play_game()
    elif choice == "n":
        print("\nThanks for playing Tunnel 12!")
    else:
        print("Invalid choice.")
        replay()

# --------------------------
# MAIN ENTRY
# --------------------------
def main():
    print("=======================")
    print("|      TUNNEL 12      |")
    print("=======================\n")

    name = input("Please enter your name:\n")
    print(f"\nWelcome {name}, to Tunnel 12.\n")

    inventory.clear()  # clear inventory once at game start
    play_game()


if __name__ == "__main__":
    main()
