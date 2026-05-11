from django.db import models


class CategoryCar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Car(models.Model):
    title = models.CharField(max_length=50, default='Lexus RX 300')
    categories = models.ManyToManyField(CategoryCar, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}--{', '.join(i.name for i in self.categories.all())}'
    

class NummerCar(models.Model):
    choice_car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='nummer_car', null=True)
    number_car = models.CharField(max_length=100, default='0_KG____')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_car}---{self.number_car}'



class ReviewCar(models.Model):
    choice_car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    MARKS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5','5')
    )
    marks = models.CharField(max_length=100, choices=MARKS, default='5')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_car}---{self.marks}'
    