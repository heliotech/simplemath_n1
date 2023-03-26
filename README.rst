`simplemath` -- project for learning 4 basic algebraic operations with python
=============================================================================

*WARNING! readme.rst is out of date.*

`simplemath` project presents the visualization of 4 basic algebraic operations. With help of the ascii or UTF characters it assists younger children in learning how to calculate and how to use the python programming language. Learning python, however, may require assistance of a tutor.

The project was build to learn how to:

1. build python packages and upload them them to PyPI,
2. use GitHub.

Contents
--------

1. `simple.py` (`<simplemath/simple.py>`_)

The file `simple.py` contains 4 functions, `add`, `sub`, `mul`, `div`, which illustrate basic arithmetical operation, respectively addition, subtraction, multiplication and division. All the functions represent provided arguments with simple dots, which can be counted, by children, to check their understanding of an operation. Each function can be used in an interactive python session, or `examples_simple.py` can be run to show all the functions in action. The implementation was simplified: the functions are designed for positive, integer arguments and results.

The `add` function use simple string concatenation, while `sub`, `mul` and `div` apply python fstrings. This approach shows better visual effect, e.i. readability of code, of the later solution.

(`printEval` function was designed to facilitate printing a piece of code, which would be followed by the execution of said code.)

2. `fancy.py` (`<simplemath/fancy.py>`_)

`fancy.py` implements the same basic functions, `add`, `sub`, `mul` and `div`, with better capabilities for representing the algebraic operations. Markers in a graphical representation of the number are grouped into parts, while printing the parts are separated, for readability. Either the marker, group length and separator can be defined, as parameters.

The functions are designed for positive integers, although they are provided with basic error handling.

3. `pyadvanced.py` (`<simplemath/pyadvanced.py>`_)

`pyadvanced.py` shows improved programming techniques, e.g. higher order function, returning another function; here this method provides general approach to defining the algebraic functions. Also functions for representation of a number, `representNumber`, and for printing and evaluating of a code snippet were moved to a library, `smlib.py`. "pyadvanced" functions manage with either negative or floating point numbers.

Development environment
-----------------------

- Linux Mint 21.1 Vera, x86_64, desktop: Cinnamon 5.6.8.
- Python 3.10.6
- Sublime Text build: 4143
- Terminal: Terminator 2.1.1, gnome-terminal 3.44.0


Author
------

khaz pykhaz@o2.pl

Homepage
--------

https://github.com/heliotech/simplemath_n1

Irresponsibility disclaimer
----------------------------

The software is provided 'as is', the author takes no responsibility for any possible problems.
