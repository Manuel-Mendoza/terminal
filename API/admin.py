from django.contrib import admin
from .models import Empresa, Destino, DestinosTuristicos, Publicidad
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Destino)
admin.site.register(DestinosTuristicos)
admin.site.register(Publicidad)
