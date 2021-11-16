# test_portfolio.py
from Portfolio import Portfolio
from Portfolio import Shares
import pytest

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost() == 0 

def test_buy_one_stock():
    p = Portfolio()
    ibm = Shares("IBM", 100, 176.48)
    p.buy(ibm)
    assert p.cost() == 17648.0

def test_buy_two_stock():
    p = Portfolio()
    ibm = Shares("IBM", 100, 176.48)
    hpq = Shares("HPQ", 100, 36.15)
    p.buy(ibm)
    p.buy(hpq)
    assert p.cost() == 21263.0

def test_not_enough_argument_to_buy():
    p = Portfolio("HPQ", 100, 36.15)
    with pytest.raises(TypeError):
        p.buy('IBM')

    """
    try:
        p.buy("IBM")
    except TypeError:
        pass
    else:
        assert False, "didnt get an exception"
    """
    
