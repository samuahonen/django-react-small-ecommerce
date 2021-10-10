from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
# Create your views here.


class CreateTest(APIView):
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        return Response("True")
    def get(self,request):
        return Response(self.request.session.session_key)

class Test2(APIView):
    def get(self,request,format=None):
        
        return Response("ok")

class HandleCart(APIView):
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            cart = Cart()
            cart.create(self.request.session.session_key)
        try:
            token = self.request.session.session_key
            cart = Cart.objects.get(token=token)
            item = Item.objects.get(id=request.data["id"])
            cart.item = item
            cart.save()
        except:
            return Response({"content":"something went wrong"})
        return Response({"content":"All Good"})

    def get(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            cart = Cart()
            cart.create(self.request.session.session_key)
        token = self.request.session.session_key
        cart = Cart.objects.get(token=token)
        data = cart.all_items()
        return Response(data)
        
