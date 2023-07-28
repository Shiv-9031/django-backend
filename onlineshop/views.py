from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import OrderSerializers,ProductSerializers,CategorySerializers
from .models import Category,Product,Orders
from rest_framework import status
from rest_framework .response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER


# Create your views here.

class OrderView(APIView):
    def get(self,request):

        try:
            orders= Orders.objects.all()
            serializer = OrderSerializers(orders,many=True)

            return Response({
                'data':serializer.data,
                'message':"order Data fetched Successfully"
            },status=status.HTTP_200_OK)
        except NameError:
            return Response({
                "data":{},
                'message':NameError

            },status=status.HTTP_400_BAD_REQUEST)


    def post( self,request):

        try:
           
            serializer = OrderSerializers(data=request.data)

            if not serializer.is_valid(): 
                return Response({
                "data":serializer.errors,
                'message':"something went wrong"

            },status=status.HTTP_400_BAD_REQUEST)  
            
            subject ="new order is placed",
            message=f"Dear Customer {request.data['customer_name']}.Your order is placed now .Thanks for your order"
            recipient_list=[request.data['customer_email']]
            send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently=True,)

            serializer.save()
            return Response({
                'data':serializer.data,
                'message':"New order is created or placed"
            },status=status.HTTP_201_CREATED)
        except NameError:
            return Response({
                "data":{},
                #'message':"something went wrong during creation  of order"
                "message": NameError

            },status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request):

        try:
            data= request.data
            order =Orders.objects.filter(id=data.get('id'))    

            if not order.exists():
                return Response({
                    'data':{},
                    "message":"data is not found for this id"
                },status=status.HTTP_400_BAD_REQUEST) 
            
            serializer=OrderSerializers(order[0],data=data,partial=True)

            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':"something went wrong"
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                "message":"data is updated",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        
        except NameError:
            return Response({
                "message":NameError,
                "data":{}
            },status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request):
        try:
            data= request.data
            order=Orders.objects.filter(id=data.get('id')) 

            if not order.exists():
                return Response({
                    'message':"order is not found",
                    "data":{}
                },status=status.HTTP_400_BAD_REQUEST)   
            
            order[0].delete()
            return Response({
                'data':{},
                'message':'order is deleted succesfully'
            },status=status.HTTP_200_OK)
        except NameError:
            return Response({
                "message":NameError,
                'data':{}
            },status=status.HTTP_400_BAD_REQUEST)
            