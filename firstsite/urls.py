"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.views import blog, detail, publish, userLogin, userSignup, detail_vote, editArticle
from django.contrib.auth.views import logout
urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/(?P<cate>[A-Za-z]+)$', blog, name='blog'),
    url(r'^blog/$', blog, name='blog'),
    url(r'^blog/(?P<cate>[A-Za-z]+)/(?P<page_num>\d+)$', blog, name='blog'),
    url(r'^blog/(?P<page_num>\d+)/$', blog, name='blog'),
    url(r'^detail/(?P<aid>\d+)$', detail, name='detail'),
    url(r'^publish', publish, name='publish'),
    url(r'^userLogin', userLogin, name='userLogin'),
    url(r'^userSignup', userSignup, name='userSignup'),
    url(r'^logout', logout, {'next_page':'/userLogin'}, name='logout'),
    url(r'^detail_vote/(?P<aid>\d+)$', detail_vote, name='detail_vote'),
    url(r'^detail/edit/(?P<aid>\d+)$', editArticle, name='editArticle'),
]
