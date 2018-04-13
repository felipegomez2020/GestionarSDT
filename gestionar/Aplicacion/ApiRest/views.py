# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from Aplicacion.models import UsuarioAdministrativo, Afiliado, Benefiniciario, Ingreso
from rest_framework.response import Response
from rest_framework import status
from serializers import AdminitrarivoSerializer
from django.template.context_processors import request
from Aplicacion.ApiRest.serializers import AfiliadoSerializer, BeneficiarioSerializer,\
    IngresoSerializer

# Create your views here.
class Login(APIView):
    serializer_usuario = AdminitrarivoSerializer
    def post(self,request):
        if request.data:
            username = request.data['usuario']
            password = request.data['pass']
            encontrado = UsuarioAdministrativo.objects.filter(username= username)
            
            if len(encontrado)>0:
                encontrado = encontrado[0]
                if(encontrado.password == password):
                    respuesta= self.serializer_usuario(encontrado,context={"request":request})
                    return Response(respuesta.data,status=status.HTTP_200_OK)
                else:
                    return Response({"mensaje":"Contraseña incorrrecta"},status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"mensaje":"El usuario no existe"},status=status.HTTP_404_NOT_FOUND)
login_user = Login.as_view()


class CrearUsuario(APIView):
    def post(self, request):
        if request.data:
            username =request.data['username']
            
            usuario= UsuarioAdministrativo.objects.filter(username=username)
            
            if (len(usuario)==0):
                nombres=request.data['nombres']
                apellidos=request.data['apellidos']
                cargo=request.data['cargo']
                password=request.data['pass']
                
                UsuarioAdministrativo.create(nombres, apellidos, username, cargo, password)
                return Response({"mensaje":"Usuario Creado correctamete"},status=status.HTTP_201_CREATED)
            else:
                return Response({"mensaje":"Usuario ya existente"},status=status.HTTP_302_FOUND)
                
        else:
            return Response({"mensaje":"No se dictaron los parametros necesarios"},status=status.HTTP_400_BAD_REQUEST)
crear_usuario= CrearUsuario.as_view()

class RegistrarAfiliado(APIView):
    def post(self,request):
        if request.data:
            cedula =request.data['cedula']
            
            usuario_afiliado = Afiliado.objects.filter(pk=cedula)
            usuario_beneficiario= Benefiniciario.objects.filter(pk=cedula)
            
            print (str(len(usuario_afiliado)) + "  " + str(len(usuario_beneficiario)))
            
            if (len(usuario_afiliado)==0 and len(usuario_beneficiario)==0):
                nombres=request.data['nombres']
                apellidos=request.data['apellidos']
                direccion=request.data['direccion']
                telefono=request.data['telefono']
                arl=request.data['arl']
                eps=request.data['eps']
                pension=request.data['pension']
                rango=request.data['rango']
                costo=request.data['costo']
                Afiliado.create(nombres, apellidos, cedula, direccion, telefono, eps, arl,pension, rango, costo)
                return Response({"mensaje":"Usuario Creado correctamete"},status=status.HTTP_201_CREATED)
            else:
                return Response({"mensaje":"Usuario ya existente"},status=status.HTTP_302_FOUND)
                
        else:
            return Response({"mensaje":"No se dictaron los parametros necesarios"},status=status.HTTP_400_BAD_REQUEST)
registrar_afiliado= RegistrarAfiliado.as_view()


class ActualizarDatosAfiliado(APIView):
    def post(self,request):
        if request.data:
            cedula =request.data['cedula']
            
            usuario_afiliado = Afiliado.objects.filter(pk=cedula)
            
            if (len(usuario_afiliado)==1):
                nombres=request.data['nombres']
                apellidos=request.data['apellidos']
                direccion=request.data['direccion']
                telefono=request.data['telefono']
                arl=request.data['arl']
                eps=request.data['eps']
                pension=request.data['pension']
                rango=request.data['rango']
                costo=request.data['costo']
                
                
                usuario_afiliado.update(nombres = nombres)
                usuario_afiliado.update(apellidos = apellidos)
                usuario_afiliado.update(direccion = direccion)
                usuario_afiliado.update(telefono = telefono)
                usuario_afiliado.update(eps = eps)
                usuario_afiliado.update(arl = arl)
                usuario_afiliado.update(rango = rango)
                usuario_afiliado.update(costo = costo)
                usuario_afiliado.update(pension = pension)
                
                
                return Response({"mensaje":"Actualizacion correcta"},status=status.HTTP_200_OK)
            else:
                return Response({"mensaje":"Usuario no existente"},status=status.HTTP_302_FOUND)
                
        else:
            return Response({"mensaje":"No se dictaron los parametros necesarios"},status=status.HTTP_400_BAD_REQUEST)
