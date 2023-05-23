class DiscountError(Exception):
    pass


def integer_discount(number: int = 60):

    def inner_function(function):
        def wrapper(price: int, discount: int) -> int:
            return function(price, discount / number)

        return wrapper
    return inner_function


@integer_discount(600)
def apply_discount(price: int, discount: float = 0.0) -> int:
    """Calculates the Final Price After Discount"""
    final_price = int(price * (1 - discount))
    if not 0 <= final_price < price:
        raise DiscountError("Invalid price")

    return final_price


print(apply_discount(1000, 30))
