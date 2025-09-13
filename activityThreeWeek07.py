from abc import ABC, abstractmethod

# Abstract PaymentMethod class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete Payment Methods
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount:.2f}"

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount:.2f}"

class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing bank transfer payment of ${amount:.2f}"

class CryptoPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing crypto payment of ${amount:.2f}"

class GooglePayPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing Google Pay payment of ${amount:.2f}"

# Factory Design Pattern for creating PaymentMethod objects
class PaymentFactory:
    @staticmethod
    def create_payment_method(method_type):
        method_type = method_type.lower()
        if method_type == "creditcard":
            return CreditCardPayment()
        elif method_type == "paypal":
            return PayPalPayment()
        elif method_type == "banktransfer":
            return BankTransferPayment()
        elif method_type == "crypto":
            return CryptoPayment()
        elif method_type == "googlepay":
            return GooglePayPayment()
        else:
            raise ValueError(f"Unknown payment method: {method_type}")

# Singleton PaymentGateway
class PaymentGateway:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentGateway, cls).__new__(cls)
        return cls._instance

    def process_payment(self, amount, method_type):
        payment_method = PaymentFactory.create_payment_method(method_type)
        return payment_method.process_payment(amount)

# Example usage
if __name__ == "__main__":
    # Get the single instance of PaymentGateway
    gateway = PaymentGateway()

    # Process payments using different methods
    print(gateway.process_payment(100.50, "creditcard"))
    print(gateway.process_payment(200.00, "paypal"))
    print(gateway.process_payment(150.75, "banktransfer"))
    print(gateway.process_payment(300.00, "crypto"))
    print(gateway.process_payment(50.25, "googlepay"))

    # Verify singleton: another reference should be the same instance
    another_gateway = PaymentGateway()
    print(f"Is same instance: {gateway is another_gateway}")