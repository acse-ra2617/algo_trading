# -*- coding: utf-8 -*-


"""file to initialise package"""

from pkg_resources import get_distribution, DistributionNotFound
from .example import *  # noqa

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


"""
Created on Fri Feb 19 22:58:51 2021

@author: acse-ra2617
"""
