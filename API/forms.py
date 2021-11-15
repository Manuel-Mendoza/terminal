from django.forms import ModelForm
from .models import Destino, DestinosTuristicos, Empresa, Publicidad

class CompanyForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class DestinosForm(ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class DestinosTForm(ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = '__all__'

class PublicidadForm(ModelForm):
    class Meta:
        model = Publicidad
        fields = '__all__'