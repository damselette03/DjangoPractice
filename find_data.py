import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

import django
django.setup()

from restaurants.models import Restaurant , Food

all_Restaurants = Restaurant.objects.all()
Restaurant1 = all_Restaurants.get(name='二號店')
print(Restaurant1)