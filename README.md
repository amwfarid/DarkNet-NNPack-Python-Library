# DarkNet-NNPack Python Library

A custom library to access DarkNet (NNPack implementation)'s functions without the default python library. This is a quick workaround (which may be considerably dirty) to the issue of the python library not initializing properly, as in [this issue](https://github.com/digitalbrain79/darknet-nnpack/issues/17)

This is done by injecting TCP server code into the DarkNet source code and communicating with it through the Python script. The main motivation of this library is to have a Python interface that only manipulates DarkNet into initializing the weights only once, then detecting as many times as needed.

Currently, this library only works for the object detection functionality.

## Installation

First, clone this repo:
```
git clone https://github.com/amwfarid/DarkNet-NNPack-Python-Library
```

You have install the original [DarkNet-NNPack](https://github.com/digitalbrain79/darknet-nnpack) code. Follow the instructions on the repo's page.

After successful installation and testing, run `install.sh`:
```
sh install.sh
```

What this essentially does is simply copy the modified `detector.c` and `darknet.h` files, then `make` the source code once again.

## Python API

To test the API, you can directly run:
```
python DarkNetDetect.py
```

To make it work anywhere by means of `import`, please make sure that the path to `DarkNetDetect.py` is in `$PYTHONPATH`.

The API is fairly simple at this stagee. Please see `DarkNetDetect.py` for more details.
