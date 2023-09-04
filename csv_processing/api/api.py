import csv

from django.core.files.uploadedfile import InMemoryUploadedFile
from drf_spectacular.utils import extend_schema
from rest_framework import status

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serialisers import LoadCSVSerialisers, ResponseLoadSerializer
from .services import load_csv_data


class LoadCSVAPIView(APIView):
    """Загрузка и обработка .csv файла."""

    serializer_class = LoadCSVSerialisers
    parser_classes = (MultiPartParser,)

    @extend_schema(
        summary="Upload CSV file",
        responses={
            200: ResponseLoadSerializer,
            409: ResponseLoadSerializer,
            400: ResponseLoadSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        """Сохранение данных загруженного файла в БД."""
        file: InMemoryUploadedFile = self.request.FILES.get("file")
        serializer = self.serializer_class()
        if file:
            if serializer.validate(file=file):
                csv_file = file.read().decode("utf-8-sig")
                csv_reader = csv.DictReader(csv_file.splitlines(), delimiter=",")
                response = load_csv_data(csv_reader=csv_reader)
                if not isinstance(response, tuple):
                    return Response(
                        status=status.HTTP_200_OK,
                        data={"msg": "Файл обработан без ошибок."},
                    )
                return Response(
                    status=status.HTTP_409_CONFLICT,
                    data={
                        "msg": f"Произошла ошибка при обработке файла. {response[1]}"
                    },
                )
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"msg": "Не верный формат файла."},
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"msg": "Необходимо добавить файл."},
        )
