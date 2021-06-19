from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/location',views.getLocation),
    path('api/v1/location/<str:location_id>/department',views.getDepartments),
    path('api/v1/location/<str:location_id>/department/<str:department_id>/category',views.getCategory),
    path('api/v1/location/<str:location_id>/department/<str:department_id>/category/<str:category_id>/subcategory',views.getSubCategory),
    path('api/v1/location/<str:location_id>/department/<str:department_id>/category/<str:category_id>/subcategory/<str:subcategory_id>',views.getSubCategoryWithId),
    path('api/v1/location/<str:location_id>/department/<str:department_id>/category/<str:category_id>/subcategory/<str:subcategory_id>/skudata',views.getSku),   
]