from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import People,Article,Comment, Ticket
from django.template import Context, Template
from firstapp.form import commentForm, articleForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.core.exceptions import ObjectDoesNotExist
import datetime
# Create your views here.

def blog(request, cate=None, page_num=None):
    context={}
    queryOrder=request.GET.get('orderBy');
    #文章排序器
    if queryOrder:
        queryOrder='-'+queryOrder
        if cate:
            article_list=Article.objects.filter(tag=cate).order_by(queryOrder)
        else:
            article_list=Article.objects.all().order_by(queryOrder)
    else:
        if cate:
            article_list=Article.objects.filter(tag=cate)
        else:
            article_list=Article.objects.all()
    #文章分页器
    page_robot = Paginator(article_list,10)
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    #文章列表
    context['article_list']=article_list
    #分类参数
    context['cate']=cate

    index_page=render(request, 'index.html', context)
    return index_page



def detail(request, aid):
    context={}
    #获取文章并修改文章访问量
    article = Article.objects.get(id=aid)
    article.views = article.views+1
    article.save()

    if request.method == 'GET':
        form = commentForm
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            name = request.user
            comment = form.cleaned_data['comment']
            c = Comment(name=name, comment=comment, belong_to=article)
            c.save()
            return redirect(to='detail',aid=aid)

    #获取投票/点赞状态
    try:
        User_vote = Ticket.objects.get(of_Article=article, of_User=request.user)
        context['User_vote'] = User_vote
    except:
        pass

    #best_comment为最佳评论功能，还在开发中
    best_comment = Comment.objects.filter(belong_to=article, best_comment=True)
    if best_comment:
        context['best_comment'] = best_comment[0]
    if article.author == request.user:
        context['IDchecked'] = True

    context['form'] = form
    context['article'] = article

    detail_page = render(request, 'detail.html', context)
    return detail_page


#投票/点赞 (分离
def detail_vote(request, aid):
    #该部分被访问就修改投票数据
    article = Article.objects.get(id=aid)
    try:
        vote = Ticket.objects.get(of_User=request.user, of_Article=article)
        if vote.vote == 'like':
            vote.vote = 'dislike'
            article.favs = article.favs - 1
        else:
            vote.vote = 'like'
            article.favs = article.favs + 1
    except:
        vote = Ticket(of_User=request.user, of_Article=article, vote='like')
        article.favs = article.favs + 1

    vote.save()
    article.save()
    return redirect(to='detail', aid=aid)


def publish(request):
    context={}
    if request.method=='GET':
        form = articleForm
    if request.method=='POST':
        form = articleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tag = form.cleaned_data['tag']
            author = request.user
            c = Article(
                title=title,
                content=content,
                createtime = datetime.datetime.now(),
                tag=tag,
                author = author
            )
            c.save()
            return redirect(to='blog')

    context['form'] = form
    detail_page = render(request, 'publish.html', context)
    return detail_page

def editArticle(request, aid):
    context = {}
    article = Article.objects.get(id=aid)
    if request.method == 'GET':
        form = articleForm()
        # form.title = article.title
        # form.content = article.content
        # form.tag = article.tag
        form_data={'title':article.title,'content':article.content,'tag':article.tag}
        form = articleForm(initial=form_data)
        #print(form.title)
        # print("===================")
        # print(form.content)
        # print("===================")
        # print(form.tag)
    if request.method == 'POST':
        form = articleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.content = form.cleaned_data['content']
            article.tag = form.cleaned_data['tag']
            article.save()
            return redirect(to='detail',aid=aid)
    context['form'] = form
    context['article'] = article
    context['editable'] = True
    detail_page = render(request, 'detail.html', context)
    return detail_page


def userLogin(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='blog')

    context['form'] = form
    detail_page = render(request, 'log.html', context)
    return detail_page



def userSignup(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='userLogin')
    context['form'] = form
    detail_page = render(request, 'log.html', context)
    return detail_page
