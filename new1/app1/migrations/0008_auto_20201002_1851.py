# Generated by Django 3.0.7 on 2020-10-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20201002_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
