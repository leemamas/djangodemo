# django学习之路
## ORM增删改操作
- 关系对象映射（Object Relational Mapping，简称ORM）。

每个模型在Django中的存在形式为一个Python类
每个模型都是django.db.models.Model的子类,
模型里的每个类代表数据库中的一个表,
模型的每个字段（属性）代表数据表的某一列,
Django将自动为你生成数据库访问API.
这种操作数据库的方式,称为orm！