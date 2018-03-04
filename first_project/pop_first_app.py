import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


#Fake Pop Script
import random
from faker import Faker
from first_app.models import Webpages,AccessRecord,Topic

fakegen = Faker()

topics = ['Search','Marketplace','News','Socail','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        #get the topic for entry
        top = add_topic()
        #fake data for entery
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create webpage
        webpg=Webpages.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        #access record
        acc_rec =  AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print('populating done!')




