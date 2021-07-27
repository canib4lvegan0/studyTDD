

class Calculator:

    def __init__(self):
        pass

    def func_sum(self, n1: float, n2: float) -> (float, None):

        if type(n1) in (float, int) and type(n2) in (float, int):
            return n1 + n2

        return None

    def func_sub(self, n1: float, n2: float) -> (float, None):

        if type(n1) in (float, int) and type(n2) in (float, int):
            return n1 - n2

        return None

    def func_mul(self, n1: float, n2: float) -> (float, None):

        if type(n1) in (float, int) and type(n2) in (float, int):
            return n1 * n2

        return None

    def func_div(self, n1: float, n2: float) -> (float, None):

        if type(n1) in (float, int) and type(n2) in (float, int):
            return n1 / n2

        return None
