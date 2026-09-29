from rest_framework import viewsets

from .models import Consulta, Profissional
from .serializers import ConsultaSerializer, ProfissionalSerializer


class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        queryset = Consulta.objects.all()

        profissional_id = self.request.query_params.get('profissional_id')

        if profissional_id:
            queryset = queryset.filter(profissional_id=profissional_id)

        return queryset