"""install script for python packages"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='algos',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description="Environment for algorithmic trading package.",
      long_description="""Environment for algorithmic trading package.""",
      url='',
      author="Aemiro Habte & Raul Adriaensen",
      author_email='raul.adriaensen17@imperial.ac.uk',
      packages=['algos'])
