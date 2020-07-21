from django.shortcuts import render,HttpResponse
from . import models

def add(request):
    #method1
    # models.Publish.objects.create(name='清华出版社')

    #method2
    # obj=models.Publish(name='北大出版社')
    # obj.save()

    #method3
    data={'name':'中大出版社'}
    models.Publish.objects.create(**data)

    return HttpResponse('ok')

def list(request):
    obj=models.Publish.objects.all()
    return HttpResponse('xxxx')

def delete(request):
    models.Publish.objects.filter(pk=1).delete()
    return HttpResponse('delete ok!')

def update(request):
    models.Publish.objects.filter(pk=2).update(name='xxxx111')
    return HttpResponse('update ok!')