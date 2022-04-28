

## 快速入门

* 设计模型

  ```python
  # mysite/news/models.py¶
  from django.db import models
  
  class Reporter(models.Model):
      full_name = models.CharField(max_length=70)
  
      def __str__(self):
          return self.full_name
  
  class Article(models.Model):
      pub_date = models.DateField()
      headline = models.CharField(max_length=200)
      content = models.TextField()
      reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
  
      def __str__(self):
          return self.headline
  ```

  ```python
  ...\> py manage.py makemigrations
  ...\> py manage.py migrate
  ```

* 创建虚拟环境 virtualenv

* deactivate, activate



## URL

函数 [`path()`](https://docs.djangoproject.com/zh-hans/3.0/ref/urls/#django.urls.path) 具有四个参数，两个必须参数：`route` 和 `view`，两个可选参数：`kwargs` 和 `name`。现在，是时候来研究这些参数的含义了



1. `route` 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 `urlpatterns` 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

   这些准则不会匹配 GET 和 POST 参数或域名。例如，URLconf 在处理请求 `https://www.example.com/myapp/` 时，它会尝试匹配 `myapp/` 。处理请求 `https://www.example.com/myapp/?page=3` 时，也只会尝试匹配 `myapp/`。

2. 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 [`HttpRequest`](https://docs.djangoproject.com/zh-hans/3.0/ref/request-response/#django.http.HttpRequest) 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。稍后，我们会给出一个例子。
3.  `kwargs` 任意个关键字参数可以作为一个字典传递给目标视图函数。本教程中不会使用这一特性。
4. 为你的 URL 取名能使你在 Django 的**任意地方**唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。



## DataBase

**SQLite 以外的其它数据库**

如果你使用了 SQLite 以外的数据库，请确认在使用前已经创建了数据库。你可以通过在你的数据库交互式命令行中使用 "`CREATE DATABASE database_name;`" 命令来完成这件事。

另外，还要确保该数据库用户中提供 `mysite/settings.py` 具有 "create database" 权限。这使得自动创建的 [test database](https://docs.djangoproject.com/zh-hans/3.0/topics/testing/overview/#the-test-database) 能被以后的教程使用。

如果你使用 SQLite，那么你不需要在使用前做任何事——数据库会在需要的时候自动创建。



**Install Apps 需要创建数据表**

默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。请执行以下命令：

```powershell
$ python manage.py migrate
```

所以可以在， 在创建数据表前可以将 Installed Apps 里的 app 注释掉或者删除掉 



每个模型被表示为 [`django.db.models.Model`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/instances/#django.db.models.Model) 类的子类

每个字段都是 [`Field`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.Field) 类的实例 - 比如：

* 字符字段被表示为 [`CharField`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.CharField) 
* 日期时间字段被表示为 [`DateTimeField`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.DateTimeField) 

每个 [`Field`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.Field) 类实例变量的名字（例如 `question_text` 或 `pub_date` ）也是字段名

所以最好使用对机器友好的格式。你将会在 Python 代码里使用它们，而数据库会将它们作为列名。

你可以使用可选的选项来为 [`Field`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.Field) 定义一个人类可读的名字。这个功能在很多 Django 内部组成部分中都被使用了，而且作为文档的一部分。如果某个字段没有提供此名称，Django 将会使用对机器友好的名称，也就是变量名。在上面的例子中，我们只为 `Question.pub_date` 定义了对人类友好的名字。对于模型内的其它字段，它们的机器友好名也会被作为人类友好名使用。

定义某些 [`Field`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.Field) 类实例需要**参数**。

例如 [`CharField`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.CharField) 需要一个 [`max_length`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.CharField.max_length) 参数。这个参数的用处不止于用来定义数据库结构，也用于验证数据，

[`Field`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.Field) 也能够接收多个可选参数；在上面的例子中：我们将 `votes` 的 [`default`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.Field.default) 也就是默认值，设为0。

注意在最后，我们使用 [`ForeignKey`](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.ForeignKey) 定义了一个关系。这将告诉 Django，每个 `Choice` 对象都关联到一个 `Question` 对象。Django 支持所有常用的数据库关系：多对一、多对多和一对一。

**那么， 这个关系数据库在插入的时候是怎么操作的， 底层实现**



将自定义的 app 添加到 Installed Apps 后再使用：

```powershell
$ python manage.py makemigrations polls
```



**迁移（Migrations）**是 **Django** 对于模型定义（也就是你的数据库结构）的**变化的储存形式** - 它们其实也只是一些你磁盘上的文件。如果你想的话，你可以阅读一下你模型的迁移数据，它被储存在`polls/migrations/0001_initial.py` 里。别担心，你不需要每次都阅读迁移文件，但是它们被设计成人类可读的形式，这是为了便于你手动调整Django的修改方式。

Django 有一个 ` 自动执行数据库迁移并同步管理你的数据库结构的命令` - 这个命令是 [`migrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-migrate)，我们马上就会接触它 - 但是首先，让我们看看迁移命令会执行哪些 SQL 语句。[`sqlmigrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-sqlmigrate) 命令接收一个迁移的名称，然后返回对应的 SQL：

```shell
python manage.py sqlmigrate polls 0001
```

```sql
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" integer NOT NULL
);
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");

COMMIT;
```

- 输出的内容和你使用的数据库有关，上面的输出示例使用的是 PostgreSQL。
- **表名构成** 数据库的表名是由应用名(`polls`)和模型名的小写形式( `question` 和 `choice`)连接而来。（如果需要，你可以自定义此行为。）
- **主键** (IDs)会被自动创建。(当然，你也可以自定义。)
- **外键** 默认的，Django 会在外键字段名后追加字符串 `"_id"` 。（同样，这也可以自定义。）
- 外键关系由 `FOREIGN KEY` 生成。你不用关心 `DEFERRABLE` 部分，它只是告诉 PostgreSQL，请在事务全都执行完之后再创建外键关系。
- 生成的 SQL 语句是为你所用的数据库定制的，所以那些和数据库有关的字段类型，比如 `auto_increment` (MySQL)、 `serial` (PostgreSQL)和 `integer primary key autoincrement` (SQLite)，Django 会帮你自动处理。那些和引号相关的事情 - 例如，**是使用单引号还是双引号** - 也一样会被自动处理。
- 这个 [`sqlmigrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-sqlmigrate) **命令并没有真正在你的数据库中的执行迁移 - 相反，它只是把命令输出到屏幕上**，让你看看 Django 认为需要执行哪些 SQL 语句。这在你想看看 Django 到底准备做什么，或者当你是数据库管理员，需要写脚本来批量处理数据库时会很有用。

如果你感兴趣，你也可以试试运行 [`python manage.py check`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-check) ;这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。



这个 [`migrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-migrate) 命令选中所有还没有**执行过的迁移（数据库结构的改变）**（Django 通过在数据库中创建一个特殊的表 `django_migrations` 来跟踪执行过哪些迁移）并应用在数据库上 - 也就是将你对模型的更改同步到数据库结构上。

迁移是非常强大的功能，它能让你在**开发过程中持续的改变数据库结构而不需要重新删除和创建表** - 它专注于使数据库平滑升级而不会丢失数据。我们会在后面的教程中更加深入的学习这部分内容，现在，你只需要记住，改变模型需要这三步：

- 编辑 `models.py` 文件，改变模型。
- 运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-makemigrations) 为模型的改变生成迁移文件。
- 运行 [`python manage.py migrate`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-migrate) 来应用数据库迁移。

数据库迁移被分解成生成和应用两个命令是**为了让你能够在代码控制系统上提交迁移数据并使其能在多个应用里使用**；这不仅仅会让开发更加简单，也给别的开发者和生产环境中的使用带来方便



## 数据库的API

```python
使用 python manage.py shell 可以操作数据库！
```



**模型需要的方法**

1. `__str__()`
2. 通过`__field` 访问字段

```python
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

## 模板

## 设计模板[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/overview/#design-your-templates)

上面的代码加载了 `news/year_archive.html` 模板。

Django 允许设置搜索模板路径，这样可以最小化模板之间的冗余。在 Django 设置中，你可以通过 [`DIRS`](https://docs.djangoproject.com/zh-hans/3.0/ref/settings/#std:setting-TEMPLATES-DIRS) 参数指定一个路径列表用于检索模板。如果第一个路径中不包含任何模板，就继续检查第二个，以此类推。

让我们假设 `news/year_archive.html` 模板已经找到。它看起来可能是下面这个样子：

```php+HTML
{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}
```

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

## 渲染模板

**Render** 函数

```python
# 原始写法
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

```python
# 更简单的说法
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

```python
# 抛出异常, 但是是否需要定义404页面呢？
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

```python
# 一个简单的处理404的方法
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

回过头去看看我们的 `detail()` 视图。它向模板传递了上下文变量 `question` 。下面是 `polls/detail.html` 模板里正式的代码：

polls/templates/polls/detail.html[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial03/#id11)

```python
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

模板系统统一使用点符号来访问变量的属性。在示例 `{{ question.question_text }}` 中，首先 Django 尝试对 `question` 对象使用字典查找（也就是使用 obj.get(str) 操作），如果失败了就尝试属性查找（也就是 obj.str 操作），结果是成功了。如果这一操作也失败的话，将会尝试列表查找（也就是 obj[int] 操作）。

在 [`{% for %}`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-for) 循环中发生的函数调用：`question.choice_set.all` 被解释为 Python 代码 `question.choice_set.all()` ，将会返回一个可迭代的 `Choice` 对象，这一对象可以在 [`{% for %}`](https://docs.djangoproject.com/zh-hans/3.0/ref/templates/builtins/#std:templatetag-for) 标签内部使用。



## 为 URL 名称添加命名空间[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial03/#namespacing-url-names)

教程项目只有一个应用，`polls` 。在一个真实的 Django 项目中，可能会有五个，十个，二十个，甚至更多应用。Django 如何分辨重名的 URL 呢？举个例子，`polls` 应用有 `detail` 视图，可能另一个博客应用也有同名的视图。Django 如何知道 `{% url %}` 标签到底对应哪一个应用的 URL 呢？

答案是：在根 URLconf 中添加命名空间。在 `polls/urls.py` 文件中稍作修改，加上 `app_name` 设置命名空间：

polls/urls.py[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial03/#id12)

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

现在，编辑 `polls/index.html` 文件，从：

polls/templates/polls/index.html[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial03/#id13)

```python
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

修改为指向具有命名空间的详细视图：

polls/templates/polls/index.html[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial03/#id14)

```python
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```





**注解**

我们的 `vote()` 视图代码有一个小问题。代码首先从数据库中获取了 `selected_choice` 对象，接着计算 `vote` 的新值，最后把值存回数据库。如果网站有两个方可同时投票在 *同一时间* ，可能会导致问题。同样的值，42，会被 `votes` 返回。然后，对于两个用户，新值43计算完毕，并被保存，但是期望值是44。

这个问题被称为 *竞争条件* 。如果你对此有兴趣，你可以阅读 [Avoiding race conditions using F()](https://docs.djangoproject.com/zh-hans/3.0/ref/models/expressions/#avoiding-race-conditions-using-f) 来学习如何解决这个问题。







## 使用通用视图：代码还是少点好[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial04/#use-generic-views-less-code-is-better)

这些视图反映基本的 Web 开发中的一个常见情况：根据 URL 中的参数从数据库中获取数据、载入模板文件然后返回渲染后的模板。 由于这种情况特别常见，Django 提供一种快捷方式，叫做“通用视图”系统。

通用视图将常见的模式抽象化，可以使你在编写应用时甚至不需要编写Python代码。

让我们将我们的投票应用转换成使用通用视图系统，这样我们可以删除许多我们的代码。我们仅仅需要做以下几步来完成转换，我们将：

1. 转换 URLconf。
2. 删除一些旧的、不再需要的视图。
3. 基于 Django 的通用视图引入新的视图。

为什么要重构代码？

一般来说，当编写一个 Django 应用时，你应该**先评估一下通用视图是否可以解决你的问题**，你应该在一开始使用它，而不是进行到一半时重构代码。本教程目前为止是有意将重点放在以“艰难的方式”编写视图，这是为将重点放在核心概念上。

就像在使用计算器之前你需要掌握基础数学一样。



### 改良 URLconf[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial04/#amend-urlconf)

首先，打开 `polls/urls.py` 这个 URLconf 并将它修改成：

polls/urls.py[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial04/#id6)

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

注意，第二个和第三个匹配准则中，路径字符串中匹配模式的名称已经由 `<question_id>` 改为 `<pk>`。



### 改良视图[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial04/#amend-views)

下一步，我们将删除旧的 `index`, `detail`, 和 `results` 视图，并用 Django 的通用视图代替。打开 `polls/views.py` 文件，并将它修改成：

polls/views.py[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial04/#id7)

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```

我们在这里使用两个通用视图： [`ListView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView) 和 [`DetailView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) 。这两个视图分别抽象“显示一个对象列表”和“显示一个特定类型对象的详细信息页面”这两种概念。

- 每个通用视图需要知道它将作用于哪个模型。 这由 `model` 属性提供。
- [`DetailView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) 期望从 URL 中捕获名为 `"pk"` 的主键值，所以我们为通用视图把 `question_id` 改成 `pk` 。（**Import**：在 **request** 的 **URL** 中捕获 **pk** 字段 ）

默认情况下，通用视图 [`DetailView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) 使用一个叫做 `<app name>/<model name>_detail.html` 的模板。



在我们的例子中，它将使用`"polls/question_detail.html"` 模板。`template_name` 属性是用来告诉 `Django` 使用一个指定的模板名字，而不是自动生成的默认名字。 



* 我们也为 `results` 列表视图指定了 `template_name` 这确保 `results` 视图和 `detail` 视图在渲染时具有不同的外观，即使它们在后台都是同一个 [`DetailView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) 



* 类似地，[`ListView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView) 使用一个叫做 `<app name>/<model name>_list.html` 的默认模板, 我们使用 `template_name` 来告诉 [`ListView`](https://docs.djangoproject.com/zh-hans/3.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView) 使用我们创建的已经存在的 `"polls/index.html"` 模板。



在之前的教程中，提供模板文件时都带有一个包含 `question` 和 `latest_question_list` 变量的 `context`。

对于 `DetailView` ， `question` 变量会自动提供因为我们使用 Django 的模型 (Question)， Django 能够为 `context` 变量决定一个合适的名字。



然而对于 `ListView`， 自动生成的 context 变量是 `question_list`。为了覆盖这个行为，我们提供 `context_object_name` 属性，表示我们想使用 `latest_question_list`。



作为一种替换方案，你可以改变你的模板来匹配新的 context 变量这是一种更便捷的方法，告诉 Django 使用你想使用的变量名。





### 测试部分 - 重要

测试代码，是用来检查你的代码能否正常运行的程序。

测试在不同的层次中都存在。

* 一些测试只关注某个很小的细节（某个模型的某个方法的返回值是否满足预期？），

* 一些测试可能检查对某个软件的一系列操作（*某一用户输入序列是否造成了预期的结果？*）。

*自动化* 测试是由某个系统帮你**自动完成**的。当你创建好了一系列测试，**每次修改应用代码**后，就可以自动检查出修改后的代码是否还像你曾经预期的那样正常工作。你不需要花费大量时间来进行手动测试。



**先写测试**

命令 `python manage.py test polls` 执行的步骤：

- `python manage.py test polls` 将会寻找 `polls` 应用里的测试代码
- 它找到了 [`django.test.TestCase`](https://docs.djangoproject.com/zh-hans/3.0/topics/testing/tools/#django.test.TestCase) 的一个子类
- 它创建一个  **特殊**  的数据库供测试使用， 创建一个数据库的 copy
- 它在类中寻找测试方法——以 `test` 开头的方法， 创建一定是 test 开头的方法。
- 在 `test_was_published_recently_with_future_question` 方法中，它创建了一个 `pub_date` 值为 30 天后的 `Question` 实例。
- 接着使用 `assertls()` 方法，发现 `was_published_recently()` 返回了 `True`，而我们期望它返回 `False`。

测试系统通知我们哪些测试样例失败了，和造成测试失败的代码所在的行号。

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```



### Django 测试工具之 Client[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#the-django-test-client)

Django 提供了一个供测试使用的 [`Client`](https://docs.djangoproject.com/zh-hans/3.0/topics/testing/tools/#django.test.Client) 来模拟用户和视图层代码的交互。我们能在：

* `tests.py` 
*  [`shell`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-shell) 

中使用他。

我们依照惯例从 [`shell`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-shell) 开始，首先我们要做一些在 `tests.py` 里不是必须的准备工作。第一步是**在 [`shell`](https://docs.djangoproject.com/zh-hans/3.0/ref/django-admin/#django-admin-shell) 中配置测试环境**:

```python
$ python manage.py shell
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

 提供了一个模板渲染器，允许我们为 responses 添加一些额外的属性，例如 `response.context`，未安装此 app 无法使用此功能。



**Tips:** 注意，这个方法并 *不会* 配置测试数据库，所以接下来的代码将会在当前存在的数据库上运行，输出的内容可能由于数据库内容的不同而不同。

**Tips:** 如果你的 `settings.py` 中关于 `TIME_ZONE` 的设置不对，你可能无法获取到期望的结果。如果你之前忘了设置，在继续之前检查一下。

然后我们需要导入 [`django.test.TestCase`](https://docs.djangoproject.com/zh-hans/3.0/topics/testing/tools/#django.test.TestCase) 类（在后续 `tests.py` 的实例中我们将会使用 [`django.test.TestCase`](https://docs.djangoproject.com/zh-hans/3.0/topics/testing/tools/#django.test.TestCase) 类，这个类里包含了自己的 client 实例，所以不需要这一步）:

```python
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
```

搞定了之后，我们可以要求 client 为我们工作了:

```python
>>> # get a response from '/'
>>> response = client.get('/')
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>
```

### 改善视图代码[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#improving-our-view)

现在的投票列表会显示将来的投票（ `pub_date` 值是未来的某天)。我们来修复这个问题。



**polls/views.py**[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#id4)

```python
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
```

我们需要改进 `get_queryset()` 方法，让他它能通过将 Question 的 pub_data 属性与 `timezone.now()` 相比较来判断是否应该显示此 Question。首先我们需要一行 import 语句：

**polls/views.py**[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#id5)

```python
from django.utils import timezone
```

然后我们把 `get_queryset` 方法改写成下面这样：

**polls/views.py**[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#id6)

```python
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
```

`Question.objects.filter(pub_date__lte=timezone.now())` returns a queryset containing `Question`s whose `pub_date` is less than or equal to - that is, earlier than or equal to - `timezone.now`.





让我们更详细地看下以上这些内容。

* 首先是一个快捷函数 `create_question`，它封装了创建投票的流程，减少了重复代码。

* `test_no_questions` 方法里没有创建任何投票，它检查返回的网页上有没有 "No polls are available." 这段消息和 `latest_question_list` 是否为空。注意到 [`django.test.TestCase`](https://docs.djangoproject.com/zh-hans/3.0/topics/testing/tools/#django.test.TestCase) 类提供了一些额外的 assertion 方法，在这个例子中，我们使用了 [`assertContains()`](https://docs.djangoproject.com/zh-hans/3.0/topics/testing/tools/#django.test.SimpleTestCase.assertContains) 和 [`assertQuerysetEqual()`](https://docs.djangoproject.com/zh-hans/3.0/topics/testing/tools/#django.test.TransactionTestCase.assertQuerysetEqual) 。

* 在 `test_past_question` 方法中，我们创建了一个投票并检查它是否出现在列表中。

* 在 `test_future_question` 中，我们创建 `pub_date` 在未来某天的投票。

  **Tips:** 数据库会在每次调用测试方法前被重置，所以第一个投票已经没了，所以主页中应该没有任何投票。

实际上，测试就是**假装一些管理员的输入**，然后通过**用户端的表现是否符合预期**来判断新加入的**改变是否破坏了原有的系统状态**。









### 测试 `DetailView`[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#testing-the-detailview)

我们的工作似乎已经很完美了？不，还有一个问题：

就算在发布日期时未来的那些投票不会在目录页 *index* 里出现，但是如果用户知道或者猜到正确的 URL ，还是可以访问到它们。所以我们得在 `DetailView` 里增加一些约束.

简单地说就是 有可能 不合法的 **urls** 也是可以被访问到。

**polls/views.py[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#id9)**

```python
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```



当然，我们将增加一些测试来检验 `pub_date` 在过去的 `Question` 可以显示出来，而 `pub_date` 在未来的不可以：

**polls/tests.py[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#id10)**

```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```



「这么多的测试不会使代码越来越复杂吗？」。



## 当需要测试的时候，测试用例越多越好[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/#when-testing-more-is-better)

貌似我们的测试多的快要失去控制了。按照这样发展下去，测试代码就要变得比应用的实际代码还要多了。而且测试代码大多都是重复且不优雅的，特别是在和业务代码比起来的时候，这种感觉更加明显。

**但是这没关系！** 就让测试代码继续肆意增长吧。大部分情况下，你写完一个测试之后就可以忘掉它了。在你继续开发的过程中，它会一直默默无闻地为你做贡献的。

但有时测试也需要更新。想象一下如果我们修改了视图，只显示有选项的那些投票，那么只前写的很多测试就都会失败。*但这也明确地告诉了我们哪些测试需要被更新*，所以测试也会测试自己。

最坏的情况是，当你继续开发的时候，发现之前的一些测试现在看来是多余的。但是这也不是什么问题，多做些测试也 *不错*。

如果你对测试有个整体规划，那么它们就几乎不会变得混乱。下面有几条好的建议：

- 对于每个 **模型** 和 **视图** 都建立单独的 `TestClass`
- 每个测试方法只测试**一个功能**
- 给每个测试方法起个能描述其功能的名字







## 自定义 *应用* 的界面和风格[¶](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial06/#customize-your-app-s-look-and-feel)

首先，在你的 `polls` 目录下创建一个名为 `static` 的目录。

Django 的 [`STATICFILES_FINDERS`](https://docs.djangoproject.com/zh-hans/3.0/ref/settings/#std:setting-STATICFILES_FINDERS) 设置包含了一系列的查找器，它们知道去哪里找到 static 文件。`AppDirectoriesFinder` 是默认查找器中的一个，它会在每个 [`INSTALLED_APPS`](https://docs.djangoproject.com/zh-hans/3.0/ref/settings/#std:setting-INSTALLED_APPS) 中指定的应用的子文件中寻找名称为 `static` 的特定文件夹，就像我们在 `polls` 中刚创建的那个一样。管理后台采用相同的目录结构管理它的静态文件。

在你刚创建的 `static` 文件夹中创建一个名为 `polls` 的文件夹，再在 `polls` 文件夹中创建一个名为 `style.css` 的文件。

例如，你的样式表路径应是 `polls/static/polls/style.css`。因为 `AppDirectoriesFinder` 的存在，你可以在 Django 中以 `polls/style.css` 的形式引用此文件，类似你引用模板路径的方式。