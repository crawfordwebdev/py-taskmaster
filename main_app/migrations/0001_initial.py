# Generated by Django 4.1 on 2022-08-04 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('reward', models.CharField(max_length=100)),
                ('penalty', models.CharField(max_length=100)),
                ('priority', models.CharField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Emergency')], default=3, max_length=1)),
            ],
        ),
    ]