# Generated by Django 3.2.8 on 2021-11-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_alter_answer_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct_answer',
            field=models.BooleanField(default=False),
        ),
    ]
