🛍️ Shopping Cart with Redis Data Structures 🛍️
=====================================================

**Project Overview**
--------------------

This project simulates a simple shopping cart system using various Redis data structures. It allows users to add, remove, and view items in their cart.

**Project Structure**
---------------------

* `requirements.txt`: Specifies the Python libraries required for the project, including Redis.
* `main.py`: The main script where you'll implement the shopping cart functionalities.
* `utils/`: Directory containing utility functions.
	+ `redis_client.py`: Handles connecting to the Redis server and provides methods for interacting with different data structures.

**Functionality**
----------------

* Users can add items to the cart (product name, quantity).
* Users can remove items from the cart.
* Users can view all items in the cart (including quantity).
* Handles situations where a user tries to add a non-existent product or removes an item that's not in the cart.

**Data Structures**
-------------------

* **Products (Hash)**: Stores product information (e.g., product_id, name, price) using a Redis Hash.
* **Cart (Sorted Set)**: Stores items in the user's cart using a Redis Sorted Set, allowing easy retrieval of items and their quantities based on the score.

**Additional Considerations**
-----------------------------

* Implements error handling for potential issues like connection failures or invalid user input.
* Considers adding functionality to set expiration times for cart items to simulate a session timeout.
* Explores using Redis Pub/Sub for broadcasting cart updates across multiple clients (optional).

**Getting Started**
-------------------

1. Install the required Python libraries specified in `requirements.txt`.
2. Run `main.py` to start the shopping cart system.
3. Interact with the system using the provided functionality.

**Redis Documentation**
----------------------

For detailed information on each Redis data structure and its commands, consult the official Redis documentation: https://redis.io/docs/latest/commands/

**Search Results**
-----------------

 https://redis.io/docs/latest/commands/

This project provides a great starting point for learning Redis data structures in Python, utilizing Hashes and Sorted Sets for practical use cases. Remember to consult the official Redis documentation for detailed information on each data structure and its commands.