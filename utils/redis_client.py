import logging

import redis


class RedisClient:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)
        logging.debug('Redis client initialized')
        # self.r.flushdb()
        # logging.warning("Redis client flushed")

    def set_product(self, product_id, product_name):
        return self.r.set(product_id, product_name)

    def get_product(self, product_id):
        return self.r.get(product_id)

    def add_to_cart(self, product_id, quantity):
        # Function to add product to cart (Sorted Set)
        return self.r.zadd("cart", {product_id: quantity})

    def remove_from_cart(self, product_id):
        # Function to remove product from cart (Sorted Set)
        return self.r.zrem('cart', product_id)

    def get_cart_items(self):
        # Function to retrieve all items (product_id, quantity) from cart (Sorted Set)
        return self.r.zrange('cart', 0, -1, withscores=True)
