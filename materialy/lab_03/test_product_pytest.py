# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product.

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    return Product("Laptop", 2999.99, 10)


# --- Testy podstawowe ---

def test_is_available(product):
    assert product.is_available() is True


def test_is_not_available_when_empty():
    empty = Product("Brak", 9.99, 0)
    assert empty.is_available() is False


def test_total_value(product):
    assert product.total_value() == pytest.approx(2999.99 * 10)


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    (5,   15),
    (0,   10),
    (100, 110),
    (1,   11),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity


@pytest.mark.parametrize("amount, expected_quantity", [
    (1,  9),
    (5,  5),
    (10, 0),
])
def test_remove_stock_parametrized(product, amount, expected_quantity):
    product.remove_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(100)


def test_add_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.add_stock(-1)


def test_remove_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(-1)

