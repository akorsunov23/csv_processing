from rest_framework.generics import CreateAPIView
from .serialisers import LoadCSVSerialisers


class LoadCSVAPIView(CreateAPIView):
    """Загрузка и обработка .csv файла."""

    serializer_class = LoadCSVSerialisers
