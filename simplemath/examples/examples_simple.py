# examples_simple.py

from .. simple import add, sub, mul, div

from .. smlib import printEval

calculations = ["add(3, 2)", "sub(7, 4)", "mul(6, 3)", "div(48, 6)"]


def run():
    for i, calculation in enumerate(calculations):
        print(f"{i}) ", end="")
        printEval(calculation, globals=globals())
