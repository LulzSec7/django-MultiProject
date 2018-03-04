import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')


import django
django.setup()

#pop with fake data
from faker import Faker
from appTwo.models import User

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()
        fake_detail = User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]


if __name__ =='__main__':
    print('populating script!')
    populate(20)
    print('populating done!')