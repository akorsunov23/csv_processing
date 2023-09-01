from typing import Union
from .models import TransactionHistory


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
        return True
    except Exception as ex:
        print(ex.args)
        return False, ex.args
