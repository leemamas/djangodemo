from django.db import models

# Create your models here.

class BaseModel(models.Model):
    is_datele=models.BooleanField(default=False)
    create_time=models.DateTimeField(auto_now_add=True)
    modify_time=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class Book(BaseModel):
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    publish=models.ForeignKey('Publish',on_delete=models.CASCADE)
    authors=models.ManyToManyField('Author')


class Publish(BaseModel):
    name=models.CharField(max_length=32)


class Author(BaseModel):
    name=models.CharField(max_length=32)

class AuthorDetail(BaseModel):
    author=models.OneToOneField('Author',on_delete=models.DO_NOTHING)
    age=models.IntegerField()