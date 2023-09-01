from rest_framework import serializers


class LoadCSVSerialisers(serializers.Serializer):
    """Сериализатор для загрузки файла .csv"""

    file = serializers.FileField()

    def validate(self, file) -> bool:
        """Проверка формата файла."""
        if file.name.lower().endswith(".csv"):
            return True
        return False
