from rest_framework import serializers
from . import models


class RestaurantSerializer(serializers.ModelSerializer):
    # Serializer for the Restaurant model, in fields we specify the model attributes we want to
    # deserialize and serialize
    class Meta:
        model = models.Restaurant
        fields = ['id', 'name', 'direction', 'phone']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    # As each recipe has an image thumbnail we deal with the serialization of the image in the function
    # When getting a recipe I want an 'ingredients' field, the value of this field is the return of the get_ingredients
    # function that serializes the ingredients for the recipe.
    ingredients = serializers.SerializerMethodField('get_ingredients')

    def get_ingredients(self, recipe):
        try:
            recipe_ingredients = models.Ingredient.objects.filter(recipe__id=recipe.id)
            return IngredientSerializer(recipe_ingredients, many=True).data
        except models.Ingredient.DoesNotExist:
            return None

    def create(self, validated_data):
        """
        function for recipes, a restaurant and a list of ingredients is asociated. The restaurantId
        is taken from the corresponding path parameter and the ingredients can be added optionally in the post body.
        """
        ingredients_data = validated_data.pop("ingredients")

        restaurant = models.Restaurant.objects.get(pk=validated_data["restaurant_id"])
        validated_data["restaurant"] = restaurant
        recipe = models.Recipe.objects.create(**validated_data)

        # Assign ingredients if they are present in the body
        if ingredients_data:
            for ingredient_dict in ingredients_data:
                ingredient = models.Ingredient(name=ingredient_dict["name"])
                ingredient.save()
                ingredient.recipe.add(recipe)
        return recipe

    class Meta:
        model = models.Recipe
        fields = ['id', 'name', 'type', 'ingredients']
