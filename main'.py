from user import User
from random import choice

first_names = ['amir','mohammadamin','erfan']
last_name = ['madadi','moradi']
phone_numbers = ['0912424823','0933131247','092649632232','09242347732']
if __name__ =="__main__":
    for mobile in phone_numbers:
        User(choice(first_names),choice(last_name),mobile)

    for user in User.object_list:
        print(user.get_fullname)