# Naive Pascal Triangle

This repository contains a python application that prints out the pascal triangle in the commandline for an arbitrary level. 

The main objectives: 

* Demonstrate how to create commandline application in python. 
* Practice recursive functions and get exposure to common python libs and patterns. 


## Setup

Setup your virtualenv as following:

1. Create and activate a virtualenv
    * `virtualenv --python=python3 venv`
    * `source venv/bin/activate`
1. Install requirements
    * `pip install -r requirements.txt`

## Usage

Once `venv` in active, the usage is fairly simple: 

```commandline
$ python main.py pascal_triangle --level 15
```

Options: 

```text
    --level  : a positive integer indicating the total number of rows. 
```

## Examples

Pascal triangle with 5 rows:

```text
$ python main.py pascal_triangle --level 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
INFO:__main__:Execution time 7.104873657226562e-05
```

Pascal triangle with 10 rows:

```text
$ python main.py pascal_triangle --level 10
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
INFO:__main__:Execution time 0.0005848407745361328
```
