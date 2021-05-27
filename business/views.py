from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import CompanyModel
from django.urls import reverse_lazy

class ReqCompany(CreateView):
    template_name = 'addcompany.html'
    model = CompanyModel
    fields = ('companyname', 'outline')
    success_url = reverse_lazy('thanks')

class RequestCompleted(TemplateView):
    template_name = 'requestecompleted.html'

class CompanyList(ListView):
    template_name = 'companylist.html'
    model = CompanyModel