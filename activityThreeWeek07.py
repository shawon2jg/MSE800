from abc import ABC, abstractmethod
from enum import Enum

# region Enum for payment method types
class PaymentType(Enum):
    CREDIT_CARD = "creditcard"
    PAYPAL = "paypal"
    BANK_TRANSFER = "banktransfer"
    CRYPTO = "crypto"
    GOOGLE_PAY = "googlepay"
# endregion

# region Abstract PaymentMethod class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
# endregion

# region Concrete Payment Methods
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount:.2f} with 3D Secure authentication"

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount:.2f} via PayPal API"

class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing bank transfer payment of ${amount:.2f} with IBAN verification"

class CryptoPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing crypto payment of ${amount:.2f} via blockchain transaction"

class GooglePayPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing Google Pay payment of ${amount:.2f} with tokenization"
# endregion

# region Abstract Factory for Payment Methods
class PaymentMethodFactory(ABC):
    @abstractmethod
    def create_payment_method(self):
        pass
# endregion

# region Concrete Factories for each Payment Type
class CreditCardFactory(PaymentMethodFactory):
    def create_payment_method(self):
        return CreditCardPayment()

class PayPalFactory(PaymentMethodFactory):
    def create_payment_method(self):
        return PayPalPayment()

class BankTransferFactory(PaymentMethodFactory):
    def create_payment_method(self):
        return BankTransferPayment()

class CryptoFactory(PaymentMethodFactory):
    def create_payment_method(self):
        return CryptoPayment()

class GooglePayFactory(PaymentMethodFactory):
    def create_payment_method(self):
        return GooglePayPayment()
# endregion

# region Factory Producer to select appropriate factory
class PaymentFactoryProducer:
    @staticmethod
    def get_factory(payment_type):
        payment_type = payment_type.lower()
        factories = {
            PaymentType.CREDIT_CARD.value: CreditCardFactory(),
            PaymentType.PAYPAL.value: PayPalFactory(),
            PaymentType.BANK_TRANSFER.value: BankTransferFactory(),
            PaymentType.CRYPTO.value: CryptoFactory(),
            PaymentType.GOOGLE_PAY.value: GooglePayFactory()
        }
        factory = factories.get(payment_type)
        if factory is None:
            raise ValueError(f"Unknown payment method: {payment_type}")
        return factory
# endregion

# region Singleton PaymentGateway
class PaymentGateway:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentGateway, cls).__new__(cls)
        return cls._instance

    def process_payment(self, amount, method_type):
        factory = PaymentFactoryProducer.get_factory(method_type)
        payment_method = factory.create_payment_method()
        return payment_method.process_payment(amount)
# endregion

if __name__ == "__main__":
    # Get the single instance of PaymentGateway
    gateway = PaymentGateway()

    # Process payments using different methods
    print(gateway.process_payment(100.50, "creditcard"))
    print(gateway.process_payment(200.00, "paypal"))
    print(gateway.process_payment(150.75, "banktransfer"))
    print(gateway.process_payment(300.00, "crypto"))
    print(gateway.process_payment(50.25, "googlepay"))
