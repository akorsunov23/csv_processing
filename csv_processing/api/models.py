from django.core.cache import cache
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver


class TransactionHistory(models.Model):
    """Модель истории сделок."""

    customer = models.CharField(verbose_name="покупатель")
    item = models.CharField(verbose_name="наименование товара")
    total = models.IntegerField(verbose_name="cумма сделки")
    quantity = models.PositiveIntegerField(verbose_name="количество товара")
    date = models.DateTimeField(verbose_name="дата и время сделки")

    class Meta:
        verbose_name = "сделка"
        verbose_name_plural = "сделки"

    def __str__(self) -> str:
        return f"Сделка №{self.pk} от {self.date.date}"


@receiver(pre_delete, sender=TransactionHistory)
@receiver(pre_save, sender=TransactionHistory)
def on_delete_cache(**kwargs):
    """Удаление кэша при изменении Истории сделок."""
    cache.delete(key="favorites")
