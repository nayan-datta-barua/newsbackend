from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

class CategoryNameView(APIView):
    def get(self,request):
        name = Category.objects.all()
        serializers= CategorySerializers(name,many=True)
        return Response(serializers.data)


class CategoryView(APIView):
    def get(self,request):
        query = Category.objects.all()
        serializer = CategorySerializers(query,many=True)
        # return Response(serializer.data)
        news1 =[]
        for n in serializer.data:
            nuse = News.objects.filter(category_id=n['id'])
            seri = NewsSerializers(nuse,many=True)
            news1.append(seri.data)
        return Response(news1)  
    
class CategoryDetailAPIView(APIView):
    def get(self, request, id):
        
        data = News.objects.filter(category_id=id)
        seri = NewsSerializers(data,many=True)
        return Response(seri.data) 
    
        # category = Category.objects.get(id=id)
        # serializer = CategorySerializers(category)
        # list=[]
        # for n in serializer.data:
        #     print(serializer.data)
            
        #     d=News.objects.get(category_id=id)
        #     catseri=NewsSerializers(d,many=True)
        #     list.append(catseri.data)
                
        # return Response(list)
    
    # Purbo-Pascim
    
    # দৈনিক পূর্বপশ্চিম 

class NewsView(APIView): 
    def get(self,request):
        query = News.objects.all()
        serializer = NewsSerializers(query,many=True)
        return Response(serializer.data)
    
class NewsDetailAPIView(APIView):
    def get(self,request,id):
        print(id)
        query = News.objects.filter(id=id)
        print(query)
        serializer = NewsSerializers(query,many=True)
        print(serializer.data)
        
        return Response(serializer.data)
        
# class CategoryDetailAPIView(APIView):
#     def get(self, request, id):
#         try:
#             category = Category.objects.get(id=id)
#             serializer = CategorySerializers(category)
#             list=[]
#             for data in serializer.data:
#                 d=News.objects.filter(category_id=data['id'])
#                 catseri=NewsSerializers(d,many=True)
#                 list.append(catseri.data)
                
#             return Response(list)
#         except Category.DoesNotExist:
#             return Response({"error": "Category not found"})


        
        
    