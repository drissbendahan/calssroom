# Generated by Django 3.2 on 2021-05-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20210514_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cour',
            name='dt',
            field=models.DateField(),
        ),
    ]
