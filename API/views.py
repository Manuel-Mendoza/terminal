from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeleteView
from .models import Empresa, Destino, DestinosTuristicos, Publicidad
from django.contrib.auth.mixins import LoginRequiredMixin

# DJANGO REST_FRAMEWORK
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from API.serializers import CompanySerializers, PublicidadSerializers

from django.urls import reverse_lazy
from .forms import CompanyForm, DestinosForm, DestinosTForm, PublicidadForm
# Create your views here.

class vista(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Empresa
    context_object_name = 'obj'
    template_name = "API/prueba.html"

class CreateCompany(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Empresa
    form_class = CompanyForm
    template_name = "API/create_empresa.html"
    success_url = reverse_lazy('list_company')

class CreateDestino(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Destino
    form_class = DestinosForm 
    template_name = "API/create_destinos.html"
    success_url = reverse_lazy('list_destination')

class CreatePublicidad(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Publicidad
    form_class = PublicidadForm
    template_name = "API/crear_publicidad.html"
    success_url = reverse_lazy('list_publicidad')

class ListPublicidad(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Publicidad
    template_name = "API/lista_publicidad.html"
    context_object_name = "obj" 

class CreateDestinoT(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Destino
    form_class = DestinosTForm 
    template_name = "API/crear_destinoT.html"
    success_url = reverse_lazy('turismo')

class ListCompany(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Empresa
    template_name = "API/lista_empresa.html"
    context_object_name = "obj" 

class DeleteCompany(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Empresa
    template_name = "API/borrar_empresa.html"
    success_url = reverse_lazy("list_company")

class UpdateCompany(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Empresa
    form_class = CompanyForm
    template_name = "API/actualizar_empresa.html"
    success_url = reverse_lazy("list_company")

class DestinoList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Destino
    context_object_name = "obj" 
    template_name = "API/listado_destinos.html"

class DestinoUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Destino
    template_name = "API/actualizar_destinos.html"
    form_class = DestinosForm
    success_url = reverse_lazy("list_destination")

class DestinoDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Destino
    template_name = "API/borrar_destino.html"
    success_url = reverse_lazy("list_destination")

class DestinosTuristicos(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = DestinosTuristicos
    context_object_name = "obj" 
    template_name = "API/destinos_turisticos.html"

# DJANGO REST_FRAMEWORK

class Company(APIView):
    def get(self, request):
        Company = Empresa.objects.all()
        data = CompanySerializers(Company, many=True).data
        return Response(data)

class CompanyDetailRest(APIView):
    def get(self, request, pk):
        Company = get_object_or_404(Empresa, pk=pk)
        data = CompanySerializers(Company).data
        return Response(data)

class PublicidadList(APIView):
    def get(self, request):
        publicidad = Publicidad.objects.all()
        data = PublicidadSerializers(publicidad, many=True).data
        return Response(data)