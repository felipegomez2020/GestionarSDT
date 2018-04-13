from django.conf.urls import url
from Aplicacion.ApiRest.views import login_user, crear_usuario, registrar_afiliado, registrar_beneficiario, obtener_afiliados, obtener_beneficiarois,\
    eliminar, actualizar_afiliado, ingreso, obtener

urlpatterns = [
     url(r'^login/$', login_user),
     url(r'^crear_usuario_administrativo/$', crear_usuario),
     url(r'^registrar_afiliado/$', registrar_afiliado),
     url(r'^registrar_beneficiario/$', registrar_beneficiario),
     url(r'^obtener_afiliado/$', obtener_afiliados),
     url(r'^obtener_beneficiarios/$', obtener_beneficiarois),
     url(r'^eliminar_afiliado/$', eliminar),
     url(r'^actualizar_afiliado/$', actualizar_afiliado),
     url(r'^registrar_ingresos/$', ingreso),
     url(r'^obtener_ingresos/$', obtener),

     
]
