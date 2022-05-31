from django.contrib import admin
from .models import Note

#admin.site.register(Note)
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Поля для отображения в админке
    list_display = ['title', 'status', 'public', 'important', 'date_plan']
    # Группировка полей в режиме редактирования
    fields = ('title', 'note', 'status', ('public', 'important'), 'date_plan', 'author')
    # Поля только для чтения в режиме редактирования
    #readonly_fields = ('author',)
    # Поиск по выбранным полям
    search_fields = ['title', 'note']
    # Фильтры
    list_filter = ['status', 'public', 'important', 'author']