"""Implement function skelektons for dictionaries exercise."""

__author__ = "730232367"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values in a given dictionary."""
    inv_dict: dict[str, str] = {}
    for key in a:
        inv_dict[a[key]] = key
    if len(inv_dict) != len(a):
        raise KeyError("One to many of the same keys")
    return inv_dict


def favorite_color(name: dict[str, str]) -> str:
    """Figuring out what is the most common favorite color from a dictionary."""
    color_list: list[str] = []
    # counts = count(color_list)
    count: dict[str, int] = {}
    for key in name:
        color_list.append(name[key])
    for color in color_list:
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
    # print(count)
    color = ""
    max: int = 0
    for key in count:
        if max < count[key]:
            max = count[key]
            color = key
    return color


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times an item appears in a dict."""
    count_dict: dict[str, int] = {}
    for item in a:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict