# Generated by Django 3.0.6 on 2020-06-19 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_auto_20200615_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertweetsmodel',
            name='topic',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]