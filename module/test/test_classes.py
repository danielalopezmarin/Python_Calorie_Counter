from unittest import TestCase

from module.orders import Order 


class OrderTestCase(TestCase):
    def test_order_id_increment(self):
        initial_counter = Order.counter
        order_1 = Order ([])
        self.assertEqual (order_1.order_id, f"order-{initial_counter + 1}")
        order_2 = Order ([])
        self.assertEqual(order_1.order_id, f"order-{initial_counter + 2}")
        
