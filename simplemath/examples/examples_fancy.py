# examples_fancy.py

from .. fancy import add, sub, mul, div

from .. smlib import printEval
from .. smlib import Animals

cat = Animals.cat
dog = Animals.dog
monkey = Animals.monkey
snake = Animals.snake

calculations = ["add(3, 2, snake)", "sub(7, 4, dog)", "mul(6, 3, cat)",
                "div(48, 6, monkey)"]


def run():
    for i, calculation in enumerate(calculations):
        print(f"{i}) ", end="")
        printEval(calculation, globals=globals())
