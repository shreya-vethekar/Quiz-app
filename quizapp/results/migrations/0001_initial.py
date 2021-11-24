# Generated by Django 3.2.8 on 2021-11-24 08:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20211124_1421'),
        ('questions', '0006_alter_answer_correct_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user_answer', models.CharField(max_length=200)),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.answer')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
