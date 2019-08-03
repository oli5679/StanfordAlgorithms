import pytest

from ps_3 import Huffman


def test_huffman():
    test_codes = [60, 25, 10, 5]
    test_huff = Huffman(test_codes)
    encodings = test_huff.encode_all()
    assert len(encodings[3]) == 3
    assert len(encodings[0]) == 1
    assert len(encodings[1]) == 2
