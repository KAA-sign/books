from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View 


from .models import Book



class BookView(ListView):
    '''Спссок книг'''
    
    model = Book
    queryset = Book.objects.filter(draft=False)
    template_name = 'books/books.html'


class BookDetailView(DetailView):
    '''Полное описание книги'''
    
    model = Book
    slug_field = "url"


