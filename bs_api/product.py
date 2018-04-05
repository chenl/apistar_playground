from typing import List
from apistar import Route
from bs_api import types

product_id = 0
products = {}


def create_product(product: types.Product):
    global product_id, products
    products[product_id] = product
    return {'id': product_id, 'product': product}


def get_all_products() -> List[types.Product]:
    return list(products.items())


routes = [
    Route('/', 'GET', get_all_products),
    Route('/', 'POST', create_product),
]
