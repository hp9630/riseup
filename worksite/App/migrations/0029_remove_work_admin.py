# Generated by Django 5.0.2 on 2024-08-23 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0028_alter_work_admin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="work",
            name="admin",
        ),
    ]
