from rest_framework import serializers
from note.models import Note
import datetime, time

class NoteSerializer(serializers.ModelSerializer):
    """Сериалайзер для всех записей"""

    # Переопределяем представление поля author
    author = serializers.SlugRelatedField(
        slug_field="username", # Создаем новое поле для отображения
        read_only=True  # Поле только для чтения
    )

    #Переопределяем представление поля status
    status = serializers.SerializerMethodField('get_status')
    def get_status(self, obj: Note):
        return obj.get_status_display()

    class Meta:
        model = Note
        #fields = "__all__" # Выбираем все поля модели
        fields = ("id", "title", "note", "status", "public", "important", "author", "date_plan",) # Так выбираем только нужные поля
        #exclude = ("note", ) # Выбираем все поля, кроме перечисленных
        #read_only_fields = ("author",) #Делаем поле доступным только для чтения

    #def to_representation(self, instance):
        #"""Переформатирование вывода даты в ответе"""
        #ret = super().to_representation(instance)
        # Конвертируем строку в старом формате в дату
        #date_plan_str = time.strptime(ret['date_plan'], '%Y-%m-%dT%H:%M:%SZ')
        # Конвертируем дату обратно в строку, но уже по новому формату
        #str_date_plan = time.strftime('%d %B %Y %H:%M:%S', date_plan_str)
        #Записываем в наше поле значение даты в новом формате
        #ret['date_plan'] = str_date_plan
        #return ret

class NoteDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер для одной записи"""

    # Переопределяем представление поля author
    author = serializers.SlugRelatedField(
        slug_field="username", # Создаем новое поле для отображения
        read_only = True # Поле только для чтения
    )
    # Переопределяем представление поля status
    status = serializers.SerializerMethodField('get_status')
    def get_status(self, obj: Note):
        return obj.get_status_display()

    class Meta:
        model = Note
        fields = ("id", "title", "note", "status","public","important", "date_plan", # Эти поля берем из модели
                  "author") # Это поле берем из сериализатора

    #def to_representation(self, instance):
        #"""Переформатирование вывода даты в ответе"""
        #ret = super().to_representation(instance)
        # Конвертируем строку в старом формате в дату
        #date_plan_str = time.strptime(ret['date_plan'], '%Y-%m-%dT%H:%M:%S.%fZ')
        # Конвертируем дату обратно в строку, но уже по новому формату
        #str_date_plan = time.strftime('%d %B %Y %H:%M:%S', date_plan_str)
        #Записываем в нашу поле значение даты в новом формате
        #ret['date_plan'] = str_date_plan
        #return ret

