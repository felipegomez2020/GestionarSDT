from rest_framework.serializers import ModelSerializer
from Aplicacion.models import UsuarioAdministrativo, Afiliado, Benefiniciario,\
    Ingreso


class AdminitrarivoSerializer(ModelSerializer):
    class Meta:
        model = UsuarioAdministrativo
        fields = '__all__'
        
class AfiliadoSerializer(ModelSerializer):
    class Meta:
        model = Afiliado
        fields = '__all__'
        
class BeneficiarioSerializer(ModelSerializer):
    class Meta:
        model = Benefiniciario
        fields = '__all__'
        
class IngresoSerializer(ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'