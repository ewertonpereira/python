from django.forms import ValidationError
from rest_framework import serializers
from person.models import Person, Match


class PersonSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class FormMatchSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=100)

    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError('Deve ter pelo menos 3 caracteres.')
        return value

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'