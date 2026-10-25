class Product:
    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name
        self.base_price = base_price

    def calculate_price(self):
        return self.base_price
    def get_info(self):
        return "{} -> PKR {}".format(self.item_name, self.calculate_price())


class PhysicalProduct(Product):
    def __init__(self, item_id, item_name, base_price, shipping_fee):
        super().__init__(item_id, item_name, base_price)
        self.shipping_fee = shipping_fee

    def calculate_price(self):
        return self.base_price + self.shipping_fee

    def get_info(self):
        return "{} (Physical) -> PKR {}".format(
            self.item_name, self.calculate_price()
        )


class DigitalProduct(Product):
    def __init__(self, item_id, item_name, base_price, discount):
        super().__init__(item_id, item_name, base_price)
        self.discount = discount

    def calculate_price(self):
        discount_amount = self.base_price * (self.discount / 100)
        return int(self.base_price - discount_amount)

    def get_info(self):
        return "{} (Digital, {}% OFF) -> PKR {}".format(
            self.item_name, self.discount, self.calculate_price()
        )

class CardPayment:
    def __init__(self, card_num, owner_name):
        self.card_num = card_num
        self.owner_name = owner_name

    def pay_bill(self, total_amount):
        bank_fee = int(total_amount * 0.02)
        final_bill = int(total_amount + bank_fee)
        hidden_card = "****-****-****-{}".format(self.card_num[-4:])

        print("\n--- Card Payment Processing ---")
        print("Card Holder : {}".format(self.owner_name))
        print("Card Number : {}".format(hidden_card))
        print("Subtotal    : PKR {}".format(int(total_amount)))
        print("Card Fee 2% : PKR {}".format(bank_fee))
        print("Total Paid  : PKR {}".format(final_bill))
        print("Status      : Payment Successful!")
        return True
class CashOnDelivery:
    def __init__(self, address):
        self.address = address

    def pay_bill(self, total_amount):
        cod_charge = 150
        final_bill = int(total_amount + cod_charge)

        print("\n--- Cash on Delivery ---")
        print("Address     : {}".format(self.address))
        print("Subtotal    : PKR {}".format(int(total_amount)))
        print("COD Charge  : PKR {}".format(cod_charge))
        print("Collect Cash: PKR {}".format(final_bill))
        print("Status      : Order Placed (Pending Cash Collection)")
        return True

class Order:
    def __init__(self, order_no):
        self.order_no = order_no
        self.items_list = []

    def add_item(self, item):
        self.items_list.append(item)
        print("Success: '{}' added to cart.".format(item.item_name))

    def get_total_price(self):
        bill = 0
        for item in self.items_list:
            bill += item.calculate_price()
        return int(bill)

    def print_bill(self):
        print("------ Cart Summary (Order #{}) --------".format(self.order_no))
        print("==========================================")
        if not self.items_list:
            print("Cart is empty.")
            return
        count = 1
        for item in self.items_list:
            print("{}. {}".format(count, item.get_info()))
            count = count + 1

        print("------------------------------------------")
        print("Subtotal Amount: PKR {}".format(self.get_total_price()))

    def checkout(self, payment_option):
        self.print_bill()
        bill_amount = self.get_total_price()

        if bill_amount > 0:
            payment_option.pay_bill(bill_amount)
            print("\nCheckout Completed Successfully!\n")
        else:
            print("\nCheckout Failed: Cart is empty.")


catalog = {
    "1": PhysicalProduct("P101", "Keyboard", 2500, 200),
    "2": DigitalProduct("D101", "E-Book", 1200, 10),
    "3": PhysicalProduct("P102", "Book", 800, 150),
    "4": DigitalProduct("D102", "Online Course", 3000, 15),
}
user_order = Order("1001")
while True:
    print("\n==========================================")
    print("      ONLINE SHOPPING SYSTEM MENU         ")
    print("1. View Store Products")
    print("2. Add Product to Cart")
    print("3. View Cart Summary")
    print("4. Proceed to Checkout")
    print("5. Exit")

    choice = input("\nEnter choice (1-5): ").strip()

    if choice == "1":
        print("\n--- AVAILABLE PRODUCTS ---")
        for product_id in catalog:
            print("{}. {}".format(product_id, catalog[product_id].get_info()))

    elif choice == "2":
        print("\n--- SELECT PRODUCT TO ADD ---")
        for product_id in catalog:
            print("{}. {}".format(product_id, catalog[product_id].item_name))

        num = input("\nEnter product number (1-4): ").strip()
        if num in catalog:
            user_order.add_item(catalog[num])
        else:
            print("Invalid choice.")

    elif choice == "3":
        user_order.print_bill()

    elif choice == "4":
        if not user_order.items_list:
            print("\nCart is empty! Add products first.")
            continue

        print("\n--- PAYMENT METHOD ---")
        print("1. Card Payment")
        print("2. Cash on Delivery")

        pay_choice = input("Select payment method (1-2): ").strip()

        if pay_choice == "1":
            name = input("Enter Card Holder Name: ").strip()
            card_num = input("Enter 16-Digit Card Number: ").strip()
            payment = CardPayment(card_num, name)
            user_order.checkout(payment)
            break

        elif pay_choice == "2":
            address = input("Enter Delivery Address: ").strip()
            payment = CashOnDelivery(address)
            user_order.checkout(payment)
            break
        else:
            print("Invalid payment choice.")

    elif choice == "5":
        print("\nExiting system.")
        break
    else:
        print("Invalid choice, enter a number from 1 to 5.")