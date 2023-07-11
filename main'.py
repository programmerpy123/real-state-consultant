from user import User
from random import choice
from estate import Apartement,House,Store
from region import  Region
from advertisment import RentApartement, SaleApartement
first_names = ['amir','mohammadamin','erfan']
last_name = ['madadi','moradi']
phone_numbers = ['0912424823','0933131247','092649632232','09242347732']
if __name__ == "__main__":

    for mobile in phone_numbers:
        User(choice(first_names),choice(last_name),mobile)

    for user in User.object_list:
        print(user.get_fullname)

    apt1 = Apartement(user=User.object_list[0],area=80, room_count=2,built_year=1387,has_parking=True,has_elevator=True,
                      region=Region(name='81.3'),floor=2,address='54 street')
    apt1.show_description()

    house1= House(user=User.object_list[1],region=Region(name='34.2'), has_yard=True,floors_count=2,show_description='its beautiful house dont miss it',
                  address='32 street',room_count=2,area='23.2',built_year='1385')

    house1.show_description()

    hs1 = Store(user=User.object_list[2], region=Region(name='34.2'),description='goooood',
                   address='32 street', room_count=2, area='23.2', built_year='1385')

    hs1.show_description()

    apartement_sale = SaleApartement(user=User.object_list[0],area=80, room_count=2,built_year=1387,has_parking=True,has_elevator=True,
                      region=Region(name='81.3'),floor=2,address='54 street',
                                     price_per_meter=2,discountable=True,convertable=False)

    apartement_sale.show_more_detail()
    print(apartement_sale.manager.search(area=89))