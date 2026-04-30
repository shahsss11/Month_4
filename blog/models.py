from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='напишите название блога')
    description = models.TextField(verbose_name='напишите статью', blank=True)
    image = models.ImageField(upload_to='blog/', verbose_name='загрузите изображение')
    blog_file = models.FileField(upload_to='blog/', verbose_name='загрузите pdf файл')
    TYPE_BLOG = (
        ('програмирование', 'програмирование'),
        ('бизнес', 'бизнес'),
        ('медицина', 'медицина'),
    )
    quantity = models.PositiveIntegerField(verbose_name='Укажите количество страниц', default=0,null=True)
    type_blog = models.CharField(max_length=100, choices=TYPE_BLOG, default='програмирование') 
    createted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title