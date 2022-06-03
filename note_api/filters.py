from typing import Optional

from django.db.models import QuerySet
from note import models

# Фильтр по важности
def note_by_important_filter(queryset: QuerySet, important: Optional[bool]): # Фильтр по важности
    return queryset.filter(important=important)

# Фильтр по публичности
def note_by_public_filter(queryset: QuerySet, public: Optional[bool]): # Фильтр по важности
    return queryset.filter(public=public)