# mutils.py

"""
Miscalleanous utility functions
"""


mdChar = chr(0x00b7)  # middle dot


def printd(*args, filename=None, marker=mdChar, **kwargs):
    # tab = int(kwargs["tab"]) if "tab" in kwargs else 0
    # print(f"D: {tab = } of type {type(tab)}")
    if "DBG" in kwargs and kwargs["DBG"] is True:
        # print(kwargs["DBG"])
        # message = "\t"*tab
        message = ""
        if "end" in kwargs:
            end = kwargs["end"]
        else:
            end = "\n"
        if "tab" in kwargs:
            nrTabs = kwargs["tab"]
        else:
            nrTabs = 0
        tabs = marker*4*nrTabs + " "
        if "src" in kwargs:
            opening = f"DBG {kwargs['src']}:"
        else:
            opening = "DBG:"
        for i in range(len(args)):
            message += str(args[i])
            if i == 0:
                message += " "
        if filename:
            with open(filename, "a") as fileOut:
                print(f"{tabs}DBG: {message}", end=end, file=fileOut)
        else:
            print(f"{tabs}{opening} {message}", end=end)
    else:
        # print("no DBG")
        pass


def printinfo(*args, src="", startwith="", end="\n", xline=False,
              filename=None, DBG=True):
    """ Prints message/various pieces of provided information """

    if DBG:
        message = ''
        for i in range(len(args)):
            message += str(args[i])
            if i < len(args) - 1:
                message += ", "
        if src != "":
            src = "'" + src + "'"
        if DBG:
            if filename:
                with open(filename, "a") as fileOut:
                    print("{}INFO {} >>> {}".format("\n" if xline else "", src,
                                                    message),
                          end=end, file=fileOut)
            else:
                opening = f"\n{startwith}" if xline else f"{startwith}"
                print("{}INFO {} >>> {}".format(opening, src,
                                                message), end=end)
    else:
        pass


def printnumbers(numbers=[], message="", fmt=".0f", DBG=False):
    """Printing an iterable of numbers with format"""

    if DBG:
        if message != "":
            print(message + ': [', end="")
        else:
            print("[", end="")
        print("".join("{:{fmt}}, ".format(n, fmt=fmt) for n in numbers),
              end="]\n")


def varinfo(var, name='', src='', line='', print_=True, fmt='.3f', DBG=False):
    """Printing information about a variable
    varinfo(var, name='', sre='')"""
    import numpy as np
    lmid = None
    result = ''

    lineHead = f", l.nr = {line}, " if line != "" else ", "
    if src != '':
        header = '***varinfo "' + src + '": ' + name + lineHead
    elif line != '':
        header = '***varinfo "' + name + lineHead
    else:
        header = '***varinfo "' + name + '": '
    try:
        l = len(var)
    except TypeError:
        # print('Exception')
        l = 0

    infogeneral = ''

    shapeS = str(np.shape(var))
    fmtSpc = "[{:<5"+fmt+"} {:<5"+fmt+"} {:<5"+fmt+"} {:<5"+fmt+"}]"
    if l > 20 and not isinstance(var, str):
        lmid = int(l/2)
        varSample = fmtSpc.format(*var[0:4])
        varSample += ' ...\n'
        varSample += fmtSpc.format(*var[lmid-2:lmid+2])
        varSample += '...\n'
        varSample += fmtSpc.format(*var[l-4:])
        try:
            varMin = np.min(var)
            varMax = np.max(var)
        except TypeError:
            varMin = None
            varMax = None
        except:
            varMin = min(var)
            varMax = max(var)
        # varMed = getMedian(var)
        infogeneral = 'len = {} (>20), lmid= {}, shape = {}'.format(l, lmid, shapeS)
    elif l > 0 and not isinstance(var, str):
        lmid = int(l/2)
        # varSample = str([x for x in var])
        varSample = "[" + ", ".join(f"{val:<5{fmt}}" for val in var) + "]"
        try:
            varMin = np.min(var)
            varMax = np.max(var)
        except TypeError:
            varMin = None
            varMax = None
        except:
            varMin = min(var)
            varMax = max(var)
        # varMed = getMedian(var)
        infogeneral = ' len = {}, lmid= {}, shape = {}'.format(l, lmid, shapeS)
    else:
        if isinstance(var, complex):
            fmt = ".3f"
            real = var.real
            imag = var.imag
            mod = np.sqrt(real**2 + imag**2)
            varSample = (f"{var}, var.real = {real:{fmt}}, "
                         f"var.imag = {imag:{fmt}}, |z| = {mod:{fmt}}")
        else:
            varSample = str(var)
        varMin = var
        # varMed = getMedian(var)
        varMax = var
        infogeneral = 'len = {} (shape = {})'.format(l, shapeS)
    result += header
    result += infogeneral
    # result += (' Value = \n' + varSample + '\ntype of = ' +
    #            str(type(var)) + ', min = ' + str(varMin) +
    #            ', med = ' + str(varMed) + ', max = '
    #            + str(varMax) + '\n')
    result += (f"Value = \n{varSample}\ntype of = {type(var)}"
               f", min = {varMin}, max = {varMax}\n")

    if DBG:
        if print_:
            print(result)
        else:
            return result

    return


class DbgInfo:
    """Class for getting helper DBG functions, parametrized

    Helper debugging functions can be parametrized for coding/debugging
    stage or for production ('silent' versions).
    """

    def __init__(self, DBG=False):
        """
            Args:
                DBG: bool - True for debugging, False for production stage.

            Returns:
                printd: function - parametrized function.
                varinfo: function - printing information about variable.
                printinfo: function - printing (diagnostic) information.
                printnumbers: function - printing numbers with information.
        """

        from functools import partial
        self.partial = partial
        self.DBG = DBG

    def __repr__(self):
        return f"DbgInfo(DBG={self.DBG})"

    def printd_(self, **kwargs):
        """Function returning `printd(..., DBG=DBG)` method"""

        return self.partial(printd, **kwargs, DBG=self.DBG)

    def printinfo_(self, **kwargs):
        """Function returning `printinfo(..., DBG=DBG)` method"""

        return self.partial(printinfo, DBG=self.DBG)

    def printnumbers_(self, **kwargs):
        """Function returning `printnumbers(..., DBG=DBG)` method"""

        return self.partial(printnumbers, DBG=True)

    def varinfo_(self, **kwargs):
        """Function returning `varinfo(..., DBG=DBG)` method"""

        return self.partial(varinfo, DBG=self.DBG)
