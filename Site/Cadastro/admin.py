
from django.contrib import admin
from .models import Cliente,Produtos
# Register your models here.

class displayAdmin(admin.ModelAdmin):
    list_display = ('id','nome','idade','email')


admin.site.register(Cliente,displayAdmin)
admin.site.register(Produtos)