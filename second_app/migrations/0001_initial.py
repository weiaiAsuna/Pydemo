# Generated by Django 2.2.12 on 2020-05-11 09:09

from django.db import migrations, models
import second_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('img', models.ImageField(default='', upload_to=second_app.models.image_upload_to, verbose_name='图片路径')),
            ],
        ),
    ]
