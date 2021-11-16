class Portfolio:

    def __inif__(self):
        self._stocks = {} 

    def buy(self, name, shares, price):
        stock = {"name": name, "shares": shares, "price": price}
        self._stocks[name] = stock

    def cost(self):
        cost = 0
        for stock in self._stocks:
            shares = stock["shares"]
            price = stock["price"]
            cost = cost + shares * price
        return cost