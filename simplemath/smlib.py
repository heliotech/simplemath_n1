# smlib.py

"""
Library for Al Project
"""

from dataclasses import dataclass
from math import copysign

# from .mutils import DbgInfo


# DBG = True
# dbgi = DbgInfo(DBG=DBG)
# printd = dbgi.printd_()
def printd(*args, **kwargs):
    # msg = ", ".join(m for m in args)
    # src = f" {kwargs['src']}" if 'src' in kwargs else ""
    # print(f"DBG{src}: {msg}")
    pass


SEP = " "  # the `part` separator, for `getNumGraph`


def sign(value):
    """ Adaptation of `copysign` function """

    return copysign(1, value)


# Dataclass for markers:
@dataclass
class Markers:
    star0 = chr(9733)
    star1 = chr(9734)
    star2 = chr(10026)
    star1 = chr(10040)
    dot = "•"


@dataclass
class Animals:
    """ Dataclass for animals emoji.

    List of animals/members:
        snake, cat, cat_face, dog, dog_face, monkey
    """

    snake = chr(128013)  # 🐍
    cat = chr(128008)  # 🐈
    cat_face = chr(128049)  # 🐱 "\u1F431"
    dog = chr(128021)  # 🐕
    dog_face = chr(128054)  # 🐶
    monkey = chr(128018)  # 🐒


# Operation dataclass:
@dataclass
class OperationData:
    ADD = {"symbol": "+", "name": "Addition", "op": (lambda x, y: x + y)}
    SUB = {"symbol": "–", "name": "Subtraction", "op": (lambda x, y: x - y)}
    MUL = {"symbol": "\u00D7", "name": "Multiplication",
           "op": (lambda x, y: x*y)}
    DIV = {"symbol": "\u00F7", "name": "Dvision",
           "op": (lambda x, y: x/y)}


def representNumber(num, marker=Markers.dot, sep=" ", part=None, DBG=False):
    """ Getting graphical representation of the result

    Args:
        num: int - number to be graphically represented,
        marker: str - char or code for a marker,
        sep: str - number parts (sections) separator,
        part: int - length of the number part (section),
        pos: int - position of the number in the calculaiton, def. -1;
            0 for the first position.
    """

    printd(src=f"representNumber ({num})")
    errMsg = ""
    numInt = int(num)
    if num == numInt:
        decimalPart = ""
    else:
        decimalPart = ".(…)"
        errMsg = ("A problem occured:\n"
                  "only integer numbers can be represented, "
                  f"but it happened to be {num}\n")
    if not part:
        part = 5 if num <= 10 else 10
    parts = abs(numInt)//part
    sgn = "" if sign(num) >= 0 else "(-)"
    printd(f"{part = }, {parts = }")
    try:
        if parts > 0:
            mainPart = sep.join(marker*part for i in range(parts))
            remainder = abs(num) - part*parts
        else:
            mainPart = marker*abs(numInt)
            remainder = 0
        printd(f"{mainPart = }, {remainder = }")
        remainderGraph = marker*int(remainder) if remainder else ""
        remainderGraph = (sep + remainderGraph if remainder > 0
                          else remainderGraph)
    except TypeError:
        errMsg = ("A problem occured:\n"
                  "only integer numbers can be represented, "
                  f"but it happened to be {num}\n")
        # return "(?)", errMsg
    numGraph = mainPart + remainderGraph
    printd(f"{part = }, {parts = }, {num = :>3}, {remainder = }", DBG=False)
    printd(f"{num = }, {len(mainPart) = }, {remainder = },\n"
           f"{len(remainderGraph) = } <= {remainderGraph}\n"
           f"{numGraph = }",
           src="getNumGraph", DBG=DBG)

    newLine0 = "" if len(numGraph) < 21 else "\n"
    return f"{newLine0}{sgn}{numGraph}{decimalPart}", errMsg


# def printEval(code, globals, locals):
def printEval(code, globals=None, locals=None):
    print(code + " →")
    # eval(code, globals, locals)
    eval(code, globals, locals)


def generalOperationFactory(operationData, marker="•"):
    """ Factory function for a basic arithmetic operation.

    Function returned is defined by `operationData`.
    """

    def fun(a, b, marker=marker):
        """
        General arithmetical operation function to be specialized
        """

        opSmb, opName, op = operationData.values()
        res = op(a, b)
        res = round(res, 2) if len(str(res - int(res))) > 4 else res
        try:
            if res.is_integer():
                res = res.as_integer_ratio()[0]
        except AttributeError:
            pass
        aGraph = representNumber(a, marker=marker, sep=SEP)[0]
        bGraph = representNumber(b, marker=marker, sep=SEP)[0]
        resGraph, err = representNumber(res, marker=marker, sep=SEP)
        aNL = " " if len(aGraph) < 21 else "\n"
        # bNL = " " if len(bGraph) < 21 else "\n"
        # rNL = "" if len(resGraph) < 21 else "\n"
        print(f"{opName}:\n"
              f"{aGraph} ({a}) {opSmb}{aNL}{bGraph} ({b}) = "
              f"{resGraph} ({res})\n{err}")

    return fun


def main():
    print(f"{Markers = }")
    od = OperationData
    print(od.ADD)
    print(f"{od.ADD = }, {type(OperationData.ADD) = }")
    print(f"{od.SUB = }, {type(od.SUB) = }")
    print(f"{od.MUL = }, {type(od.MUL) = }")
    print(f"{od.DIV = }, {type(od.DIV) = }")
    # foritemin(od)
    print(f"{Animals = }")
    print(f"{Animals.snake = }")
    div = generalOperationFactory(od.DIV)
    div(9, 3, Animals.snake)
    mul = generalOperationFactory(od.MUL, Markers.star0)
    mul(6, 3)
    mul(7, 4, marker=Markers.star1)
    mul(7, 3.4, marker=Markers.star2)


if __name__ == '__main__':
    main()