actualizar_afiliado= ActualizarDatosAfiliado.as_view()


class RegristrarBeneficiario(APIView):
    def post(self,request):
        if request.data:
            cedula =request.data['cedula']
            
            usuario_afiliado = Afiliado.objects.filter(pk=cedula)
            usuario_beneficiario= Benefiniciario.objects.filter(pk=cedula)
            
            print (str(len(usuario_afiliado)) + "  " + str(len(usuario_beneficiario)))
            
            if (len(usuario_afiliado)==0 and len(usuario_beneficiario)==0):
                nombres=request.data['nombres']
                apellidos=request.data['apellidos']
                fecha_nacimiento=request.data['fecha_nacimiento']
                parentesco=request.data['parentesco']
                afiliado=request.data['cedula_afiliado']
                afiliado = Afiliado.objects.get(pk=afiliado)
                Benefiniciario.create(nombres, apellidos, cedula,fecha_nacimiento, parentesco, afiliado)
                return Response({"mensaje":"Usuario Creado correctamete"},status=status.HTTP_201_CREATED)
            else:
                return Response({"mensaje":"Usuario ya existente"},status=status.HTTP_302_FOUND)
                
        else:
            return Response({"mensaje":"No se dictaron los parametros necesarios"},status=status.HTTP_400_BAD_REQUEST)
registrar_beneficiario= RegristrarBeneficiario.as_view()

class ObtenerAfiliados(APIView):
    afiliado_serializer = AfiliadoSerializer
    def get(self,request):
        afiliados = Afiliado.objects.all()
        
        if len(afiliados)==0:
            return Response({"mensaje":"no hay datos para mostrar"},status=status.HTTP_404_NOT_FOUND)
        else:
            respuesta = self.afiliado_serializer(afiliados, many=True, context={"request" : request})
            return Response(respuesta.data, status=status.HTTP_200_OK)
obtener_afiliados= ObtenerAfiliados.as_view()


class ObtenerBeneficiarios(APIView):
    beneficiado_serializer = BeneficiarioSerializer
    def post(self,request):
        if request.data:
            cedula =request.data['cedula_afiliado']
            beneficiarios = Benefiniciario.objects.filter(afiliado_id = cedula)
            if (len(beneficiarios)==0):
                return Response({"mensaje":"no hay datos para mostrar"},status=status.HTTP_404_NOT_FOUND)
            else:
                respuesta = self.beneficiado_serializer(beneficiarios, many=True, context={"request" : request})
                return Response(respuesta.data, status=status.HTTP_200_OK)    
        else:
            return Response({"mensaje":"No se dictaron los parametros necesarios"},status=status.HTTP_400_BAD_REQUEST)
obtener_beneficiarois= ObtenerBeneficiarios.as_view()
    


class Eliminar(APIView):
    def post(self,request):
        if request.data:
            cedula = request.data['cedula']
            Afiliado.objects.get(pk=cedula).delete()
            return Response({"mensaje":"Eliminado satisfactoriamente"},status=status.HTTP_200_OK)
eliminar = Eliminar.as_view()


class RegistrarIngresos(APIView):
    def post(self,request):
        if request.data:
            cedula = request.data['cedula']
            afiliado = Afiliado.objects.filter(pk=cedula)
            if len(afiliado)>0:
                motivo = request.data['motivo']
                valor = request.data['valor']
                afiliado = afiliado[0]
                Ingreso.create(motivo,valor,afiliado)
                return Response({"mensaje":"Ingreso correcto"},status=status.HTTP_200_OK)
            else:
                return Response({"mensaje":"No se encuentra la cedula"},status=status.HTTP_404_NOT_FOUND)
ingreso = RegistrarIngresos.as_view()

class ObtenerIngresos(APIView):
    ingreso_serializer = IngresoSerializer
    def get(self,request):
        ingresos = Ingreso.objects.all()
        if len(ingresos)==0:
            return Response({"mensaje":"no hay datos para mostrar"},status=status.HTTP_404_NOT_FOUND)
        else:
            respuesta = self.ingreso_serializer(ingresos, many=True, context={"request" : request})
            return Response(respuesta.data, status=status.HTTP_200_OK)
obtener = ObtenerIngresos.as_view()


