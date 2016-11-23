from django.contrib import admin
from .models import Producto
from .models import Persona
from .models import Compra
from .models import Marca
from .models import ComDes

admin.site.register(Producto)
admin.site.register(Persona)
admin.site.register(Compra)
admin.site.register(Marca)
admin.site.register(ComDes)
