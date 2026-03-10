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
    """
    Generates a new 4-letter code at the start of each loop
    """
    letters = random.sample(string.ascii_uppercase, 4)
    state["morse_code"] = "".join(letters)


def play(state):

    code = state["morse_code"]

    print("\nSIGNAL TELEGRAPH ONLINE\n")
    print("Incoming signal:\n")

    # print morse slowly like a telegraph
    for letter in code:

        signal = morse_dict[letter]

        for symbol in signal:
            print(symbol, end="", flush=True)
            time.sleep(0.3)

        print()
        time.sleep(0.4)

    guess = input("\nEnter the 4 letter code: ").upper()

    if guess == code:
        return True
    else:
        return False