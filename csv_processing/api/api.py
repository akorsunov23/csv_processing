from django.core.files.uploadedfile import InMemoryUploadedFile
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import ParseError, ValidationError, NotFound
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serialisers import LoadCSVSerializers, ResponseSerializers, UsersSerializers
from .services import get_favorites, load_csv_data


class LoadCSVAPIView(APIView):
    """Загрузка и обработка .csv файла."""

    serializer_class = LoadCSVSerializers
    parser_classes = (MultiPartParser,)

    @extend_schema(
        summary="Upload CSV file",
        responses={
            200: ResponseSerializers,
            400: ResponseSerializers,
        },
    )
    def post(self, *args, **kwargs):
        """Сохранение данных загруженного файла в БД."""
        file: InMemoryUploadedFile = self.request.FILES.get("file")
        serializer = self.serializer_class()
        if file and serializer.validate(file=file):
            response, msg = load_csv_data(file=file)
            if response:
                return Response(
                    status=status.HTTP_200_OK,
                    data={"msg": msg},
                )
            raise ValidationError(
                detail=f"Произошла ошибка "
                       f"при обработке файла. {msg}"
            )
        raise ParseError(detail="Ошибка при обработке.")


class FavoriteUsersAPIView(APIView):
    """Получение списка покупателей потративших наибольшую сумму за весь период."""

    serializer_class = UsersSerializers

    @extend_schema(
        summary="Get favorites",
        responses={
            200: serializer_class,
            404: ResponseSerializers,
        },
    )
    def get(self, *args, **kwargs):
        favorites = get_favorites()
        serializer = self.serializer_class(data=favorites, many=True)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        raise NotFound(detail="Ошибка при обработке запроса.")
