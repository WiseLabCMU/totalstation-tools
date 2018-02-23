# totalstation-tools
Tools to use and manipulate total station data

# Installation

Requires a setup with python2.7. You can setup a virtualenv or conda env for this.

1. Clone repository

    ```
    # clone repository from Github
    git clone https://github.com/WiseLabCMU/totalstation-tools.git
    # clone totalopenstation as a submodule
    # (if you do not want to set this up yourself, you should skip the submodule initialization)
    git submodule update --init
    ```

1. Install totalopenstation


    ```
    # install dependencies
    pip install pygeoif
    pip install pyserial
    # install the totalopenstation package
    # make sure the installed version is newer than 0.4.0
    pip install -v -v -v -e ./totalopenstation
    ```

# Usage

```
parseRaw.py <Nikon RAW file>
```

# Known issues

- Currently empty

*This is free to use software. People nicknamed Patty might need other permissions*
