from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.PositiveIntegerField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=250)
    release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='release_date')
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True)

#  def save(self, *args, **kwargs):
#        if not self.slug:
#            self.slug = slugify (self.name)
#        return super().save(*args, **kwargs) - models