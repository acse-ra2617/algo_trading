# algo_trading
The current main focus of this project is to build experience in algorithmic trading.
next development stages that will be covered:
* design a good architecture that can grow in modules and can be released at an early stage
* access an API to obtain market data
* construct visualisation functions

<center><img src="./documents/stonks.png" width="30%" class="centerImage" alt="Connway way of life single frame example"></center>

# repo structure
tests -> store tests that will be run by github CI and user locally
documents -> data used by repo, documentations, etc..
algos -> our program
  - data -> data storage
  - static -> static graphs called to web interface
  - templates -> web interface

# installation
To run our program, while not a requirement, it is recommended that
you create a new virtual environment and install the required `Python` packages
within your virtual environment.

If you wish to create an `Anaconda` environment, an `environment.yml` file has
been provided from which you can create the `acse_la` environment
by running
```bash
conda env create -f environment.yml
```

Note that Ta-lib has not been included due to clashes it cuases with the github CI, for windows please follow the following installation intructions:
https://stackoverflow.com/questions/49154899/resolvepackagenotfound-create-env-using-conda-and-yml-file-on-macos

from within the base folder of this repository. If you wish to use some other virtual environment solution (or none at all),
when in your environment ensure that all requirements are satisfied via
```bash
pip install -r requirements.txt
```

Whichever solution you decide upon, the package `algos` should then be installed
by running
```bash
pip install -e .
```
again from within the base folder of this repository.


# Authors
* [Aemiro Habte](https://www.linkedin.com/in/aemiro-habte-772525179/)
* [Raul Adriaensen](www.linkedin.com/in/rauladriaensen)

