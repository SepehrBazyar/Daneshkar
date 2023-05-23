def apply_discount(price, discount):
    final_price = int(price * (1 - discount))
    if not 0 <= final_price < final_price < price:
        raise ValueError('Invalid Discount')

    return final_price
