# Reverse Polish Notation Calculator

## Run without installing
```bash
# One shot calculation
python rpn.py 3 4 +

# Pipeline
cat foobar.txt | python rpn.py

# Interactive mode
python rpn.py
```

## To install
```bash
sudo make install
```

It will create a `rpn` symbolic link to `rpn.py` that you can run anywhere.

## To uninstall
```bash
sudo make uninstall
```

## To run tests
```bash
make test
```

Requires `pytest` installed.

## Considerations
- It was tested on a Linux system with Python 3.8.2, but should run on any Unix system with python 3.5+.
- I deliberately choosed to not use some external modules (Click, Argparse, etc).
- I aimed to be as simple as possible: flat files organization, no complex classes, etc. Basically pragmatism over purism.
