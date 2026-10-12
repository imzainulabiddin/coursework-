from dataclasses import dataclass, field
from typing import List

@dataclass
class CartItem:
    name: str
    price: float
    quantity: int = 1

class ShoppingCart:
    def __init__(self):
        """Initialize an empty list to store items for THIS specific cart."""
        self.items: List[CartItem] = []

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Add a product with its price and quantity to the cart."""
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be non-negative and quantity must be positive.")
        self.items.append(CartItem(name, price, quantity))

    def remove_item(self, name: str) -> None:
        """Remove an item from the cart by its name."""
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self) -> float:
        """Calculate and return the total cost of all items in the cart."""
        return sum(item.price * item.quantity for item in self.items)


# --- Testing the ShoppingCart ---

if __name__ == "__main__":
    
    cart1 = ShoppingCart()
    cart2 = ShoppingCart()


    cart1.add_item("Laptop", 1200.50, 1)
    cart1.add_item("Mouse", 25.99, 2)
    cart1.add_item("Keyboard", 45.00, 1)


    cart2.add_item("Monitor", 300.00, 2)
    cart2.add_item("HDMI Cable", 15.50, 3)


    print(f"Cart 1 Total: ${cart1.calculate_total():.2f}")
    print(f"Cart 2 Total: ${cart2.calculate_total():.2f}")


    cart1.remove_item("Mouse")
    print(f"Cart 1 Total after removing Mouse: ${cart1.calculate_total():.2f}")