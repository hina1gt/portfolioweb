# Generated by Django 4.2.6 on 2023-10-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_created_alter_post_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=29),
        ),
    ]
