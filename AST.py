class Equality:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class RawCombinator(Equality):
    def __init__(self, comb):
        self.comb = comb

    def eval(self, combinators):
        return self.comb


class CombinatorExp(Equality):
    def __init__(self, comb, argument):
        self.comb = comb
        self.arg = argument

    def eval(self, combinators):
        if self.comb == 'S':
            return
        elif self.comb == 'K':
            if type(self.arg) == RawCombinator:
                return self.arg
            else:
                return self.arg.eval()
        else:
            return combinators[self.comb].eval(combinators)
