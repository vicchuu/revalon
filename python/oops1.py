
from abc import ABC , abstractmethod

from datetime import datetime
class PaymentProcessor(ABC):
    @abstractmethod
    def otp_verification(self):
        pass

    @abstractmethod
    def validation(self):
        pass


class Creditcardprocessor(PaymentProcessor):

    def __init__(self,card_number,name,total_amount):
        self.total_cash = total_amount
        self.card_number = card_number
        self.name =  name


    def process_payment(self,amount):

        print(f"amount {amount} is debited from the account in {datetime.now()}")

    def log_payment(func):
        def wrapper(*args , **kwargs):
            print(f"logging function called {func.__name__}")
            return func(*args ,**kwargs)
        return wrapper

    def validation(func):
        def wrapper(*args,**kwargs):
            print(f"validation done..{func.__name__}")
            return func(*args,**kwargs)
        return wrapper

    @log_payment
    @validation
    def otp_verification(self):
        print(f"OTP verification done")



ccp = Creditcardprocessor(card_number=123456,name="vishnu",total_amount=1000)
ccp.otp_verification()

def print_generators(num):

    i =0
    while i<num:
        yield i
        i = i+1

#for t in print_generators(10):
g = print_generators(10)
#while g<10:
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
g.close()
print(next(g))
