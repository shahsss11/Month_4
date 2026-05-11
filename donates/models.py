from django.db import models
from blog.models import Blog

class Donate(models.Model):
    name = models.CharField(max_length=20, verbose_name='ваше фио')
    choice_blog = models.ForeignKey(Blog, verbose_name='выберите блог для покупки', 
                                    on_delete=models.CASCADE)
    number_card = models.PositiveIntegerField(default='41695853')
    photo = models.ImageField(upload_to='donate/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}-{self.choice_blog}'
    