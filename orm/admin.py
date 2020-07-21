from django.contrib import admin
from . import models
# Register your models here.



@admin.register(models.Publish)
class PublishAdmin(admin.ModelAdmin):
    list_display = ['id','name','create_time','my']
    actions_on_top = False
    actions_on_bottom = True

    def func(self, request, queryset):
        pass

    func.short_description = "自定义action"
    actions = [func, ]

    def my(self,request):
        return 'xxxx'

    my.short_description = '定义的列'

    search_fields = ['name']
    list_filter = ['name']  # 右侧栏过滤器，按作者进行筛选
    date_hierarchy = 'create_time'  # 详细时间分层筛选　



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(models.Author,AuthorAdmin)