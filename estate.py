from base import BaseClass
from abc import ABC, abstractmethod


class EstateAbstract(ABC):
    def __init__(self, user, area, room_count,built_year, region,address,*args,**kwargs):
        self.user = user
        self.area = area
        self.room_count = room_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args,**kwargs)

    @abstractmethod
    def show_description(self):
        pass


class Apartement(EstateAbstract):
    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args,**kwargs)

    def show_description(self):
        print(f"apartement")


class House(EstateAbstract):
    def __init__(self, has_yard, floors_count, show_description, *args, **kwargs):
        self.has_yard = has_yard
        self.floors_count = floors_count
        self.show_descripton = show_description
        super(House, self).__init__(*args,**kwargs)

    def show_description(self):
        print(f"House")


class Store(EstateAbstract):
    def __init__(self, description,*args,**kwargs):
        self.description = description
        super(Store, self).__init__(*args,**kwargs)

    def show_description(self):
        print(f"store")

