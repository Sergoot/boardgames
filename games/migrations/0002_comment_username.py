# Generated by Django 4.0.2 on 2022-02-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='гость', max_length=255),
        ),
    ]