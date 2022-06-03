from typing import Optional

from django.db.models import QuerySet
from note import models

# Фильтр по важности
def note_by_important_filter(queryset: QuerySet, important: Optional[bool]):
    if important:
        return queryset.filter(important=important)
    else: # Если параметр фильтрации не задан, то возвращаем исходный queryset
        return queryset

# Фильтр по публичности
def note_by_public_filter(queryset: QuerySet, public: Optional[bool]):
    if public:
        return queryset.filter(public=public)
    else:
        return queryset # Если параметр фильтрации не задан, то возвращаем исходный queryset

# Фильтр по статусу
def note_by_status_filter(queryset: QuerySet, status: Optional[int]):
    if status:
        return queryset.filter(status=status)
    else:
        return queryset # Если параметр фильтрации не задан, то возвращаем исходный queryset