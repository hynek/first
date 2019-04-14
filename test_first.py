import unittest
from first import first


isbool = lambda x: isinstance(x, bool)
isint = lambda x: isinstance(x, int)
odd = lambda x: isint(x) and x % 2 != 0
even = lambda x: isint(x) and x % 2 == 0
is_meaning_of_life = lambda x: x == 42


class TestFirst(unittest.TestCase):
    def test_empty_iterables(self):
        s = set()
        l = []
        assert first(s) is None
        assert first(l) is None

    def test_default_value(self):
        s = set()
        l = []
        assert first(s, default=42) == 42
        assert first(l, default=3.14) == 3.14

        l = [0, False, []]
        assert first(l, default=3.14) == 3.14

    def test_selection(self):
        l = [(), 0, False, 3, []]

        assert first(l, default=42) == 3
        assert first(l, key=isint) == 0
        assert first(l, key=isbool) is False
        assert first(l, key=odd) == 3
        assert first(l, key=even) == 0
        assert first(l, key=is_meaning_of_life) is None

    def test_dictionary_first(self):
        d = {
                1: (),
                2: 0,
                3: False,
                4: 3,
                5: [],
                6: None
        }

        assert first(d) == 4
        assert first(d, default=42) == 4
        assert first(d, key=isint) == 2
        assert first(d, key=isbool) == 3
        assert first(d, key=odd) == 4
        assert first(d, key=even) == 2
        assert first(d, key=is_meaning_of_life) is None

        d = {1: None, 2: 3.14, 3: 2.72}

        assert first(d) == 2


if __name__ == '__main__':
    unittest.main()
