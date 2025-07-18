# Generated by Django 5.1.6 on 2025-06-26 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("user", "User"), ("admin", "Admin")],
                default="user",
                max_length=5,
                verbose_name="user type",
            ),
        ),
    ]
