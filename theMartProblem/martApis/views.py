from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from martApis.models import Mart,Sku
from martApis.serializer import MartSerializer,SkuSerializer
import logging
import json

logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', level=logging.DEBUG,)

@api_view(['GET'])
def getLocation(request):
    '''
    Purpose: Get all the locations
    Output: JSON containing all the locations
    '''
    try:
        location = Mart.objects.all().values('location').distinct()
        return Response(location,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'Error_code': status.HTTP_400_BAD_REQUEST,
                            'Error_Message': "Could not retrieve locations"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET'])
def getDepartments(request,location_id):   
    '''
    Purpose: Get all departments against the given location, available in the Mart
    Input:
    location_id: (mandatory) <str> Location
    Output: JSON containing all departments for the given location
    '''     
    try:
        departments = Mart.objects.filter(location=location_id).values('department').distinct()
        return Response(departments,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'Error_code': status.HTTP_400_BAD_REQUEST,
                            'Error_Message': "Could not retrieve departments"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def getCategory(request,location_id,department_id): 
    '''
    Purpose: Get all categories against the given location and department, available in the Mart
    Input:
    location_id: (mandatory) <str> Location
    department_id: (mandatory) <str> Department
    Output: JSON containing all categories for the given location and department
    '''  
    try:
        category = Mart.objects.filter(location=location_id,department=department_id).values('category').distinct()
        return Response(category,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'Error_code': status.HTTP_400_BAD_REQUEST,
                            'Error_Message': "Could not retrieve categories"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getSubCategory(request,location_id,department_id,category_id): 
    '''
    Purpose: Get all subcategories against the given location, department and category, available in the Mart
    Input:
    location_id: (mandatory) <str> Location
    department_id: (mandatory) <str> Department
    category_id: (mandatory) <str> Category
    Output: JSON containing all subcategories for the given location,department and category
    '''  
    try:
        subcategory = Mart.objects.filter(location=location_id,department=department_id,category=category_id).values('subcategory').distinct()
        return Response(subcategory,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'Error_code': status.HTTP_400_BAD_REQUEST,
                            'Error_Message': "Could not retrieve subcategories"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)        

@api_view(['GET'])
def getSubCategoryWithId(request,location_id,department_id,category_id,subcategory_id): 
    '''
    Purpose: Get the subcategory for the given subcategory_id
    Input:
    location_id: (mandatory) <str> Location
    department_id: (mandatory) <str> Department
    category_id: (mandatory) <str> Category
    subcategory_id: (mandatory) <str> Subcategory
    Output: Mart Object for the subcategory for the given subcategory_id
    '''  
    try:
        subcategory = Mart.objects.filter(location=location_id,department=department_id,category=category_id,subcategory=subcategory_id)
        serializer = MartSerializer(subcategory,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'Error_code': status.HTTP_400_BAD_REQUEST,
                            'Error_Message': "Could not retrieve the subcategory"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getSku(request,location_id,department_id,category_id,subcategory_id): 
    '''
    Purpose: Get the Sku Data for the given Mart Data (i.e. location, department, category, subcategory)
    Input:
    location_id: (mandatory) <str> Location
    department_id: (mandatory) <str> Department
    category_id: (mandatory) <str> Category
    subcategory_id: (mandatory) <str> Subcategory
    Output: Sku Object of all the matching Sku Data for the given Mart Data
    '''  
    try:
        SkuData = Sku.objects.filter(location=location_id,department=department_id,category=category_id,subcategory=subcategory_id)
        serializer = SkuSerializer(SkuData,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'Error_code': status.HTTP_400_BAD_REQUEST,
                            'Error_Message': "Could not retrieve the subcategory"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)        