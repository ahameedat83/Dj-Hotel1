# Generated by Django 3.1.1 on 2020-09-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]