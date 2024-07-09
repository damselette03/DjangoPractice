from django.contrib import admin
from restaurants.models import Restaurant, Food #新增

admin.site.register(Restaurant) #新增
admin.site.register(Food) #新增