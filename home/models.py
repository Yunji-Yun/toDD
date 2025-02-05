from django.db import models
from django.contrib.auth.models import User
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/home/category/{self.slug}'

class Post(models.Model):
    # 투두 리스트 제목
    title = models.CharField(max_length=30)
    # 투두 리스트 상세 내용
    content = models.TextField()
    # 데드라인
    deadline = models.DateTimeField(auto_now=False)
    # 작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # 카테고리
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # 완료 여부
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'check_details_{self.pk}/'
