# Generated by Django 3.2 on 2021-05-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_alter_document_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='cour',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='document',
            name='files',
            field=models.FileField(upload_to='Docs'),
        ),
    ]
