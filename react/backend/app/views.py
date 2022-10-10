from rest_framework.views import APIView
from rest_framework.response import Response


class HomeApiView(APIView):
    def get(self, resquest, format=None):
        return Response({'Nome': 'Ewerton', 'idade': 28}, status=200)