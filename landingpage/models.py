from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
phone_min_validator = MinLengthValidator(10, "- 없이 올바른 전화번호를 입력했는지 확인해주세요.")
phone_max_validator = MaxLengthValidator(12, "- 없이 올바른 전화번호를 입력했는지 확인해주세요.")
class Estimate(models.Model):
    PURPOSE = (
        ('a', '수선'),
        ('l', '세탁'),
        ('r', '리폼'),
        ('d', '선택 안함')
    )
    purpose_of_estimate = models.CharField(
        max_length=1,
        choices=PURPOSE,
        default='d',
        help_text='패피스에 고객님의 소중한 상품을 맡기시는 목적을 선택해주세요.',
    )
    TYPE = (
        ('a', '가방/핸드백'),
        ('e', '신발'),
        ('f', '지갑/벨트'),
        ('b', '의류'),
        ('g', '패션 잡화'),
    )
    type_of_product = models.CharField(
        max_length = 1,
        choices = TYPE,
        default = 'a',
        help_text='고객님의 상품의 종류를 선택해주세요',
    )
    create_date = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 10, help_text = '고객님의 이름을 입력해주세요.')
    phone_number = models.CharField(max_length = 11, help_text = '고객님의 전화 번호를 입력해주세요.', validators=[phone_min_validator, phone_max_validator])
    address = models.TextField(help_text = '고객님의 주소를 입력해주세요.')
    request_content = models.TextField(max_length=1000, default='전달하실 요청사항을 자세히 입력해주세요.')
    labels = {
        'purpose_of_estimate': ' ',
    }
    is_done = models.BooleanField(default=False)
    brand = models.TextField(max_length=20, blank=True)
    price = models.TextField(max_length=20, blank=True)
    YEAR = (
        ('0', '기억 안 남'),
        ('1', '2021년'),
        ('2', '2020년'),
        ('3', '2019년'),
        ('4', '2018년'),
        ('5', '2017년'),
        ('6', '2016년'),
        ('7', '2015년'),
        ('8', '2014년'),
        ('9', '2013년'),
        ('10', '2012년'),
        ('11', '2011년'),
        ('12', '2010년'),
        ('13', '2009년'),
        ('14', '2008년'),
        ('15', '2007년'),
        ('16', '2006년'),
        ('17', '2005년'),
        ('18', '2004년'),
        ('19', '2003년'),
        ('20', '2002년'),
        ('21', '2001년'),
        ('22', '2000년 이전'),
    )
    year = models.CharField(
        max_length = 2,
        choices = YEAR,
        default='1',
        blank=False,
    )
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

class OverallImage(models.Model):
    estimate = models.ForeignKey('Estimate', on_delete = models.CASCADE)
    overall_image = models.ImageField(upload_to='overall-image/')

class DetailImage(models.Model):
    estimate = models.ForeignKey('Estimate', on_delete = models.CASCADE)
    detail_image = models.ImageField(upload_to='detail-image/')