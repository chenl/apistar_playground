from apistar import typesystem


class Rating(typesystem.Integer):
    minimum = 1
    maximum = 5


class ProductSize(typesystem.Enum):
    enum = ['small', 'medium', 'large']


class Product(typesystem.Object):
    properties = {
        'name': typesystem.string(max_length=100),
        # ^ user lowercase functions for inline declarations
        'rating': Rating,
        'in_stock': typesystem.Boolean,
        'size': ProductSize,
    }
