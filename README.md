[![robinhood-logo](https://i.imgur.com/74CYw5g.png)](https://github.com/robinhood-unofficial/pyrh)

------------------------------------------------------------------------

# pyrh - Unofficial Robinhood API

[![Build Status](https://github.com/robinhood-unofficial/pyrh/workflows/build/badge.svg?branch=master&event=push)](https://github.com/robinhood-unofficial/pyrh/actions?query=workflow%3Abuild+branch%3Amaster)

[![Coverage](https://codecov.io/gh/robinhood-unofficial/pyrh/branch/master/graph/badge.svg)](https://codecov.io/gh/robinhood-unofficial/pyrh)

[![Documentation Status](https://readthedocs.org/projects/pyrh/badge/?version=latest)](https://pyrh.readthedocs.io/en/latest/?badge=latest)

[![PyPI Version](https://img.shields.io/pypi/v/pyrh?style=plastic)](https://pypi.org/project/pyrh/)

[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyrh?color=blue&style=plastic)](https://pypi.org/project/pyrh/)

[![License](https://img.shields.io/github/license/robinhood-unofficial/Robinhood)](https://github.com/robinhood-unofficial/pyrh/blob/master/LICENSE)

[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Gitter](https://img.shields.io/gitter/room/J-Robinhood/Lobby)](https://gitter.im/J-Robinhood/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Python Framework to make trades with Unofficial Robinhood API. Supports
Python 3.6+

# *Please note that parts of this project maybe non-functional / under rapid development*

-   A stable release is imminent

Documentation: <https://pyrh.readthedocs.io/en/latest/>

## Quick start

``` python
from pyrhhfbp import Robinhood

rh = Robinhood()
rh.login(username="YOUR_EMAIL", password="YOUR_PASSWORD")
rh.print_quote("AAPL")
```

## Installing

    pip install pyrhhfbp

## Running unit tests

    poetry run pytest --cov-report=xml

##  Release to PyPI 

    poetry publish --build

## Sample usage

See the [./pyrhhfbp/samples/](./pyrhhfbp/samples/) folder for some examples of how to login to Robin Hood, to place BUY orders, etc.

## Running [example.ipynb](https://github.com/robinhood-unofficial/pyrh/blob/master/notebooks/example.ipynb)

Clone the repository and install jupyter capabilities.

    git clone https://github.com/robinhood-unofficial/pyrh.git
    cd pyrh
    python --version # python 3.3+ for venv functionality
    
    python -m venv pyrh_env
    source pyrh_env/bin/activate
    pip install .[notebook]
    cp .env.sample .env # update the values in here
    jupyter notebook notebooks/example.ipynb


Now just run the files in the example.

## Related

-   [robinhood-ruby](https://github.com/rememberlenny/robinhood-ruby) -
    RubyGem for interacting with Robinhood API
-   [robinhood-node](https://github.com/aurbano/robinhood-node) - NodeJS
    module to make trades with Robinhood Private API
-   See the original [blog
    post](https://medium.com/@rohanpai25/reversing-robinhood-free-accessible-automated-stock-trading-f40fba1e7d8b).
