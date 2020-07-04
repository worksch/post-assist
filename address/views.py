# -*- coding: utf-8 -*-
from django.shortcuts import render

import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpRequest

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Address
from .serializer import AddressSerializer

# 使用APIView
'''class AddressView(APIView):
    def get(self, request, format=None):
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
class StudentAddressView(APIView):
    def get(self, request, id):
        stu_list = []
        stu_list.append({'student_id':'weisf'})
        return JsonResponse(stu_list, safe=False)
    
    '''
    新增学生信息
    '''
    def post(self, request): 
        body_str = request.body.decode()
        stu_info = json.loads(body_str)
        print(stu_info.get('name'))

        try:
            addr = Address.objects.get(student_name=stu_info.get('name'), student_id='123')
        except Address.DoesNotExist:
            print('DoesNotExist')

        return JsonResponse({'msg': 'success'})

    def put(self, request):

        return HttpResponse('put')