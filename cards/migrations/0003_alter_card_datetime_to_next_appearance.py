# Generated by Django 4.0.1 on 2022-02-27 03:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_card_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='datetime_to_next_appearance',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]