# Generated by Django 5.0.6 on 2024-05-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(default='No subject', max_length=200),
        ),
    ]
