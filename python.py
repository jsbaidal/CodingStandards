"""
This module implements a simple shopping cart system, which allows the user to add items,
apply discounts, and calculate the final total after tax.
"""

class Item:
    """Represents an item in the shopping cart."""

    def __init__(self, name, price, qty):
        """Initialize an item with name, price, quantity, and other properties."""
        self.name = name
        self.price = price
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def get_total(self):
        """Calculate the total price for the item."""
        return self.price * self.qty

    def get_discounted_price(self):
        """Calculate a discounted price for the item."""
        return self.price * self.qty * 0.6


class ShoppingCart:
    """Represents a shopping cart containing multiple items."""

    def __init__(self):
        """Initialize the shopping cart with default values."""
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"

    def add_item(self, item):
        """Add an item to the shopping cart."""
        self.items.append(item)

    def calculate_subtotal(self):
        """Calculate the subtotal of the items in the shopping cart."""
        subtotal = 0
        for item in self.items:
            subtotal += item.get_total()
        return subtotal

    def apply_discounts(self, subtotal, is_member):
        """Apply discounts based on membership and the subtotal."""
        if is_member:
            subtotal -= subtotal * self.member_discount
        if subtotal > 100:
            subtotal -= self.big_spender_discount
        return subtotal

    def calculate_total(self, is_member, has_coupon):
        """Calculate the final total after applying discounts and tax."""
        subtotal = self.calculate_subtotal()
        subtotal = self.apply_discounts(subtotal, is_member)
        total = subtotal + (subtotal * self.tax_rate)
        if has_coupon:
            total -= total * self.coupon_discount
        return total


def main():
    """Main function to execute the shopping cart logic."""
    cart = ShoppingCart()
    item1 = Item("Apple", 1.5, 10)
    item2 = Item("Banana", 0.5, 5)
    item3 = Item("Laptop", 1000.0, 1)

    item3.category = "electronics"
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    is_member = True
    has_coupon = True

    total = cart.calculate_total(is_member, has_coupon)

    if total < 0:
        print("Error in calculation!")
    else:
        print(f"The total price is: ${int(total)}")


if __name__ == "__main__":
    main()
