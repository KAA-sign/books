from django.contrib import admin
from .models import Category, Author, Genre, Book, TextBook, RatingStar, Rating, Reviews


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(TextBook)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)