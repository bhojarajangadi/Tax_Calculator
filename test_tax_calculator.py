import pytest
from tax_calculator import taxable_income, tax, net_income, tax_percentage

def test_taxable_income():
    assert taxable_income(500000) == 500000

def test_negative_income():
    with pytest.raises(ValueError):
        taxable_income(-1000)

def test_zero_tax():
    assert tax(300000) == 0

def test_tax_calculation():
    assert tax(1000000) == 40000

def test_net_income():
    assert net_income(1000000) == 960000

def test_tax_percentage():
    assert tax_percentage(1000000) == 4.0