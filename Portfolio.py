class Shares:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price



class Portfolio:

    def __init__(self):
        self._stocks = [] 

    def buy(self, shares):
        self._stocks.append(shares)

    def cost(self):
        cost = 0
        for stock in self._stocks:
            shares = stock.number
            price = stock.price
            cost = cost + shares * price
        return cost