from django.contrib import admin
from .models import Productos
from .models import Categoria
from .models import Clientes
from .models import Pedidos

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categoria)
admin.site.register(Clientes)
admin.site.register(Pedidos)
