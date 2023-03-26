# fancy.py

"""
A part of the Simplemath Project

Fancy version of `simple.py`, 4 basic algebraic operations in python.
The arguments and results are presented with UTF icons.
Each number is represented with the help of dedicated function, `showNumber`

Symbols:
    subtraction chr(8211) -> – (regular - vs. –)
    multiplication \u00D7 -> ×
    division \u00F7 -> ÷

"""
# from numpy import sign
from math import copysign
try:
    from .mutils import DbgInfo
except ImportError:
    from mutils import DbgInfo

DBG = True
dbgi = DbgInfo(DBG=DBG)
printd = dbgi.printd_()

ftitle = __file__.split('/')[-1].split('.')[0]

# Markers:
mrkDot = "•"
mrkCat = chr(128008)  # 🐈
mrkDog = chr(128021)  # 🐕
mrkSnake = chr(128013)  # 🐍


def sign(value):
    """ Adaptation of `copysign` function """

    return copysign(1, value)


def printEval(code):
    """ Prints and evaluates `code` """

    print(code + " →")
    eval(code)
    print()


def showNumber(num, marker=mrkDot, sep=" ", part=5,
               DBG=False):
    """ Getting graphical representation of a number.

    Args:
        num: int - number to be graphically represented,
        marker: str - char for a marker,
        sep: str - number parts (sections) separator,
        part: int - length of the number part (section),
        pos: int - position of the number in the calculaiton, def. -1;
            0 for the first position.
    """

    # if float(num).is_integer():
    #     num = int(num)
    if float(num).is_integer():
        num = int(num)
        numInt = num
        decimalPart = ""
    else:
        numInt = int(num)
        decimalPart = "..."
    errMsg = ""
    parts = abs(numInt)//part
    sgn = "" if sign(num) >= 0 else "(-)"
    try:
        if parts > 0:
            mainPart = sep.join(marker*part for i in range(parts))
            remainder = abs(num) - part*parts
            remainder = 0 if remainder < 1 else -1
        else:
            mainPart = marker*abs(numInt)
            remainder = 0
        remainderGraph = marker*remainder if remainder else ""
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
           src="showNumber", DBG=DBG)

    newLine0 = "" if len(numGraph) < 21 else "\n"  # 'last' new line

    return f"{sgn}{numGraph}{decimalPart} ({num}){newLine0}", errMsg


def add(a, b, marker="•"):
    res = a + b
    res = round(res, 2) if len(str(abs(res) - int(abs(res)))) > 4 else res
    aGraph = showNumber(a, marker=marker)[0]
    bGraph = showNumber(b, marker=marker)[0]
    resGraph, err = showNumber(res, marker=marker)
    print("Addition:\n"
          f"{aGraph} + {bGraph} = {resGraph} \n{err}")


def sub(a, b, marker="•"):
    res = a - b
    res = round(res, 2) if len(str(abs(res) - int(abs(res)))) > 4 else res
    aGraph = showNumber(a, marker=marker)[0]
    bGraph = showNumber(b, marker=marker)[0]
    resGraph, err = showNumber(res, marker=marker)
    nl0B = " " if len(bGraph) < 21 else "\n"
    nl0Res = " " if len(resGraph) < 21 else "\n"
    print("Subtraction:\n"
          f"{aGraph}{nl0B}– {bGraph}{nl0Res}= {resGraph} \n{err}")


def mul(a, b, marker="•"):
    res = a*b
    res = round(res, 2) if len(str(abs(res) - int(abs(res)))) > 4 else res
    aGraph = showNumber(a, marker=marker)[0]
    bGraph = showNumber(b, marker=marker)[0]
    resGraph, err = showNumber(res, marker=marker)
    nl0B = " " if len(bGraph) < 21 else "\n"
    nl0Res = " " if len(resGraph) < 21 else "\n"
    print("Multiplication:\n"
          f"{aGraph}{nl0B}\u00D7 {bGraph}{nl0Res}= {resGraph} \n{err}")


def div(a, b, marker="•"):
    res = a/b
    print("")
    a = int(a) if float(a).is_integer() else a
    b = int(b) if float(b).is_integer() else b
    # assert (isinstance(a, int) and isinstance(b, int) and
    #         (a//b == res))
    res = round(res, 2) if len(str(abs(res) - int(abs(res)))) > 4 else res
    aGraph = showNumber(a, marker=marker)[0]
    bGraph = showNumber(b, marker=marker)[0]
    resGraph, err = showNumber(res, marker=marker)
    nl0B = " " if len(bGraph) < 21 else "\n"
    nl0Res = " " if len(resGraph) < 21 else "\n"
    print("Division:\n"
          f"{aGraph} \u00F7{nl0B}{bGraph}{nl0Res}= {resGraph}"
          f"\n{err}")


def main():
    nrs = [3, 7, 11., 11]
    bes = [2, 3, 4, 5]
    mrkrs = [mrkDot, mrkCat, mrkDog, mrkSnake]
    for i, nr in enumerate(nrs):
        marker = mrkrs[i]
        nrGraph, errMsg = showNumber(nr, marker)
        print(f"{i}) {nr}: {nrGraph = }\n{errMsg = }")
    print(mrkDot, type(mrkDot))
    print(mrkDog, type(mrkDog))
    for i, (a, b) in enumerate(zip(nrs, bes)):
        print(f"... {i})")
        mul(a, b, mrkrs[i])
    add(3, 5.3, marker)
    sub(12, 3, marker)
    div(14., 2, marker)
    div(-21, 3.1, marker)

if __name__ == '__main__':
    main()

