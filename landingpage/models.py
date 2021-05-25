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
        default='a',
        help_text='패피스에 고객님의 소중한 상품을 맡기시는 목적을 선택해주세요.',
    )
    TYPE = (
        ('a', '가방/핸드백'),
        ('b', '아우터'),
        ('c', '상의'),
        ('d', '하의'),
        ('e', '신발'),
        ('f', '지갑/벨트'),
        ('g', '패션 잡화'),
        ('h', '기타'),
    )
    type_of_product = models.CharField(
        max_length = 1,
        choices = TYPE,
        default = 'a',
        help_text='고객님의 상품의 종류를 선택해주세요',
    )
    create_date = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 10, help_text = '고객님의 이름을 입력해주세요.')
    phone_number = models.CharField(max_length = 11, help_text = '고객님의 전화 번호를 입력해주세요.')
    address = models.TextField(help_text = '고객님의 주소를 입력해주세요.')
    age = models.CharField(max_length = 3, help_text='고객님의 나이를 입력해주세요.')
    GENDER = (
        ('m', '남자'),
        ('f', '여자'),
    )
    gender = models.CharField(
        max_length = 1,
        choices = GENDER,
        default = 'm',
        help_text='고객님의 성별을 선택해주세요',
    )
    request_content = models.TextField(max_length=1000, default='전달하실 요청사항을 자세히 입력해주세요.')
    labels = {
        'purpose_of_estimate': ' ',
    }
    overall_image = models.ImageField(upload_to='overall-image/')
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

class Photo(models.Model):
    estimate = models.ForeignKey('Estimate', on_delete = models.CASCADE)
    detail_image = models.ImageField(upload_to='detail-image/')