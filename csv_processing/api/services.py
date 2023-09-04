from typing import Union

from django.db.models.aggregates import Count, Sum

from .models import TransactionHistory
from django.core.cache import cache

def load_csv_data(csv_reader: dict) -> Union[bool, tuple]:
    """Обработка и загрузка данных .csv в БД."""

    try:
        TransactionHistory.objects.bulk_create(
            [
                TransactionHistory(
                    customer=row["customer"],
                    item=row["item"],
                    total=row["total"],
                    quantity=row["quantity"],
                    date=row["date"],
                )
                for row in csv_reader
            ]
        )
        cache.delete(key='favorites')
        return True
    except Exception as ex:
        print(ex.args)
        return False, ex.args


def get_favorites():
    """Фильтрация модели сделок для получения фаворитов."""
    
    try:
        result = cache.get(key='favorites')
        if result is not None:
            return result
        top_customers = (
            TransactionHistory.objects.values("customer")
            .annotate(spent_money=Sum("total"))
            .order_by("-spent_money")[:5]
        )
        gems = (
            TransactionHistory.objects.values("item")
            .annotate(bought_by=Count("customer", distinct=True))
            .filter(
                bought_by__gte=2,
                customer__in=top_customers.values_list("customer", flat=True),
            )
            .values_list("item", flat=True)
            .distinct()
        )
        result: list = []
        for customer in top_customers:
            result.append(
                {
                    "username": customer["customer"],
                    "spent_money": customer["spent_money"],
                    "gems": list(gems),
                }
            )
        cache.set(key='favorites', value=result)
        return result
    except Exception as ex:
        return ex
