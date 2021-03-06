# Generated by Django 3.2 on 2021-07-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0007_auto_20210616_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='purpose_of_estimate',
            field=models.CharField(choices=[('a', '수선'), ('l', '세탁'), ('r', '리폼'), ('d', '선택 안함')], default='d', help_text='패피스에 고객님의 소중한 상품을 맡기시는 목적을 선택해주세요.', max_length=1),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='type_of_product',
            field=models.CharField(choices=[('a', '가방/핸드백'), ('e', '신발'), ('f', '지갑/벨트'), ('b', '의류'), ('g', '패션 잡화')], default='a', help_text='고객님의 상품의 종류를 선택해주세요', max_length=1),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='year',
            field=models.CharField(choices=[('0', '기억 안 남'), ('1', '2021년'), ('2', '2020년'), ('3', '2019년'), ('4', '2018년'), ('5', '2017년'), ('6', '2016년'), ('7', '2015년'), ('8', '2014년'), ('9', '2013년'), ('10', '2012년'), ('11', '2011년'), ('12', '2010년'), ('13', '2009년'), ('14', '2008년'), ('15', '2007년'), ('16', '2006년'), ('17', '2005년'), ('18', '2004년'), ('19', '2003년'), ('20', '2002년'), ('21', '2001년'), ('22', '2000년 이전')], default='1', max_length=2),
        ),
    ]
