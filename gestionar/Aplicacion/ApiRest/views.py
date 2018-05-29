# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from datetime import datetime
from Aplicacion.models import UsuarioAdministrativo, Afiliado, Benefiniciario, Ingreso,\
    CitaMedica
from rest_framework.response import Response
from rest_framework import status
from serializers import AdminitrarivoSerializer
from django.template.context_processors import request
from Aplicacion.ApiRest.serializers import AfiliadoSerializer, BeneficiarioSerializer,\
    IngresoSerializer, CitaSerializer


from django.core.mail import send_mail
from gestionar import settings



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
                correo=request.data['correo']
                direccion=request.data['direccion']
                telefono=request.data['telefono']
                arl=request.data['arl']
                eps=request.data['eps']
                pension=request.data['pension']
                rango=request.data['rango']
                costo=request.data['costo']
                Afiliado.create(nombres, apellidos, cedula, direccion, telefono, eps, arl,pension, rango, costo,correo)
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
                correo=request.data['correo']
                
                
                usuario_afiliado.update(nombres = nombres)
                usuario_afiliado.update(apellidos = apellidos)
                usuario_afiliado.update(direccion = direccion)
                usuario_afiliado.update(telefono = telefono)
                usuario_afiliado.update(eps = eps)
                usuario_afiliado.update(arl = arl)
                usuario_afiliado.update(rango = rango)
                usuario_afiliado.update(costo = costo)
                usuario_afiliado.update(pension = pension)
                usuario_afiliado.update(correo = correo)
                
                
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
            afiliados_ultimos =[]
            for afiliado in afiliados:
                mes_afiliado = (afiliado.ultima_afiliacion).month
                mes_actual = datetime.now().month
                if(mes_afiliado -mes_actual)==0:
                    afiliados_ultimos.append(afiliado)
            if len(afiliados_ultimos)>0:
                respuesta = self.afiliado_serializer(afiliados_ultimos, many=True, context={"request" : request})
                return Response(respuesta.data, status=status.HTTP_200_OK)
            else:
                return Response({"mensaje":"no hay datos para mostrar"},status=status.HTTP_404_NOT_FOUND)
obtener_afiliados= ObtenerAfiliados.as_view()


class ObtenerAfiliadosMora(APIView):
    afiliado_serializer = AfiliadoSerializer
    def get(self,request):
        afiliados = Afiliado.objects.all()
        
        if len(afiliados)==0:
            return Response({"mensaje":"no hay datos para mostrar"},status=status.HTTP_404_NOT_FOUND)
        else:
            afiliados_mora = []
            for afiliado in afiliados:
                mes_afiliado = (afiliado.ultima_afiliacion).month
                #mes_afiliado = datetime.strptime(str('2018-04-01'), '%Y-%m-%d').month
                mes_actual = datetime.now().month
                
                
                if (mes_afiliado - mes_actual)<0:
                    afiliados_mora.append(afiliado)
            
            if len(afiliados_mora)>0:             
                respuesta = self.afiliado_serializer(afiliados_mora, many=True, context={"request" : request})
                return Response(respuesta.data, status=status.HTTP_200_OK)
            else:
                return Response({"mensaje":"no hay afiliados en mora"},status=status.HTTP_404_NOT_FOUND)
obtener_afiliadosmora= ObtenerAfiliadosMora.as_view()


class RenovarAfiliacion(APIView):
    def post(self,request):
        if request.data:
            cedula = request.data['cedula']
            correo = request.data['correo']
            usuario_afiliado = Afiliado.objects.filter(pk=cedula)
            if (len(usuario_afiliado)==0):
                return Response({"mensaje":"NO se encontro datos correspondientes"},status=status.HTTP_404_NOT_FOUND)
            else:
                usuario_afiliado.update(ultima_afiliacion =datetime.now())
                
                subject = 'Gestionar Afiliacion'
                message = 'Gracias por realizar el respectivo pago'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [correo]
                motivo = "renovacion afiliacion"
                valor = "200000"
                print usuario_afiliado
                Ingreso.create(motivo,valor,usuario_afiliado[0])
                send_mail(subject, message, from_email, recipient_list, fail_silently = True )
                
                return Response({"mensaje":"Actualizacion correcta"},status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"No se dictaron los parametros necesarios"},status=status.HTTP_400_BAD_REQUEST)
renovarafiliacion= RenovarAfiliacion.as_view()
            

class EnviarCorreo(APIView):
    def post(self,request):
        if request.data:
            correo = request.data['correo']
            subject = 'Gestionar Afiliacion'
            message = 'En el momento no se han realizado los correspondientes pagos, por favor realice el respectivo pago.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [correo]    
            send_mail(subject, message, from_email, recipient_list, fail_silently = True )
            return Response({"mensaje":"Correo enviado correctamente"},status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"No se dictaron los parametros necesarios "},status=status.HTTP_400_BAD_REQUEST)
enviar_correo= EnviarCorreo.as_view()
            
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


class RegistrarCitas(APIView):
    def post(self,request):
        if request.data:
            cedula = request.data['cedula']
            afiliado = Afiliado.objects.filter(pk=cedula)
            
            if len(afiliado)>0:
                tipo_cita = request.data['tipo_cita']
                valor = request.data['valor']
                afiliado = afiliado[0]
                fecha_cita =request.data['fecha_cita']
                nombre =request.data['nombre']
                cedula_dps =request.data['cedula_dos']
                CitaMedica.create(fecha_cita,tipo_cita,valor,afiliado,nombre,cedula_dps)
                return Response({"mensaje":"Cita registrada correctamente"},status=status.HTTP_200_OK)
            else:
                return Response({"mensaje":"No se encuentra la cedula"},status=status.HTTP_404_NOT_FOUND)
registro_cita = RegistrarCitas.as_view()



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

class ObtenerCitas(APIView):
    ingreso_serializer = CitaSerializer
    def get(self,request):
        citas = CitaMedica.objects.all()
        if len(citas)==0:
            return Response({"mensaje":"no hay datos para mostrar"},status=status.HTTP_404_NOT_FOUND)
        else:
            respuesta = self.ingreso_serializer(citas, many=True, context={"request" : request})
            return Response(respuesta.data, status=status.HTTP_200_OK)
obtener_citas = ObtenerCitas.as_view()

