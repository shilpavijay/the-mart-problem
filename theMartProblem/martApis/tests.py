from django.test import TestCase
from martApis.views import getLocation,getDepartments,getCategory,getSubCategory,getSubCategoryWithId,getSku
from rest_framework.test import APIRequestFactory
from rest_framework import status

factory = APIRequestFactory()

class MartApisTestCases(TestCase):
    def test_getLocation(self):
        request = factory.get('/api/v1/location')
        response = getLocation(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_getDepartments_Perimeter(self):
        request = factory.get('/api/v1/location/Perimeter/department')
        response = getDepartments(request,"Perimeter")
        self.assertEqual(response.status_code,status.HTTP_200_OK)  

    def test_getDepartments_Center(self):
        request = factory.get('/api/v1/location/Center/department')
        response = getDepartments(request,"Center")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_getCategory(self):
        request = factory.get('/api/v1/location/Perimeter/department/Bakery/category')
        response = getCategory(request,"Perimeter","Bakery")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_getSubCategory(self):
        request = factory.get('/api/v1/location/Center/department/Bakery/category/Bakery Bread/subcategory')
        response = getSubCategory(request,"Perimeter","Bakery","Bakery Bread")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_getSubCategoryWithId(self):
        request = factory.get('/api/v1/location/Center/department/Bakery/category/Bakery Bread/subcategory/Bagels')
        response = getSubCategoryWithId(request,"Perimeter","Bakery","Bakery Bread","Bagels")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_getSku(self):
        request = factory.get('/api/v1/location/Center/department/Bakery/category/Bakery Bread/subcategory/Bagels/skudata')
        response = getSku(request,"Perimeter","Bakery","Bakery Bread","Bagels")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
