from datetime import datetime

from django.core.exceptions import ValidationError

def has_no_numbers(field: str):
    if not field.isalpha():
        raise ValidationError('Invalid symbol')


def check_year(field: int):
    if not  0 < field <= datetime.now().year:
        raise ValidationError(f'Year must be in range between 0 and {datetime.now().year}')
