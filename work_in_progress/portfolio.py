# portfolio.py
# source: https://github.com/dabeaz-course/practical-python/blob/master/Solutions/8_2/portfolio.py
import fileparse
import stock


class Portfolio:


    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name', 'shares', 'price'],
                                        types=[str, int, float],
                                        **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self


