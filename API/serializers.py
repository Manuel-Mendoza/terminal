from rest_framework import serializers
from API.models import Empresa, Publicidad

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        
class PublicidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publicidad
        fields = '__all__'