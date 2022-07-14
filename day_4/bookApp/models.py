from django.db import models

# Create your models here.
"""
Model represent inf in author
"""
class Author(models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 200)
    status = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.name}-{self.last_name}'
"""
category model
"""
class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField (max_length = 200)
    status = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.name}-{self.description}'

class Book (models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    isbn = models.CharField(max_length = 13)
    status = models.BooleanField(default = True)
    idAuthor = models.ForeignKey(Author, on_delete = models.CASCADE)
    idCategory = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.idAuthor}'
"""
Author.objects.all()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
"""