# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Aplicacion.models import UsuarioAdministrativo, Afiliado, Benefiniciario,\
    Ingreso

admin.site.register(UsuarioAdministrativo)
admin.site.register(Afiliado)
admin.site.register(Benefiniciario)
admin.site.register(Ingreso)