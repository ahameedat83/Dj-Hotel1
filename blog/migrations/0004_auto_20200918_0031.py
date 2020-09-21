# Generated by Django 3.1.1 on 2020-09-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='author_mail',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('NOTE', 'NOTE'), ('BIG NOTE', 'BIG NOTE')], default='NOTE', max_length=20),
        ),
    ]
