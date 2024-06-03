from utils.redis_client import RedisClient

redis_client = RedisClient()

if __name__ == '__main__':

    while True:
        commands = ['add_product', 'get_product', 'add_to_cart', 'remove_from_cart', 'get_cart_items']

        command = input(f"What can i do for you?\nCommands are {commands}\n")

        if command not in commands:
            print(f"Wrong ❗ the commands are:\n {commands}")

        if command == 'add_product':
            product_id = input("add product id:\n")
            product_name = input("add product title:\n")
            result = redis_client.set_product(product_id, product_name)
            print(result)

        elif command == 'get_product':
            product_id = input("get product id:\n")
            result = redis_client.get_product(product_id)
            print(result)

        elif command == 'add_to_cart':
            product_id = input("add product id:\n")
            quantity = input("quantity:\n")
            result = redis_client.add_to_cart(product_id, quantity)
            print(result)

        elif command == 'remove_from_cart':
            product_id = input("remove product id:\n")
            result = redis_client.remove_from_cart(product_id)
            print(result)

        elif command == 'get_cart_items':
            result = redis_client.get_cart_items()
            print(result)
