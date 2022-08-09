from http import client
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from mailing.serializers import MailingSerializer, ClientSerializer, MessageSerializer
from mailing.models import Mailing, Client, Message

from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

# добавления новой рассылки со всеми её атрибутами
class MailingCreateView(generics.CreateAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()
    

# получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам
class MailingListView(generics.ListAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

# обновления атрибутов рассылки, удаления рассылки, обработки активных рассылок и отправки сообщений клиентам
class MailingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

# добавления нового клиента в справочник со всеми его атрибутами
class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

# обновления данных атрибутов клиента, удаления клиента из справочника
class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

# получения детальной статистики отправленных сообщений по конкретной рассылке
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('status')

    def get(self, request, *args, **kwargs):
        queryset = Message.objects.filter(mailing_id=request.GET['id']) # фильтрует по mailing ig
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)
   