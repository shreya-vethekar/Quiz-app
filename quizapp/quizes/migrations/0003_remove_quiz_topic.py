# Generated by Django 3.2.8 on 2021-11-22 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='topic',
        ),
    ]
