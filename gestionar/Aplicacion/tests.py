# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from Aplicacion.models import Afiliado, Benefiniciario

class RegistroAfiliado(TestCase):
    def setUp(self):
        Afiliado.create("pepito", "apellidos", "cedula", "direccion", "telefono","eps", "pension", "arl", 3, 12000)
        

    def test_registro(self):
        afiliado = Afiliado.objects.get(nombres = "pepito")
        self.assertEqual(afiliado.nombres, "pepito")
        
    def test_actualizar(self):
        afiliado = Afiliado.objects.get(nombres = "pepito")
        afiliado.nombres ="panchito" 
        self.assertEqual(afiliado.nombres, "pepito")
        