# Generated by Django 3.2 on 2021-05-21 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='doc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.document'),
        ),
    ]
