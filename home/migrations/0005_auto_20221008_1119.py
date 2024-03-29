# Generated by Django 3.2.7 on 2022-10-08 10:19

from django.db import migrations, models
import notez.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220926_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image1',
            field=models.ImageField(storage=notez.storage_backends.PublicMediaStorage(), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image2',
            field=models.ImageField(storage=notez.storage_backends.PublicMediaStorage(), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image3',
            field=models.ImageField(storage=notez.storage_backends.PublicMediaStorage(), upload_to='uploads/'),
        ),
    ]
