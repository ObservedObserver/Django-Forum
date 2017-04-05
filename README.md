# Django-Forum
A Django Forum with SemanticUI<br>单纯为了测试Django的使用体验，所以舍弃了所有Js操作，部分功能的实现会轻微蛋疼<br>
<a href='https://www.djangoproject.com/'>PythonWeb框架:Django</a> + <a href='http://www.semantic-ui.com/'>UI框架:SemanticUI</a>
## 使用

### 安装Django

> pip install Django

### 搭建本地服务器并创建合并数据库

> python manage.py runserver<br>
> python manage.py makemigrations<br>
> python manage.py migrate<br>
	
### 创建网站管理员账户

> python manage.py createsuperuser
	
访问localhost/admin即可进入数据库

## Demo

这里将展示部分界面的样式<br>
---
主页样式
![Alt text](./demo/D01.png "主页样式")
<br>------
文章详情页
![Alt text](./demo/D02.png)
<br>------评论
![Alt text](./demo/D03.png)
<br>------再编辑修改
![Alt text](./demo/D05.png)
