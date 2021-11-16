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

"""
Within it, define a new class called Portfolio which:
has a method called buy, which adds a new stock to the portfolio, taking 3 arguments
name, a str, the symbol of the stock which is being bought
shares, an int, the quantity which is being bought
price, a float, the price paid per share
and has a second method called cost which returns a float, the total cost paid for all stocks in the portfolio
Consider that to implement the cost method, you'll need to be storing the purchases made each time the buy method is called somewhere.
 You may do so by any means convenient to you.
Commit this file to your repository and push it to GitHub using GitHub Desktop, with a suitable commit message.
"""