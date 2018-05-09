# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Aplicacion.models import UsuarioAdministrativo, Afiliado, Benefiniciario,\
    Ingreso,CitaMedica
    
    
admin.site.site_header = "Gestionar"
admin.site.site_title = "Gestionar"

admin.site.register(UsuarioAdministrativo)
admin.site.register(Afiliado)
admin.site.register(Benefiniciario)
admin.site.register(Ingreso)
admin.site.register(CitaMedica)