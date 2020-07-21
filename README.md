# django学习之路
## ORM增删改操作
- 关系对象映射（Object Relational Mapping，简称ORM）。

每个模型在Django中的存在形式为一个Python类
每个模型都是django.db.models.Model的子类,
模型里的每个类代表数据库中的一个表,
模型的每个字段（属性）代表数据表的某一列,
Django将自动为你生成数据库访问API.
这种操作数据库的方式,称为orm！

## 定制Admin管理后台
* 注册需要的应用
> 装饰器注册
```python
@admin.register(models.Publish)
```
* 注册参数,admin中注册绑定
```python
admin.site.register(models.Author)
```
* 后台模型管理的类创建
```python
@admin.register(models.Publish)
class PublishAdmin(admin.ModelAdmin):
    list_display = ['id','name','create_time']
```
- 指定显示字段list_display=[]
- 每页显示多少条记录list_per_page = 50
- 排序ordering = ('-created_time',)
- 可编辑字段list_editable = ['name']
- 显示外键字段fk_fields = ['category']
- 操作选项显示
    actions_on_top = False ,
    actions_on_bottom = True
- 定义action方法
```python
    def func(self, request, queryset):
        pass

    func.short_description = "自定义action"
    actions = [func, ]
```
- 方法作为列
```python
    list_display = ['id','name','create_time','my']

    def my(self,request):

        print('xxxxx!!',self.name)
        return 'xxxx'

    my.short_description = '定义的列'
```
- 搜索框
search_fields=['name']

- 右侧栏过滤器和日期筛选list_filter = ['name'] 

- 日期筛选属性：date_hierarchy='create_time'