"""test file for examples"""
import numpy as np
import pytest
from algos import Summation


class TestExample(object):
    """
    Class for testing examples
    """

    @pytest.mark.parametrize('a, b, c', [
        (2, 3, 5,)
    ])
    def test_Summation(self, a, b, c):
        """ Test the gauss function """
        out = Summation(a, b)
        assert np.issclose(c, out)
