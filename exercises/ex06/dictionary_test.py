"""Test for the dictionary functions created."""

__author__ = "730232367"

from dictionary import invert, favorite_color, count
import pytest


def test_empty_invert() -> None:
    """Test to see if empty dict is returned when given an empty dict."""
    empty_dict: dict[str, str] = {}
    assert invert(empty_dict) == {}


def test_long_dict_invert() -> None:
    """Test to see if the function works properly with sizable list."""
    dict_test: dict[str, str] = {'Nick': 'Miller', 'Jessica': 'Day', 'Winston': 'Bishop', 'Cece': 'Parekh'}
    assert invert(dict_test) == {'Miller': 'Nick', 'Day': 'Jessica', 'Bishop': 'Winston', 'Parekh': 'Cece'}


def test_error_invert() -> None:
    """Test to see if KeyError works."""
    with pytest.raises(KeyError):
        my_dictionary = {'Nick': 'Day', 'Jessica': 'Day', 'Winson': 'Bishop'}
        invert(my_dictionary)


def test_empty_color() -> None:
    """Test to see what color is returned when given an empty list."""
    color_empty: dict[str, str] = {}
    assert favorite_color(color_empty) == ""


def test_fav_color() -> None:
    """Test to see if the favorite color function works."""
    fav_color_dict: dict[str, str] = {'Nick': 'blue', 'Jess': 'yellow', 'Winston': 'brown', 'Schmidt': 'blue', 'Cece': 'purple', 'Aly': 'green'}
    assert favorite_color(fav_color_dict) == 'blue'


def test_tie_color() -> None:
    """Test to see if first value is returned when there is a tie."""
    tie_color: dict[str, str] = {'Nick': 'blue', 'Jess': 'yellow', 'Winston': 'brown', 'Schmidt': 'blue', 'Cece': 'green', 'Aly': 'green'}
    assert favorite_color(tie_color) == 'blue'


def test_empty_count() -> None:
    """Test to see what is returned if given empty list."""
    empty_count_list: list[str] = []
    assert count(empty_count_list) == {}


def test_count() -> None:
    """Test when there is not multiple of the same values."""
    count_list: list[str] = ['Bob', 'Joe', 'Bill']
    assert count(count_list) == {'Bob': 1, 'Joe': 1, 'Bill': 1}


def test_count_multiple() -> None:
    """Test to see if the count function works properly with list of phrases."""
    phrases_list: list[str] = ["hey", "hey", "wow", "no", "hey", "hello", "no"]
    assert count(phrases_list) == {'hey': 3, 'wow': 1, 'no': 2, 'hello': 1}