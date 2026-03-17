"""
Program Name: Tunnel 12

Description:
Runs the main game loop, manages cabin transitions, and tracks
player state throughout the train and time loops.

Author: Kate Bartu
Date Created: March 10, 2026
"""

import cabin_one
from minigames.morse_puzzle import generate_code

# --------------------------
# GLOBAL INVENTORY
# --------------------------
inventory = []  # shared across all cabins


# --------------------------
# RESET GAME STATE
# --------------------------
def reset_state():
    """Return initial state for a new game."""
    return {
        "loop_count": 1,
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
# INPUT HELPERS
# --------------------------
def pause(message="Press enter to continue.\n"):
    """Pause until the player presses enter."""
    input(message)


def get_choice(prompt, valid_choices=None, allow_blank=False):
    """
    Get player input and keep asking until it is valid.
    On invalid input, only print an error and ask again.
    """
    while True:
        choice = input(prompt).strip().lower()

        if allow_blank and choice == "":
            return choice

        if valid_choices is None or choice in valid_choices:
            return choice

        print("Invalid choice.")
        prompt = "Try again: "


# --------------------------
# DISPLAY HUD
# --------------------------
def display_status(state, cabin):
    """Display loop and current inventory."""
    print("\n" + "=" * 45)
    print(f"LOOP: {state.get('loop_count', 1)}")
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
# MAIN GAME START
# --------------------------
def play_game():
    game_state = reset_state()
    generate_code(game_state)
    cabin_one.enter(game_state)


# --------------------------
# REPLAY PROMPT
# --------------------------
def replay():
    choice = get_choice("\nPlay again? (y/n): ", {"y", "n"})
    if choice == "y":
        inventory.clear()
        play_game()
    else:
        print("\nThanks for playing Tunnel 12!")


# --------------------------
# MAIN ENTRY
# --------------------------
def main():
    print("=======================")
    print("|      TUNNEL 12      |")
    print("=======================\n")

    name = input("Please enter your name:\n").strip()
    print(f"\nWelcome {name}, to Tunnel 12.\n")

    inventory.clear()
    play_game()


if __name__ == "__main__":
    main()
