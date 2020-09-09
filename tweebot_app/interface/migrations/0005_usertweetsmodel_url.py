# Generated by Django 3.0.6 on 2020-06-23 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_user_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertweetsmodel',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]