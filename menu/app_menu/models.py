from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    """ Модель Меню """
    title = models.CharField(max_length=255, unique=True, verbose_name='name_menu')
    slug = models.SlugField(max_length=255,
                            db_index=True,
                            verbose_name='url',
                            )
    
    def __str__(self):
        return self.title


class MenuCategory(MPTTModel, models.Model):
    """ Модель Категория """
    name = models.CharField(max_length=255,unique=True, verbose_name='name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                        related_name="children", verbose_name='parent category')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True, verbose_name='name_menu')
    slug = models.SlugField(max_length=255,
                            db_index=True,
                            verbose_name='url',
                            )
    
    def get_absolute_url(self):
        return reverse('sub_menu', kwargs={'name_menu': self.menu.slug, 'name_node': self.slug})
    
    
    def __str__(self):
        return self.name
    
    
    class MPTTMeta:
        order_insertion_by = ['name']