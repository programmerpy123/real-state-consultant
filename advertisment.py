from abc import ABC

from base import BaseClass
from estate import House,Apartement, Store
from deal import Sale, Rent
from abc import ABC , abstractmethod


class Advertisment(ABC):
    @abstractmethod
    def show_more_detail(self):
        pass

class SaleHouse(BaseClass,Advertisment, House, Sale):
    def show_more_detail(self):
        print("---------------------------------------------")
        self.show_description()
        self.show_detial()


class SaleApartement(BaseClass,Advertisment, Apartement,Sale):
    def show_more_detail(self):
        print("---------------------------------------------")
        self.show_description()
        self.show_detial()

    def __str__(self):

        return f"{self.price_per_meter}\t{self.region}\t{self.show_more_detail()}"


class SaleStore(BaseClass, Store,Sale):
    pass


class RentHouse(BaseClass, House,Rent):
    pass


class RentApartement(BaseClass, Apartement,Rent):
    pass


class RentStore(BaseClass, Store,Rent):
    pass

