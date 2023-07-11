from base import BaseClass
from abc import ABC ,abstractmethod


class Sale(ABC):
    def __init__(self,price_per_meter,discountable,convertable,*args,**kwargs):
        self.price_per_meter= price_per_meter
        self.discountable = discountable
        self.convertable = convertable
        super(Sale, self).__init__(*args,**kwargs)

    def show_detial(self):
        print(f"price is {self.price_per_meter} and discountable:{self.discountable}, and convertable:{self.convertable}")


class Rent(ABC):
    def __init__(self,initial_price,monthly_price,discountable,convertable,*args,**kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.discountable = discountable
        self.convertable = convertable
        super(Rent, self).__init__(*args,**kwargs)





