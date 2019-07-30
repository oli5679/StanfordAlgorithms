import pytest
from ps_4 import Kosaraju, INPUT_PATH, parse_input_file
from IPython import embed

TEST_EDGE_A = [[1, 0], [2, 1], [0, 2], [0, 3], [3, 4]]
TEST_EDGE_B = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [3, 1],
    [2, 1],
    [2, 5],
    [1, 4],
    [5, 4],
    [4, 6],
    [6, 5],
    [5, 7],
    [6, 8],
    [7, 8],
    [8, 7],
]


def test_a():
    kos = Kosaraju(TEST_EDGE_A)
    res = kos.largest_n_sccs(3)
    assert res == [3, 1, 1]


def test_b():
    kos = Kosaraju(TEST_EDGE_B)
    res = kos.largest_n_sccs(3)
    assert res == [4, 3, 2]


def test_larger_Input():
    edges_list = parse_input_file(INPUT_PATH)
    edges_list = edges_list[:50000]
    kos = Kosaraju(edges_list)
    res = kos.largest_n_sccs(5)


test_larger_Input()
