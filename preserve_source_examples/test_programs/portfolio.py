# portfolio.py
# source: https://github.com/dabeaz-course/practical-python/blob/master/Solutions/8_2/portfolio.py
import fileparse
import stock


class Portfolio:
    def __init__(self):
        self._holdings = []

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name', 'shares', 'price'], # <-- See this line of AST unparse results
                                        types=[str, int, float],
                                        **opts)
                                        # <-- See this line is missing in of AST unparse results
        for d in portdicts:
            self.append(stock.Stock(**d))

        return self

    def append(self, holding):
        self._holdings.append(holding)

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    @property
    def total_cost(self):
        return sum(s.shares * s.price for s in self._holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares



