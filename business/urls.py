from django.urls import path
from .views import ReqCompany, RequestCompleted, CompanyList

urlpatterns = [
    path('add/', ReqCompany.as_view(),name='addcompany'),
    path('request/', RequestCompleted.as_view(),name='thanks'),
    path('list/', CompanyList.as_view(),name='companylist'),
]