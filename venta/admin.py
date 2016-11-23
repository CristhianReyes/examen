from django.contrib import admin
from .models import Productos
from .models import Usuarios
from .models import Venta

admin.site.register(Productos)
admin.site.register(Usuarios)
admin.site.register(Venta)
