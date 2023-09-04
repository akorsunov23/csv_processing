from rest_framework import serializers


class LoadCSVSerialisers(serializers.Serializer):
    """Сериализатор для загрузки файла .csv"""

    file = serializers.FileField()

    def validate(self, file) -> bool:
        """Проверка формата файла."""
        if file.name.lower().endswith(".csv"):
            return True
        return False


class UsersSerialiser(serializers.Serializer):
    """Сериализатор ответа на запрос о покупателях."""

    username = serializers.CharField()
    spent_money = serializers.IntegerField()
    gems = serializers.ListField()


class ResponseSerializer(serializers.Serializer):
    """Сериальзатор ответа на запрос загрузки файла."""

    status = serializers.CharField()
    data = serializers.CharField()
