# Generated by Django 4.0.1 on 2022-02-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('definition', models.CharField(max_length=255)),
                ('datetime_to_next_appearance', models.DateTimeField(auto_now_add=True)),
                ('number_times_incorrect', models.IntegerField(default=0)),
                ('bin', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddConstraint(
            model_name='card',
            constraint=models.CheckConstraint(check=models.Q(('number_times_incorrect__range', (0, 10))), name='cards_card_number_times_incorrect_range'),
        ),
        migrations.AddConstraint(
            model_name='card',
            constraint=models.CheckConstraint(check=models.Q(('bin__range', (0, 11))), name='cards_card_bin_range'),
        ),
    ]
