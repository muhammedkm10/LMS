# Generated by Django 5.1.1 on 2024-09-25 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("TeacherApp", "0004_quiz"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="question_index",
            field=models.IntegerField(default=0),
        ),
    ]
