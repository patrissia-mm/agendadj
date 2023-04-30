from rest_framework import serializers
#
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__'
        )

class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo = serializers.BooleanField(required=False)

class PersonaSerializer2(serializers.ModelSerializer):
    activo = serializers.BooleanField(default = True)
    class Meta:
        model = Person
        fields = ('__all__')
