from django.db import models

class Category(models.Model):

    '''Категории'''
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Author(models.Model):

    '''Авторы'''
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    images = models.models.ImageField("Изображение", upload_to="authors/")
    

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Автор_detail", kwargs={"pk": self.pk})


class Genre(models.Model):

    '''Жанры'''
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Book(models.Model):

    '''Книга'''
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
#    fragment = 
    cover = models.ImageField("Изображение", upload_to="books/")
    authors = models.ManyToManyField(Author, verbose_name="авторы")
    number_of_pages = models.PositiveIntegerField("Количество страниц")
    geners = models.ManyToManyField(Genre, verbose_name="жанры")
    сategorys = models.ManyToManyField(Category, verbose_name="категории")
    url = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name
