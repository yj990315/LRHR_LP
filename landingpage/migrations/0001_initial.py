# Generated by Django 3.2 on 2021-05-28 11:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose_of_estimate', models.CharField(choices=[('a', '수선'), ('l', '세탁'), ('r', '리폼')], default='a', help_text='패피스에 고객님의 소중한 상품을 맡기시는 목적을 선택해주세요.', max_length=1)),
                ('type_of_product', models.CharField(choices=[('a', '가방/핸드백'), ('b', '아우터'), ('c', '상의'), ('d', '하의'), ('e', '신발'), ('f', '지갑/벨트'), ('g', '패션 잡화'), ('h', '기타')], default='a', help_text='고객님의 상품의 종류를 선택해주세요', max_length=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='고객님의 이름을 입력해주세요.', max_length=10)),
                ('phone_number', models.CharField(help_text='고객님의 전화 번호를 입력해주세요.', max_length=11, validators=[django.core.validators.MinLengthValidator(10, '- 없이 전화번호만 입력해주십시오'), django.core.validators.MaxLengthValidator(12, '- 없이 전화번호만 입력해주십시오')])),
                ('address', models.TextField(help_text='고객님의 주소를 입력해주세요.')),
                ('age', models.CharField(help_text='고객님의 나이를 입력해주세요.', max_length=3)),
                ('gender', models.CharField(choices=[('m', '남자'), ('f', '여자')], default='m', help_text='고객님의 성별을 선택해주세요', max_length=1)),
                ('request_content', models.TextField(default='전달하실 요청사항을 자세히 입력해주세요.', max_length=1000)),
                ('overall_image', models.ImageField(upload_to='overall-image/')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_image', models.ImageField(upload_to='detail-image/')),
                ('estimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landingpage.estimate')),
            ],
        ),
    ]
