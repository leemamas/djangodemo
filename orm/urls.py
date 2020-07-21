# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2020/7/22  0:41

from django.urls import path
from . import views

urlpatterns=[
    path('add/',views.add),
    path('list/',views.list),
    path('delete/',views.delete),
    path('update/',views.update),
]