"""test file for examples"""
import numpy as np
import pytest
from algos import summation


class TestExample(object):
    """
    Class for testing examples
    """

    @pytest.mark.parametrize('a, b, c', [
        (20, 3, 23,)
    ])
    def test_summation(self, a, b, c):
        """ Test the gauss function """
        out = summation(a, b)
        assert np.isclose(c, out)
