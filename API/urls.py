from django.urls import path

from .views import Company, CompanyDetailRest, CreateDestino, CreateDestinoT, ListCompany, CreateCompany, ListPublicidad
from .views import DeleteCompany, UpdateCompany, DestinoList, DestinoUpdate, DestinoDelete, DestinosTuristicos, CreatePublicidad, PublicidadList

urlpatterns = [
    # LOGIN
    
    # DJANGO_RESTFRAMWORK
    path('company/list', Company.as_view(), name = "list"),
    path('company/list/<int:pk>/', CompanyDetailRest.as_view(), name = "companyRest"),
    path('advertising/list/', PublicidadList.as_view(), name = "publicidad"),
    
    # VISTAS API
    path('administration/create/company/', CreateCompany.as_view(), name="create_company"),
    path('administration/create/destinations/', CreateDestino.as_view(), name="create_destinations"),
    path('administration/company/list/', ListCompany.as_view(), name="list_company"),
    path('administration/delete/company/<int:pk>', DeleteCompany.as_view(), name="delete_company"),
    path('administration/update/company/<int:pk>', UpdateCompany.as_view(), name="update_company"),
    path('administration/destinations/list/', DestinoList.as_view(), name="list_destination"),
    path('administration/destinations/update/<int:pk>/', DestinoUpdate.as_view(), name="update_destination"),
    path('administration/destinations/delete/<int:pk>/', DestinoDelete.as_view(), name="delete_destination"),
    path('administration/destinations/turismo/list/', DestinosTuristicos.as_view(), name="turismo"),
    path('administration/destinations/create/turismo/', CreateDestinoT.as_view(), name="create_turismo"),
    path('administration/destinations/create/advertising/', CreatePublicidad.as_view(), name="create_publicidad"),
    path('administration/destinations/advertising/list/', ListPublicidad.as_view(), name="list_publicidad"),

]