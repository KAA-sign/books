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
    images = models.ImageField("Изображение", upload_to="authors/")
    

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
    fragment = models.TextField("Отрывок")
    cover = models.ImageField("Изображение", upload_to="books/")
    authors = models.ManyToManyField(Author, verbose_name="автор", related_name="book_author")
    number_of_pages = models.PositiveIntegerField("Количество страниц", default=0)
    geners = models.ManyToManyField(Genre, verbose_name="жанры")
    сategory = models.ForeignKey(Category, verbose_name="категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

class TextBook(models.Model):

    '''Текст книги'''
    title = models.CharField("Название", max_length=150)
    text_book = models.TextField("Текст")
    images = models.ImageField("Изображение", upload_to="text_book/")
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Текст книги"
        verbose_name_plural = "Тексты книг"

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    
    '''Звезда рейтинга'''
    value = models.PositiveSmallIntegerField("Значенние", default=0)

    def __str__(self):
        return self.value 

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

class Rating(models.Model):
    
    '''Рейтинг'''

    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name='звезда', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name="книга", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.book}'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинг"

class Reviews(models.Model):
    
    '''Отзывы'''

    email = models.EmailField()
    name = models.CharField('Имя', max_length = 100)
    message = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    book = models.ForeignKey(Book, verbose_name="книга", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} - {self.book}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы" 