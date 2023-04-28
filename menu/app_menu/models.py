from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MenuCategory(MPTTModel):
    """ Модель Категория """
    name = models.CharField(max_length=255,unique=True, verbose_name='name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                        related_name="children", verbose_name='parent category')
    slug = models.SlugField(max_length=255,
                            db_index=True,
                            verbose_name='url',
                            help_text='unique url fragment based on the category name'
                            )

    def __str__(self):
        return self.name
    
    
    class MPTTMeta:
        order_insertion_by = ['name']