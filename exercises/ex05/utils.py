"""Implement function skelektons here."""

__author__ = "730232367"


def only_evens(xs: list[int]) -> list[int]:
    """Return only even numbers from the list."""
    even: list[int] = []
    for num in xs:
        if num % 2 == 0:
            even.append(num)
    return even


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Return a subset of a given list between a and b."""
    subset_list: list[int] = []
    if a < 0:
        a = 0
    if b > len(xs):
        b = len(xs)
    if len(xs) == 0 or a > len(xs) or b <= 0:
        return []
    i: int = a
    while a <= i and i < b:
        subset_list.append(xs[i])
        i += 1
    return subset_list


def concat(a: list[int], b: list[int]) -> list[int]:
    """Concat both lists given."""
    concat_list: list[int] = []
    for i in a:
        concat_list.append(i)
    for i in b:
        concat_list.append(i)
    return concat_list