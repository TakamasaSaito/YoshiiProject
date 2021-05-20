from django.urls import path
from .views import ReqCompany

urlpatterns = [
    path('add/', ReqCompany.as_view(),name='addcompany'),
]