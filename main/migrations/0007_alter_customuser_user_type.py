# Generated by Django 5.1.6 on 2025-06-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_customuser_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("1", "admin"), ("2", "subadmin")], default="1", max_length=2
            ),
        ),
    ]
