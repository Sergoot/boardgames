import datetime

from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from django.utils import timezone

rate_choices = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
CAT_CHOICES = [('Cтратегия','Cтратегия'),('На двоих','На двоих'),('Экономическая','Экономическая'),('Кооперативная','Кооперативная'),('Вечеринка','Вечеринка')]

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CAT_CHOICES, max_length=255,default='Стратегия')
    # publisher = models.CharField(max_length=50)
    short_dscr = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=700)
    img = models.ImageField(upload_to='images/',blank=True)
    img1 = models.ImageField(upload_to='images/',blank=True)
    img2 = models.ImageField(upload_to='images/',blank=True)
    img3 = models.ImageField(upload_to='images/',blank=True)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    rating = models.IntegerField(default=0, null=True, blank=True, choices=rate_choices)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    user_rate = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Vote(models.Model):
#     value = models.SmallIntegerField()
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     voted_on = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         unique_together = ('user', 'game')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255, default='гость')
    post = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, related_name='comment')
    pub_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(default='')
    active = models.BooleanField(default=True)
