"""EX02 - Chardle - The next cute step in Wordle building."""

__author__ = "730232367"

secret_word: str = "python"
length_secret_word: int = len(secret_word)
guess: str = input(f"What is your {length_secret_word}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input(f"That was not {length_secret_word} letters! Try again: ")


i: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

store_emoji: str = ""

while i < length_secret_word: 
    if secret_word[i] == guess[i]:
        store_emoji = store_emoji + GREEN_BOX 
    else: 
        character_exist: bool = False
        alt: int = 0
        while alt < length_secret_word and character_exist is False:
            if secret_word[alt] == guess[i]:
                character_exist = True
            else:
                alt = alt + 1
        if character_exist is True:
            store_emoji = store_emoji + YELLOW_BOX 
        else:
            store_emoji = store_emoji + WHITE_BOX 
    i = i + 1

print(store_emoji)

if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")