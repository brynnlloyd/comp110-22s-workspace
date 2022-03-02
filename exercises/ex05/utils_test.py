"""Test for the utils functions created."""

__author__ = "730232367"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test to see an empty set is returned when given an empty set."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_odds() -> None:
    """Test to see if empty set is returned when given an only odd list."""
    xs: list[int] = [3, 5, 11]
    assert only_evens(xs) == []


def test_many_num() -> None:
    """Test to see when there are many numbers in the set."""
    xs: list[int] = [2, 9, 16, 10, 12, 4, 3, 7, 8]
    assert only_evens(xs) == [2, 16, 10, 12, 4, 8]


def test_sub_negative_start() -> None:
    """Test to see if start number of subset is negative will actually start subset at 0."""
    xs: list[int] = [2, 4, 8, 9, 12]
    assert sub(xs, -1, 2) == [2, 4]


def test_sub_empty() -> None:
    """Test an empty set with parameters that are specified."""
    xs: list[int] = []
    assert sub(xs, 0, 2) == []


def test_sub_many_num() -> None:
    """Test a sub function with a lot of ints in the list."""
    xs: list[int] = [2, 3, 10, 11, 14, 34, 35]
    assert sub(xs, 1, 4) == [3, 10, 11]


def test_concat_first_empty() -> None:
    """Test with the first list being an empty set."""
    a_list: list[int] = []
    b_list: list[int] = [4, 5, 6]
    assert concat(a_list, b_list) == [4, 5, 6]


def test_concat_second_empty() -> None:
    """Test with the both list being an empty set."""
    a_list: list[int] = []
    b_list: list[int] = []
    assert concat(a_list, b_list) == []


def test_concat_normal() -> None:
    """Test the concat function with multiple int in each list."""
    a_list: list[int] = [1, 3, 9, 10, 12]
    b_list: list[int] = [2, 8, 4, 15]
    assert concat(a_list, b_list) == [1, 3, 9, 10, 12, 2, 8, 4, 15]