from dataclasses import dataclass

@dataclass
class Order:
    customer_name: str
    shipping_address: str
    items: list

@dataclass
class Item:
    name: str
    quantity: int
    price: float

class PriceCalculator:
    @staticmethod
    def get_sub_total(order: Order):
        sub_total = 0.0
        for item in order.items:
            sub_total += item.quantity * item.price
        return sub_total

    @staticmethod
    def get_total(order: Order, sub_total: float, tax_rate: float, percent_discounts: list = [], flat_discounts: list = []):
        total = sub_total
        for discount in flat_discounts:
            total -= discount
        for discount in percent_discounts:
            total *= (1.0 - discount)
        total *= 1 + tax_rate
        return total

class EmailHandler:
    @staticmethod
    def send_confirmation(order, email):
        print(f"mailto:{email} Your order containing {order.items} is confirmed! It will be shipped to {order.shipping_address}.")

class InventoryHandler:
    @staticmethod
    def items_available(order: Order, inventory: list):
        for item in order.items:
            for inv_item in inventory:
                if item.name == inv_item.name and item.quantity <= inv_item.quantity:
                    return True
        return False

    @staticmethod
    def process_order(order: Order, inventory: list):
        for item in order.items:
            for inv_item in inventory:
                if inv_item.name == item.name:
                    inv_item.quantity - item.quantity
                    break

def main():
    customer_name = "Johny Appleseed"
    address = "One Apple Park Way Cupertino, CA 95014"
    items = [Item("Galaxy S24", 100000, 799.99), Item("Google Pixel 8", 9999, 699.99)]
    tax_rate = 0.0725
    email = "jappleseed@icloud.com"

    inventory = [Item("Galaxy S24", 1000009, 799.99), Item("Google Pixel 8", 99999, 699.99)]
    
    order = Order(customer_name, address, items)
    sub_total = PriceCalculator.get_sub_total(order)
    total = PriceCalculator.get_total(order, sub_total, tax_rate)
    if (InventoryHandler.items_available(order, inventory)):
        print(f"Sub-total is: ${sub_total}")
        print(f"Total is : ${total}")
        EmailHandler.send_confirmation(order, email)
        InventoryHandler.process_order(order, inventory)


if __name__=="__main__":
    main()