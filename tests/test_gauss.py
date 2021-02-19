"""test file for Gaussian elimination algorithm and related"""
import numpy as np
import pytest
from acse_la import gauss, matmul, zeromat


class TestGauss(object):
    """
    Class for testing the Gaussian elimination algorithm Gauss
    and its associated functions.
    """

    @pytest.mark.parametrize('a, b, dete, xe, a2, b2, dete2, xe2', [
        ([[2, 9, 4], [7, 5, 3], [6, 1, 8]],
         [[1, 0, 0], [0, 1, 0], [0, 0, 1]], -360.0,
         [[-0.10277777777777776, 0.18888888888888888, -0.019444444444444438],
          [0.10555555555555554, 0.02222222222222223, -0.061111111111111116],
          [0.0638888888888889, -0.14444444444444446, 0.14722222222222223]],
         [[.2, .9, .4], [.7, .5, .3], [.6, .1, .8]],
         [[1, 0, 0], [0, 1, 0], [0, 0, 1]], -.36,
         [[-1.027777777777778, 1.8888888888888888, -0.1944444444444443],
          [1.0555555555555558, 0.22222222222222218, -0.6111111111111112],
          [0.638888888888889, -1.4444444444444444, 1.472222222222222]])
    ])
    def test_gauss(self, a, b, dete, xe, a2, b2, dete2, xe2):
        """ Test the gauss function """
        det, x = gauss(a, b)
        det2, x2 = gauss(a2, b2)

        assert np.isclose(det, dete)
        assert np.allclose(x, xe)
        assert np.isclose(det2, dete2)
        assert np.allclose(x2, xe2)

    @pytest.mark.parametrize('a, b, producte ,a2, b2, producte2', [
        ([[2, 0, -1], [0, 5, 6], [0, -1, 1]],
         [[2], [1], [2]],
         [[2], [17], [1]],
         [[3, 4], [2, 1]],
         [[1, 5], [3, 7]],
         [[15, 43], [5, 17]])
    ])
    def test_matmul(self, a, b, producte, a2, b2, producte2):
        """ Test the matrix multiplication function """
        product = matmul(a, b)
        product2 = matmul(a2, b2)
        assert np.allclose(product, producte)
        assert np.allclose(product2, producte2)

    @pytest.mark.parametrize('p, q, list_empty', [
        (3,
         1,
         [[0], [0], [0]])
    ])
    def test_zeromat(self, p, q, list_empty):
        """ Test the zeros matrix function """
        list_zeros = zeromat(p, q)
        assert list_zeros == list_empty

# Consider what when not invertible!
# a = [[1, 1, 1], [2, 3, 3], [3, 4, 4]] #no inverse matrix exists!
# b = [[1], [1], [1]]

# a = [[0,3],[0,2]]
# b = [[1],[1]]
