from rest_framework import serializers

from .models import Category,Product,Orders

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('__all__')

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields=("__all__") 


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model =Orders
        fields=("__all__") 

