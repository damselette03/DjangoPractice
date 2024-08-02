from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=20) #餐廳名稱
    phone_number = models.CharField(max_length=15) #餐廳電話
    address = models.CharField(max_length=50, blank=True)  #餐廳地址
    
    def __str__(self): #新增
        return f'{self.name} 地址：{self.address}, 電話：{self.phone_number}'

class Food(models.Model):
    name = models.CharField(max_length=20) #食物名稱
    price=models.DecimalField(max_digits=3,decimal_places=0) #食物價錢
    is_spicy = models.BooleanField(default=False) #會不會辣
    food_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) #由哪個餐廳製作
    
    def __str__(self): #新增
        return self.name
