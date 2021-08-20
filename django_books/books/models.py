from django.db import models

class Category(models.Model):

    '''Категории'''
    name = models.models.CharField(_("Категория"), max_length=150)
    description = models.TextField(_("Описание"))
    url = models.SlugField(max_length=150)


    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

