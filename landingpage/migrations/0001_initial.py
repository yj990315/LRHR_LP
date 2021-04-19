# Generated by Django 3.2 on 2021-04-16 02:21

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
                ('status', models.CharField(blank=True, choices=[('a', 'Alteration'), ('l', 'Laundry'), ('r', 'Reform')], default='a', help_text='패피스에 고객님의 소중한 상품을 맡기시는 목적을 선택해주세요.', max_length=1)),
                ('type_of_product', models.CharField(blank=True, choices=[('b', 'Bag'), ('t', 'Trouser'), ('s', 'Shoe')], default='b', help_text='고객님의 상품의 종류를 선택해주세요', max_length=1)),
                ('brand', models.CharField(help_text='고객님의 상품의 브랜드를 선택해주세요', max_length=100)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('estimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landingpage.estimate')),
            ],
        ),
    ]
