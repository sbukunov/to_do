from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from note.models import Note
from . import serializers

class NoteListCreateAPIView(ListAPIView):
    """Представление, которое позволяет вывести весь список и добавить новую запись"""

#class NoteListCreateAPIView(APIView): # Это старый сериализатор
    #def get(self, request: Request):
        #objects = Note.objects.all() # Получаем все объекты из БД
        #serializer = serializers.NoteSerializer(  #Сериализуем данные
            #instance = objects,
            #many = True
        #)
        #return Response(serializer.data) # Возвращаем JSON-объекты
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer

    ordering = ["date_plan", "important"] #Сортировка сначала по дате, затем по важности

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(author=user)
        #user_1 = queryset[6]
        #if(user == user_1):
            #return queryset.filter(author = user)
        #else:
            #return queryset.filter(public = True)

    def post(self, request: Request):
        # Передаем в сериалайзер данные из запроса
        serializer = serializers.NoteSerializer(data=request.data)

        # Проверка параметров
        if not serializer.is_valid():  # Проверяем "сырые" данные на валидность,
            # поскольку данные пришли от пользователя, а не из БД
            return Response(
                serializer.errors,  # Здесь будут все ошибки - отдаем их пользователю
                status=status.HTTP_400_BAD_REQUEST
            )
        # Записываем новую запись в БД и добавляем в качестве автора пользователя из request
        serializer.save(author=request.user)  # Передаем в БД пользователя из request
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

class NoteDetailAPIView(APIView):
    """Представление, которое позволяет вывести отдельную запись"""
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk) # Получаем ORM-объект по pk
        serializer = serializers.NoteDetailSerializer( # Новый сериализатор
            instance=note, # Здесь не указываем many = True, потому что объект один
        )
        return Response(serializer.data) #Возвращаем сериализованный JSON-объект

    def put(self, request, pk):
        note_one = get_object_or_404(Note, pk=pk) #Получаем python-объект из базы данных по pk
        # Проверка пользователя
        if (note_one.author != request.user):
            return Response(
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = serializers.NoteSerializer(
            instance = note_one, data = request.data
        )
        serializer.is_valid(raise_exception=True) # Проверяем на наличие ошибок
        serializer.save() # Сохраняем обновленный объект в БД
        return Response(serializer.data)

    def patch(self, request, pk):
        note_one = get_object_or_404(Note, pk=pk)  # Получаем python-объект из базы данных по pk
        # Проверка пользователя
        if (note_one.author != request.user):
            return Response(
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = serializers.NoteSerializer(
            instance=note_one, data=request.data, partial = True
        )
        serializer.is_valid(raise_exception=True)  # Проверяем на наличие ошибок
        serializer.save()  # Сохраняем обновленный объект в БД
        return Response(serializer.data)

    def delete(self, request, pk):
        note_one = get_object_or_404(Note, pk=pk)  # Получаем python-объект из базы данных по pk
        # Проверка пользователя
        if (note_one.author != request.user):
            return Response(
                status=status.HTTP_403_FORBIDDEN
            )
        note_one.delete() # Удаляем объект из БД
        return Response(status = status.HTTP_204_NO_CONTENT) # Возвращаем сообщение "нет содержимого"

class ImportantNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteDetailSerializer # Используем уже существующий сериализатор

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(important=True)

class PublicNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteDetailSerializer # Используем уже существующий сериализатор

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)

class ActiveNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteDetailSerializer # Используем уже существующий сериализатор

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status=1)

class HoldNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteDetailSerializer # Используем уже существующий сериализатор

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status=2)

class DoneNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteDetailSerializer # Используем уже существующий сериализатор

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status=3)

class StatusNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteDetailSerializer # Используем уже существующий сериализатор

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status=1 or 3)