# -*- coding: utf-8 -*-
from django.shortcuts import render

import os
import json
import time
import uuid

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpRequest

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import View
from rest_framework import generics

from openpyxl import Workbook
from openpyxl import load_workbook

from .models import Address
from .serializer import AddressSerializer

from postassistant import settings

from pyutils import excelutils as ecu
from pyutils.excelutils import Column

from datetime import datetime as dtm

BASE_DIR = os.getcwd()

# 使用APIView
class StudentAddressView(APIView):
    def get(self, request, id):

        print('Address post method')
        stu_list = []
        stu_list.append({'student_id':'weisf'})

        return JsonResponse(stu_list, safe=False)

    '''
    ' @brief: 获取当前表中所有用户信息
    '''
    def get(self, request):
        print('Address post all student information method')
        addr_json = []
        '''{data: "student_name"}, {data: "student_id"}, {data: "delivery_name"}, {data: "delivery_phone"},
        {data: "delivery_address_cn"}'''
        addr_objs = Address.objects.all()
        id_cnt = 0
        for addr in addr_objs:
            id_cnt += 1
            addr_json.append({'id':id_cnt,
                'student_name': addr.student_name,
                'student_id': addr.student_id, 
                'delivery_name': addr.delivery_name, 
                'delivery_phone': addr.delivery_phone, 
                'delivery_address_cn': addr.delivery_address_cn})

        return JsonResponse(addr_json, safe=False)
    
    '''
    ' @brief: 批量导入、增加学生信息
    '''
    def post(self, request): 
        print('Address post all student information method')
        addr_info = []
        '''{data: "student_name"}, {data: "student_id"}, {data: "delivery_name"}, {data: "delivery_phone"},
        {data: "delivery_address_cn"}'''
        addr_info.append({'student_name':'魏绍飞',
                        'student_id': '2018640492', 
                        'delivery_name': '魏绍飞', 
                        'delivery_phone': '13001997216', 
                        'delivery_address_cn': '北京海演区'})

        return JsonResponse(addr_info, safe=False)

    '''
    ' @brief: 更新指定资源
    '''
    def put(self, request):
        print('Address put method')
        body_str = request.body.decode()
        json_info = json.loads(body_str)

        try:
            address = Address.objects.get(student_name=json_info.get('name'), 
                        student_id=json_info.get('suid'))
            print (address.student_name, address.student_id)
            address.delivery_name = json_info.get('delivery_name')     # N收货人姓名
            address.delivery_phone = json_info.get('delivery_phone')   # O收货人手机
            address.delivery_address_cn = json_info.get('address_cn')  # P收货人地址中文
            address.delivery_address_en = json_info.get('address_en')  # Q收货人地址英文
            address.delivery_zipcode = json_info.get('zipcode')      # R收货人邮编
            address.last_update_date = dtm.now().strftime('%Y/%m/%d %H:%M:%S')
            address.save()  # 保存修改
            
        except Address.DoesNotExist:
            print('DoesNotExist')
            return JsonResponse({'code': 404})

        return JsonResponse({'code': 200})

'''
' @brief: 批量导入、增加学生信息
'       接收地址导入功能, 只能使用此方法接收，class无法实现
'''
@csrf_exempt
def address_attachment_upload(request):
    print('AddressImport get method')
    if request.method == 'POST':
        mem_file = request.FILES.get('excelAttachment',None)

        file_name = ''
        if (mem_file.name.endswith('.xlsx')):
            #file_name = mem_file.name[0:len(mem_file.name)-5]+str(uuid.uuid4()).replace('-','')
            file_name = str(uuid.uuid4()).replace('-','')
        
        file_name = file_name + str(time.time()).replace('.','') + '.xlsx'
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        print(file_path)
        xls_file = open(file_path, 'wb')
        for dt in mem_file.chunks():
            xls_file.write(dt)
        xls_file.close()

        et = ecu.ExcelUtils()
        et.open(file_path)

        for row in range(3, et.row_count()):
            addr = Address.objects.create (
                course_id = et.readColumn(row, Column.B),       # B课序号
                class_room = et.readColumn(row, Column.D),      # D教室，iCenter
                student_id = et.readColumn(row, Column.E),      # E学号
                student_name = et.readColumn(row, Column.F),    # F姓名
                student_gender = et.readColumn(row, Column.H),  # H性别
                department = et.readColumn(row, Column.I),      # I院系
                class_name = et.readColumn(row, Column.J),      # J班级
                student_type = et.readColumn(row, Column.K),    # K学生类别
                student_phone = et.readColumn(row, Column.L),   # L联系方式
                student_email = et.readColumn(row, Column.M),   # M电子邮箱
            )

        return JsonResponse({'id': 200})
    else:
        return JsonResponse({'id': 201})