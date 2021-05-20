from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import CompanyModel
from django.urls import reverse_lazy

class ReqCompany(CreateView):
    template_name = 'addcompany.html'
    model = CompanyModel
    fields = ('companyname', 'outline')
    success_url = reverse_lazy('')