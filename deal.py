from base import BaseClass


class Sale(BaseClass):
    def __init__(self,price_oer_meter,discountable,convertable,*args,**kwargs):
        self.price_per_meter= price_oer_meter
        self.discountable = discountable
        self.convertable = convertable
        super(Sale, self).__init__(*args,**kwargs)


class Rent(BaseClass):
    def __init__(self,initial_price,monthly_price,discountable,convertable,*args,**kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.discountable = discountable
        self.convertable = convertable
        super(Rent, self).__init__(*args,**kwargs)




