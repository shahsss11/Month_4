from django.contrib import admin
from . import models

admin.site.register(models.Car)
admin.site.register(models.NummerCar)
admin.site.register(models.ReviewCar)
admin.site.register(models.CategoryCar)
