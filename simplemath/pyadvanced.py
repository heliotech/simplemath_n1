# pyadvanced.py

from .smlib import (Animals, generalOperationFactory, Markers, printEval,
                    OperationData)

add = generalOperationFactory(OperationData.ADD, Markers.dot)
sub = generalOperationFactory(OperationData.SUB, Animals.snake)
mul = generalOperationFactory(OperationData.MUL, Animals.cat)
div = generalOperationFactory(OperationData.DIV, Animals.monkey)
