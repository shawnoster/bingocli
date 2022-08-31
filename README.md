[![Board Status](https://shawnoster.visualstudio.com/5e1d907d-b0b4-4272-be99-f3ac5c2e7a67/d5f5307e-41cf-4213-b276-aeabbe419a5e/_apis/work/boardbadge/535d3815-5607-47d2-a109-a8d1e277201f)](https://shawnoster.visualstudio.com/5e1d907d-b0b4-4272-be99-f3ac5c2e7a67/_boards/board/t/d5f5307e-41cf-4213-b276-aeabbe419a5e/Microsoft.RequirementCategory)
# nightowlcli

```
  ___    
 (o,o)   Night Owl CLI
 {`"'}   A stub folder structure for Python 3 CLIs
 -"-"-
```

## what?

This is a bare-bones CLI skeleton inspired by (totally ripped off from) a post titled "[The easy (and nice) way to do CLI apps in Python][easy-way-to-do-cli]" by Thomas Stringer with some testing bits snaked from [Python Unit Testing – Structuring Your Project][unit-testing].

## why?

I write a lot of these, and invariably forget some detail or best practice that I swore I'd totally always remember that I then promptly forget. My favorite form of procrastination is two hour squirrel adventures searching for the "right way" to do things so to my future self... _"get back to work arsehole, we've already been down this rabbit hole."_

The more I code the more I become a fan of opinionated languages, frameworks and software free of all the wishy washy "you can put it here, or here, or here" which is all fine and dandy for the long time disciples but when just starting out nothing's more frustrating than multiple options with no direction.

### in the box

- Python 3
- Best-practice folder structure (for now)
- Tests (using unittest)
- install scripts

### folder structure and files

```
nightowlcli/
├── README.md           # what it is, include lots of examples, fewer words
├── install.bat         # debug script to run pip3 install -e . (because Windows)
├── install.sh          # debug script to run pip3 install -e . (because Linux)
├── LICENSE             # license your stuff
├── nightowlcli         # the guts
  ├── __init__.py       # empty, tells Python the folder is a module
  ├── __main__.py       # entry point, do arg parsing here
  └── funky.py          # the code
├── test                # folder for your tests
  ├── __init__.py       # empty, tells Python the folder is a module (yes, even for tests)
  └── test_funky.py     # tests for funky
└── setup.py            # needed to install the cli
```

### method amoung the madness

Given this is pretty 101 stuff I'm going to assume at least some lost souls might not have their console skills turned up to 11 yet. Or you simply can't make sense of my idosyncratic chicken scratch so here are some over-explained conventions:

- On Windows replace all the commands `python3` with `python`
- All pound symbols (#) are comments, don't type them!

## how?

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
nightowlcli -h
```

Check that the test framework is working correctly before you go mucking it up and trying to blame me for your crap typing. Talking to my future self again.

```
python3 -m unittest discover -v
```

When you're done futzzing around with your code you should _actually_ install it via pip3.

```
pip3 install nightowlcli --user
```

### make it yours

Clone and rename the root folder (nightowlcli) and the code module subfolder (also nightowlcli) as you desire. Toss funky.py and test_funky.py, those are examples and your code is better.

Nothing about this structure is sacred but it is fairly common and it hasn't failed me yet.

### don't forget to...

- update `setup.py` with your information, not mine, unless you're me
- replace the LICENCE file and test in setup.py to match whatever license you're using. I use MIT because it's simple
- Delete everything in this `README.md`, insert your magic. I strongly suggest you at least include:
  - How to install it, assuming the barest knowledge of Python
  - Lots of examples and for all flags/options, at least 2-3 examples ranging from basic to kung fu master. No one reads docs, you hate writing it and no one really likes to wade through tests to see example usage.

[easy-way-to-do-cli]: https://medium.com/@trstringer/the-easy-and-nice-way-to-do-cli-apps-in-python-5d9964dc950d
[unit-testing]:https://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/