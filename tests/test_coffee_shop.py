import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from customer import Customer
from coffee import Coffee


def test_customer_creation():
    c = Customer("John")
    assert c.name == "John"
    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLong")


def test_coffee_creation():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"
    with pytest.raises(ValueError):
        Coffee("AB")


def test_order_creation_and_relationships():
    cust = Customer("Alice")
    coffee = Coffee("Latte")
    order = cust.create_order(coffee, 5.0)
    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 5.0
    assert cust.orders() == [order]
    assert cust.coffees() == [coffee]
    assert coffee.orders() == [order]
    assert coffee.customers() == [cust]


def test_aggregate_methods():
    cust = Customer("Bob")
    coffee = Coffee("Espresso")
    cust.create_order(coffee, 4.0)
    cust.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0


def test_most_aficionado():
    cust1 = Customer("A")
    cust2 = Customer("B")
    coffee = Coffee("Latte")
    cust1.create_order(coffee, 3.0)
    cust1.create_order(coffee, 2.0)
    cust2.create_order(coffee, 4.0)
    assert Customer.most_aficionado(coffee) == cust1
