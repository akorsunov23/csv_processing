from django.contrib import admin
from .models import TransactionHistory


@admin.register(TransactionHistory)
class TransactionHistoryAdmin(admin.ModelAdmin):
    """Регистрация модели сделок в админ-панели."""

    list_display = ("customer", "item", "total", "quantity", "date")
