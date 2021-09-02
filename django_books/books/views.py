from django.shortcuts import render
from django.views.generic.base import View


from .models import Book



class BookView(View):
    '''Спссок книг'''
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/book_list.html', {'book_list': books})
