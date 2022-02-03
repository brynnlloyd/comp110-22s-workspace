"""EX03 - Wordle - The not so cute version of Wordle."""

__author__ = "730232367"


def contains_char(searched_word: str, single_character: str) -> bool:
    """If single character is found in the word."""
    assert len(single_character) == 1
    alt: int = 0
    character_exist: bool = False
    while alt < len(searched_word) and character_exist is False:
        if searched_word[alt] == single_character:
            character_exist = True
        else:
            alt += 1
    if character_exist is True:
        return True
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """Emoji color coded if letters in guess are in or not in the secret word."""
    assert len(guess) == len(secret_word)
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    store_emoji: str = ""
    while i < len(secret_word):
        if secret_word[i] == guess[i]:
            store_emoji += GREEN_BOX  # if letter i is in secret word i then given green box
        else:
            if contains_char(secret_word, guess[i]) is True:
                store_emoji += YELLOW_BOX
            else:
                store_emoji += WHITE_BOX
        i += 1
    return store_emoji


def input_guess(expected_length: int) -> str:
    """If the guess is the right character length of the word."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = str(input(f"That wasn't {expected_length} chars! Try again: "))
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    user_guess: str = ""
    user_won: bool = False
    turn: int = 1
    while turn <= 6 and user_won is False:
        print(f" === Turn {turn}/6 ===")
        user_guess: str = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess != secret_word:
            turn += 1
        else: 
            user_won = True
    if user_won is True:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()