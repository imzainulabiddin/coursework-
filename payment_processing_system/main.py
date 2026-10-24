from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product(ABC):
    name: str
    price: Decimal

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Product name cannot be empty.")
        if self.price < Decimal("0"):
            raise ValueError("Product price cannot be negative.")

    @abstractmethod
    def unit_total(self) -> Decimal:
        """Return the per-unit price including product-specific costs."""


@dataclass(frozen=True)
class PhysicalProduct(Product):
    shipping_fee: Decimal = Decimal("0.00")

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.shipping_fee < Decimal("0"):
            raise ValueError("Shipping fee cannot be negative.")

    def unit_total(self) -> Decimal:
        return self.price + self.shipping_fee


@dataclass(frozen=True)
class DigitalProduct(Product):
    def unit_total(self) -> Decimal:
        return self.price


@dataclass(frozen=True)
class OrderItem:
    product: Product
    quantity: int = 1

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive.")

    @property
    def subtotal(self) -> Decimal:
        return self.product.unit_total() * self.quantity


@dataclass
class Order:
    customer_name: str
    items: list[OrderItem]
    is_paid: bool = False

    def __post_init__(self) -> None:
        if not self.customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        if not self.items:
            raise ValueError("An order must contain at least one item.")

    @property
    def total(self) -> Decimal:
        return sum((item.subtotal for item in self.items), Decimal("0.00"))


class Customer:
    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Customer name cannot be empty.")
        self.name = name

    def place_order(self, items: list[OrderItem]) -> Order:
        return Order(customer_name=self.name, items=items)


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: Decimal) -> str:
        """Process a payment and return a confirmation message."""


class CardPayment(PaymentMethod):
    def pay(self, amount: Decimal) -> str:
        return f"Card payment approved: ${amount:.2f}"


class CashPayment(PaymentMethod):
    def pay(self, amount: Decimal) -> str:
        return f"Cash payment received: ${amount:.2f}"


class CheckoutService:
    def checkout(self, order: Order, payment_method: PaymentMethod) -> None:
        if order.is_paid:
            raise ValueError("This order has already been paid.")

        print(f"Order for {order.customer_name}:")
        for item in order.items:
            print(
                f"  {item.product.name} x{item.quantity}: "
                f"${item.subtotal:.2f}"
            )
        print(f"Total: ${order.total:.2f}")
        print(payment_method.pay(order.total))
        order.is_paid = True
        print("Checkout complete.\n")


def main() -> None:
    keyboard = PhysicalProduct(
        name="Keyboard",
        price=Decimal("45.00"),
        shipping_fee=Decimal("5.00"),
    )
    book = PhysicalProduct(
        name="Python Programming Book",
        price=Decimal("30.00"),
        shipping_fee=Decimal("4.00"),
    )
    ebook = DigitalProduct(name="Python E-book", price=Decimal("15.00"))

    customer = Customer("Haris Rauf")
    order_items = [
        OrderItem(keyboard),
        OrderItem(book),
        OrderItem(ebook, quantity=2),
    ]
    checkout = CheckoutService()

    print("=== Card checkout ===")
    card_order = customer.place_order(order_items)
    checkout.checkout(card_order, CardPayment())

    print("=== Cash checkout ===")
    cash_order = customer.place_order(order_items)
    checkout.checkout(cash_order, CashPayment())


if __name__ == "__main__":
    main()
