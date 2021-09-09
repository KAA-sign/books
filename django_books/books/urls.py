from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookView.as_view()),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="book_detail")
]