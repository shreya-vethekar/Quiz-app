# Generated by Django 3.2.8 on 2021-11-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_alter_answer_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]