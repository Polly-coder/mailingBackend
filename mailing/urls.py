from django.contrib import admin
from django.urls import path, include
from mailing import views



urlpatterns = [
    path('/mailing/all/', views.MailingListView.as_view()),
    path('/mailing/create/', views.MailingCreateView.as_view()),
    path('/mailing/detail/<int:pk>/', views.MailingDetailView.as_view()),
    path('/client/create/', views.ClientCreateView.as_view()),
    path('/client/detail/<int:pk>/', views.ClientDetailView.as_view()),
    path('/message/create/', views.MessageCreateView.as_view()),
    path('/message/all/', views.MessageListView.as_view()),
]