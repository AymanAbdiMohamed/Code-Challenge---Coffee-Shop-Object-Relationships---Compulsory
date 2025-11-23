# Coffee Shop Domain Model

## Overview
This Python project models a Coffee Shop domain using object-oriented programming principles. The application defines three main entities: `Customer`, `Coffee`, and `Order`, and establishes relationships between them to simulate real-world interactions in a coffee shop.

The project demonstrates class design, method implementation, data validation, and object relationships in Python.

---

## Features
- **Customer**
  - Has a name (1-15 characters)
  - Can place multiple orders
  - Can list all coffees ordered
  - Can determine the most devoted customer for a coffee (`most_aficionado`)

- **Coffee**
  - Has a name (minimum 3 characters)
  - Can list all orders and unique customers
  - Can calculate total orders and average price

- **Order**
  - Associates a `Customer` with a `Coffee` and a `price` (1.0–10.0)
  - Ensures valid data and maintains a list of all orders

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AymanAbdiMohamed/Code-Challenge---Coffee-Shop-Object-Relationships---Compulsory
   cd coffee_shop
