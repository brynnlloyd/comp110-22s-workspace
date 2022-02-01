"""EX03 - Wordle - The not cute version of wordle."""

__author__ = "730232367"

i: int = 0


def contains_char(searched_string: str, single_character: str) -> bool:
    """If single character is found in the string."""
    assert len(single_character) == 1
    if single_character == searched_string[i]:
        return True
    else:
        return False