# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import AdminSite
from Aplicacion.models import UsuarioAdministrativo, Afiliado, Benefiniciario,\
    Ingreso,CitaMedica
    
class MyModelAdmin(admin.ModelAdmin):
    view_on_site = False


    
    
admin.site.site_header = "Gestionar"
admin.site.site_title = "Gestionar"

admin.site.register(MyModel,MyModelAdmin)
admin.site.register(UsuarioAdministrativo)
admin.site.register(Afiliado)
admin.site.register(Benefiniciario)
admin.site.register(Ingreso)
admin.site.register(CitaMedica)
