from rest_framework import serializers
from .models import *


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News 
        fields = "__all__"
        depth =1

class CategorySerializers(serializers.ModelSerializer):
    posts = NewsSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'timestamp', 'posts']
        depth = 1
        


    
        