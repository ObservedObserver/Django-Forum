from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField(null=True, blank=True)
    img = models.CharField(null=True, blank=True, max_length=200)
    views = models.IntegerField(default=0)
    favs = models.IntegerField(default=0)
    createtime = models.DateField(null=True, blank=True)
    author = models.ForeignKey(to=User, related_name='under_articles', null=True, blank=True)
    TAG_CHOICES=(
    ('life','Life'),
    ('tech','Tech'),
    )
    tag = models.CharField(null=True, blank=True, max_length=20, choices=TAG_CHOICES)
    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.ForeignKey(to=User, related_name='under_comments', null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    belong_to = models.ForeignKey(to=Article, related_name='under_comments', null=True, blank=True)
    best_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.name

#用户额外信息，储存头像url
class UserInfo(models.Model):
    belong_to = models.OneToOneField(to=User,related_name='info')
    img = models.CharField(null=True, blank=True, max_length=200)



class Ticket(models.Model):
    of_Article = models.ForeignKey(to=Article, related_name='under_tickets', null=True, blank=True)
    of_User = models.ForeignKey(to=User, related_name='under_tickets', null=True, blank=True)
    VOTE_CHOICE=(('like','like'),('dislike','dislike'),('init','init'))
    vote = models.CharField(null=True, blank=True, max_length=20, choices=VOTE_CHOICE)

    def __str__(self):
        return str(self.id)
