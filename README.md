# Grade Tracker

A command-line tool that reads student marks from a CSV file and prints a ranking.

## Install

```
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Usage

```
python tracker.py marks.csv
```

## Run the tests

```
python -m pytest
```

## What I learned

- print vs return: print shows a value on screen; return gives the value back to the program so it can be used again.
- class vs object: a class is the cookie cutter, and objects are the cookies shaped by it.
- empty-marks test: the empty marks test is more important than the happy pass test because it covers the input that would crash the program , which would go unnoticed until someone else hit it   
- tmp_path: tmp_path beats my real marks.csv because the test makes its own throwaway file with known contents, so it keeps passing even when I change the real file.