# Bingo CLI

```
  ___    
 (o,o)   Bingo CLI
 {`"'}   A playful Python project used to explore serious things
 -"-"-
```

## Overview

A playful Python-based, bingo-themed CLI project used as a playground to explore various Python techniques. A fully featured set of bingo services will emerge over time but this is primarily a learning tool.

### Folders and Files

```
bingocli/
├── README.md           # what it is, include lots of examples, fewer words
├── install.bat         # debug script to run pip3 install -e . (because Windows)
├── install.sh          # debug script to run pip3 install -e . (because Linux)
├── LICENSE             # license your stuff
├── bingocli            # the guts
  ├── __init__.py       # empty, tells Python the folder is a module
  ├── __main__.py       # entry point, do arg parsing here
├── test                # folder for your tests
  ├── __init__.py       # empty, tells Python the folder is a module (yes, even for tests)
└── setup.py            # needed to install the cli
```

### Setup

To prove it works, clone the repro, cd into the root folder and depending on your OS run:

Linux/Mac

```
$ sh install.sh
```

or

Windows

```
> install # (it's a batch file)
```

Then

```
bingoapi -h
```

Check that the test framework is working correctly before you go mucking it up and trying to blame me for your crap typing. Talking to my future self again.

```
python3 -m unittest discover -v
```

When you're done futzzing around with your code you should _actually_ install it via pip3.

```
pip3 install bingoapi --user
```
