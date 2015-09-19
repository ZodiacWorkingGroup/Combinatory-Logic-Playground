class Result:
    def __init__(self, value, combinators):
        self.value = value
        self.combinators = combinators

class Expression:  # Credit to Tanner Swett
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class CombinatorExpression(Expression):
    def __init__(self, comb):
        self.comb = comb

    def eval(self, combinators):
        if self in combinators:
            return self.comb
        else:
            raise ValueError('Invalid Combinator Encountered')


class ApplyExpression(Expression):
    def __init__(self, comb, argument):
        self.comb = comb
        self.arg = argument

    def eval(self, combinators):
        if self.comb == 'S':
            return Result(None, combinators)
        elif self.comb == 'K':
            return Result(self.arg.eval(), combinators)
        else:
            return Result(combinators[self.comb].eval(combinators), combinators)