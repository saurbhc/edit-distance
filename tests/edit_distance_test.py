from __future__ import annotations

from edit_distance import calculate_distance


def test_calculate_distance_1():
    assert calculate_distance("tomayto", "tomahto") == 1


# def test_calculate_distance_2():
#     assert calculate_distance("intention", "execution") == 8
