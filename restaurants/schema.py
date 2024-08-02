import graphene
from graphene_django.types import DjangoObjectType
from .models import Restaurant , Food # 导入您的模型



class FoodType(DjangoObjectType):
    class Meta:
        model = Food

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
    foods = graphene.List(FoodType)

    def resolve_foods(self, info):
        return Food.objects.filter(food_restaurant=self.id)

class Query(graphene.ObjectType):
    all_restaurants = graphene.List(RestaurantType)
    all_foods = graphene.List(FoodType)
    food_by_restaurant = graphene.List(FoodType, restaurant_id=graphene.Int())
    foods_by_restaurant_name = graphene.List(FoodType, restaurant_name=graphene.String(required=True))

    def resolve_all_restaurants(self, info):
        return Restaurant.objects.all()

    def resolve_all_foods(self, info):
        return Food.objects.all()

    def resolve_food_by_restaurant(self, info, restaurant_id):
        return Food.objects.filter(food_restaurant_id=restaurant_id)

    def resolve_foods_by_restaurant_name(self, info, restaurant_name):
        restaurant = Restaurant.objects.filter(name=restaurant_name).first()
        if restaurant:
            return Food.objects.filter(food_restaurant_id=restaurant.id)
        return []


schema = graphene.Schema(query=Query)