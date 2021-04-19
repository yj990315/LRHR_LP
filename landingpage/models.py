from django.db import models
from django.contrib.auth.models import User
class Estimate(models.Model):
    PURPOSE = (
        ('a', '수선'),
        ('l', '세탁'),
        ('r', '리폼'),
    )
    purpose_of_estimate = models.CharField(
        max_length=1,
        choices=PURPOSE,
        blank=True,
        default='a',
        help_text='패피스에 고객님의 소중한 상품을 맡기시는 목적을 선택해주세요.',
    )
    TYPE = (
        ('b', '가방'),
        ('t', '바지'),
        ('s', '신발'),
    )
    type_of_product = models.CharField(
        max_length=1,
        choices=TYPE,
        blank=True,
        default='b',
        help_text='고객님의 상품의 종류를 선택해주세요',
    )
    brand = models.CharField(
        max_length = 100,
        help_text = '고객님의 상품의 브랜드를 입력해주세요',
    )
    create_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Request(models.Model):
    estimate = models.ForeignKey('Estimate', on_delete = models.CASCADE)
    content = models.TextField()

class Photo(models.Model):
    request_target = models.ForeignKey('Request', on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/')