from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookView.as_view()),
    path("<int:pk>", views.BookDetailView.as_view())
]