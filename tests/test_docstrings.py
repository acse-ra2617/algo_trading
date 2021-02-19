# -*- coding: utf-8 -*-
"""Runs docstrings in gauss.py, in command prompt type
'python test_docstrings.py' to trigger' """
import os

os.system("python -m pytest --doctest-modules ../acse_la/gauss.py")
