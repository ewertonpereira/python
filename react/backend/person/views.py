from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from person.models import Person
from person.seriallizer import PersonSeriallizer, FormMatchSerializer, MatchSerializer
from person.models import Match


class PersonAPIView(APIView):
    def get(self, request, format=None):
        people = Person.objects.all()
        serializer = PersonSeriallizer(people, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class FormMatchAPIView(APIView):
    def post(self, request, id, format=None):
        person = get_object_or_404(Person, id=id)
        serializer = FormMatchSerializer(data=request.data)
        if serializer.is_valid():
            match = Match(
                name=serializer.validated_data.get('name'),
                email=serializer.validated_data.get('email'),
                person =person
            )
            match.save()
            match_serializer = MatchSerializer(match, many=False)
            return Response(match_serializer.data, status=HTTP_201_CREATED)
        return Response({'message': 'Houveram erros na validação','errors':serializer.errors}, status=HTTP_400_BAD_REQUEST)