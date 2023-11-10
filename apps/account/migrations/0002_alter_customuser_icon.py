# Generated by Django 4.2.6 on 2023-11-06 12:15

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='icon',
            field=image_optimizer.fields.OptimizedImageField(blank=True, null=True, upload_to='user-icons'),
        ),
    ]
