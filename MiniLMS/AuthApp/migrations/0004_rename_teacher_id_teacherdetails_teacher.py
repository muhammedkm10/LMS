# Generated by Django 5.1.1 on 2024-09-24 16:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("AuthApp", "0003_teacherdetails"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teacherdetails",
            old_name="teacher_id",
            new_name="teacher",
        ),
    ]
