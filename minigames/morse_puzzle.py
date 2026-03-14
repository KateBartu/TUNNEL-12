import random
import string
import time

morse_dict = {
"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.",
"G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..",
"M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.",
"S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-",
"Y":"-.--","Z":"--.."
}


def generate_code(state):

    letters = random.sample(string.ascii_uppercase, 4)
    state["morse_code"] = "".join(letters)


def play(state, view_only=False):

    code = state["morse_code"]

    print("\nIncoming signal:\n")

    for letter in code:

        signal = morse_dict[letter]

        for symbol in signal:
            print(symbol, end=" ", flush=True)
            time.sleep(0.3)

        print("   ", end="", flush=True)
        time.sleep(0.5)

    print("\n")

    if view_only:
        input("Press enter to return to the terminal.\n")
        return False

    guess = input("Enter the 4 letter code: ").upper()

    if guess == code:
        return True
    else:
        print("\nWrong code, try again.\n")
        return False