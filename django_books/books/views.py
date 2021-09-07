from django.shortcuts import render
from django.views.generic.base import View 


from .models import Book



class BookView(View):
    '''Спссок книг'''
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/books.html', {'book_list': books})


class BookDetailView(View):
    '''Полное описание книги'''
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        return render(request, 'books/book_detail.html', {'book': book})

