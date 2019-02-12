# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UsuarioAdministrativo (models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    activo = models.BooleanField(default=False)
    password = models.CharField(max_length=32)
    
    
    @classmethod
    def create(cls,nombres,apellidos,username,cargo,password):
        usuario = cls(nombres=nombres,apellidos = apellidos,username=username,cargo=cargo,password=password)
        usuario.save()
        return usuario    
    
    def __unicode__(self):
        return self.nombres

    class  Meta(object):
        verbose_name = 'Usuario Administrativo'
        verbose_name_plural = 'Usuario Administrativos'



class Afiliado (models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    ultima_afiliacion = models.DateTimeField(auto_now_add=True, blank=True)
    cedula = models.CharField(max_length=30,primary_key=True)
    direccion = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.CharField(max_length=30)
    eps = models.CharField(max_length=30)   
    pension = models.CharField(max_length=30)   
    arl = models.CharField(max_length=30)
    rango = models.IntegerField()
    costo = models.CharField(max_length=30)
    
    @classmethod
    def create(cls,nombres,apellidos,cedula,direccion,telefono,eps,arl,pension,rango,costo,correo):
        usuario = cls(nombres=nombres,apellidos = apellidos,cedula= cedula,direccion=direccion,
                      telefono=telefono,eps=eps,arl=arl,pension = pension,rango=rango,costo=costo,correo=correo)
        usuario.save()
        return usuario    
    
    def __unicode__(self):
        return self.nombres

    class  Meta(object):
        verbose_name = 'Afiliado'
        verbose_name_plural = 'Afiliados'
    
    
class Benefiniciario(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30,primary_key=True)
    fecha_nacimiento = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=30)
    afiliado = models.ForeignKey(Afiliado,on_delete=models.CASCADE)
    
    @classmethod
    def create(cls,nombres,apellidos,cedula,fecha_nacimiento,parentesco,afiliado):
        usuario = cls(nombres=nombres,apellidos = apellidos,cedula = cedula,fecha_nacimiento=fecha_nacimiento,
                      parentesco=parentesco,afiliado=afiliado)
        usuario.save()
        return usuario    
    
    def __unicode__(self):
        return self.nombres

    class  Meta(object):
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'
    
class Ingreso(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    motivo = models.CharField(max_length=30)
    valor = models.CharField(max_length=30)
    afiliado = models.ForeignKey(Afiliado,on_delete=models.CASCADE)
        
    @classmethod
    def create(cls,motivo,valor,afiliado):
        ingreso = cls(motivo = motivo,valor = valor, afiliado = afiliado)
        ingreso.save()
        return ingreso    
    class  Meta(object):
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
    def __unicode__(self):
        return self.afiliado.nombres

class CitaMedica(models.Model):
    dia_registro = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_cita = models.CharField(max_length=30)
    tipo_cita = models.CharField(max_length=30)
    valor= models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    afiliado = models.ForeignKey(Afiliado,on_delete=models.CASCADE)
    
        
    @classmethod
    def create(cls,fecha_cita,tipo_cita,valor,afiliado,nombre,cedula):
        cita = cls(fecha_cita = fecha_cita,tipo_cita = tipo_cita,valor=valor, afiliado = afiliado,nombre=nombre,cedula=cedula)
        cita.save()
        return cita    
    class  Meta(object):
        verbose_name = 'Cita medica'
        verbose_name_plural = 'Citas medicas'
        
    def __unicode__(self):
        return self.afiliado.nombres
        
        
class DerechoPeticion(models.Model):
    dia_registro = models.DateTimeField(auto_now_add=True, blank=True)
    costo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    afiliado = models.ForeignKey(Afiliado,on_delete=models.CASCADE)
    
        
    @classmethod
    def create(cls,costo,descripcion,afiliado):
        derecho = cls(costo = costo,descripcion = descripcion,afiliado=afiliado)
        derecho.save()
    class  Meta(object):
        verbose_name = 'Derecho de peticion'
        verbose_name_plural = 'Derechos de peticiones'
        
    def __unicode__(self):
        return self.afiliado.nombres