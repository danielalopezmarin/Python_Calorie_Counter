from module.functions import calorie_counter, price_counter


class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 0

    def __init__(self, items, date=None):
        Order.counter += 1
        self.order_id = f"order-{Order.counter}"
        self.items = items
        self.calories = None
        self._price = None


        self.order_accepted = False
        self.order_refused_reason = None
        self.date = date 
     

    @property
    def calories (self):
        pass

    @property
    def price (self):
        pass

