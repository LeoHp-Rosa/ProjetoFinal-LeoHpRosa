# Generated by Django 4.0.7 on 2023-07-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('date', models.DateField()),
                ('link', models.URLField(blank=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
