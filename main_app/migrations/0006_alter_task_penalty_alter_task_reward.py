# Generated by Django 4.1 on 2022-08-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_penalty_reward_remove_task_penalty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='penalty',
            field=models.ManyToManyField(blank=True, to='main_app.penalty'),
        ),
        migrations.AlterField(
            model_name='task',
            name='reward',
            field=models.ManyToManyField(blank=True, to='main_app.reward'),
        ),
    ]
