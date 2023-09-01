from rest_framework import serializers


class LoadCSVSerialisers(serializers.Serializer):
    """Сериализатор для загрузки файла .csv"""

    file = serializers.FileField
