# Generated by Django 4.2.6 on 2023-10-29 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
